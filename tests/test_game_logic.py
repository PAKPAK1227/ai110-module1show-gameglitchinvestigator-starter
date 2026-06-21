"""Unit tests for the refactored game logic in ``logic_utils``.

Covers the three bugs investigated in this module:
  * the high/low hint bug in ``check_guess``
  * the scoring bug in ``update_score``
  * the New Game reset/freeze bug in ``new_game_state``

``check_guess`` returns a ``(outcome, message)`` tuple — the contract app.py
relies on via ``outcome, message = check_guess(...)`` — so tests unpack it.
"""

import os
import sys

# Make the project root importable so `logic_utils` resolves regardless of the
# directory pytest is invoked from.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess, update_score, new_game_state


# --- Starter tests: basic outcome contract for check_guess -------------------


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win.
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, the outcome should be "Too High".
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, the outcome should be "Too Low".
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Tests targeting the high/low hint bug fixed in check_guess --------------
#
# The original bug: when a guess was higher than the secret, the game told the
# player to "Go HIGHER!" (and vice versa) — the hint messages were paired with
# the wrong outcome branches. These tests lock in the corrected behavior.


def test_guess_too_high_tells_player_to_go_lower():
    """A guess above the secret must steer the player DOWN."""
    outcome, message = check_guess(80, 42)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_guess_too_low_tells_player_to_go_higher():
    """A guess below the secret must steer the player UP."""
    outcome, message = check_guess(10, 42)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_correct_guess_wins():
    outcome, message = check_guess(42, 42)
    assert outcome == "Win"
    assert "Correct" in message


# --- Tests targeting the scoring bug fixed in update_score -------------------
#
# The original bug: a correct guess failed to meaningfully increase the score,
# and the score could stay negative even after a win because
#   - the win bonus was over-penalized by an off-by-one and clamped near zero,
#   - a wrong "Too High" guess on even attempts *added* points, and
#   - wrong-guess penalties could drive the score arbitrarily negative.


def test_win_increases_score():
    """A correct guess must increase the score."""
    assert update_score(0, "Win", 2) > 0


def test_first_guess_win_awards_full_bonus():
    """Winning on the first guess should award the top (un-eroded) bonus,
    not the clamped-to-floor value the off-by-one used to produce."""
    # attempts starts at 1 and is pre-incremented, so the first guess passes 2.
    assert update_score(0, "Win", 2) == 90


def test_win_recovers_a_negative_score():
    """Even a late win must leave the player better off, never stuck negative."""
    assert update_score(0, "Win", 8) > 0


def test_too_high_never_rewards_points():
    """A wrong 'Too High' guess must never increase the score, on any attempt.

    This is the regression that let an even-numbered 'Too High' add +5.
    """
    for attempt in range(1, 9):
        assert update_score(50, "Too High", attempt) <= 50


def test_too_high_and_too_low_penalize_equally():
    """Both wrong outcomes should cost the same, regardless of attempt parity."""
    for attempt in range(1, 9):
        assert update_score(50, "Too High", attempt) == update_score(
            50, "Too Low", attempt
        )


def test_penalty_never_goes_negative():
    """Wrong guesses must not drive the score below zero."""
    assert update_score(0, "Too Low", 3) == 0
    assert update_score(0, "Too High", 4) == 0
    assert update_score(3, "Too Low", 3) == 0


def test_win_bonus_has_a_floor():
    """A very late win still awards at least the minimum bonus (never <= 0)."""
    assert update_score(0, "Win", 100) >= 10


# --- Tests targeting the New Game reset bug ----------------------------------
#
# The original bug: clicking "New Game" reset `attempts` and `secret` but left
# `status` untouched. After a finished game, `status` stayed "won"/"lost", so
# the app's guard short-circuited with st.stop() on every rerun — the board
# froze: submitting did nothing, attempts never moved, no hint appeared, and
# even the correct number had no effect. A new round must restore status to
# "playing" (and clear the previous score/history).


def test_new_game_resets_status_to_playing():
    """The core of the freeze bug: a new game must clear a stale status.

    This is the regression that left status as "won"/"lost" and tripped the
    st.stop() guard, freezing the board.
    """
    assert new_game_state(42)["status"] == "playing"


def test_new_game_clears_score_and_history():
    """A new round must not inherit the previous game's score or guesses."""
    state = new_game_state(42)
    assert state["score"] == 0
    assert state["history"] == []


def test_new_game_uses_provided_secret():
    """The fresh state carries the secret chosen for the new round."""
    assert new_game_state(7)["secret"] == 7


def test_new_game_is_fully_playable_after_a_finished_game():
    """End-to-end: a finished 'won' game, then New Game, must be playable.

    Simulates the exact bug scenario — the prior state is 'won' with score and
    history — and asserts the reset produces a clean, playing state so a
    subsequent guess would be accepted instead of hitting st.stop().
    """
    finished = {
        "secret": 13,
        "attempts": 8,
        "score": 120,
        "status": "won",
        "history": [10, 13],
    }

    fresh = new_game_state(55)

    assert finished["status"] == "won"  # precondition: the board was frozen
    assert fresh["status"] == "playing"
    assert fresh["attempts"] == 1
    assert fresh["score"] == 0
    assert fresh["history"] == []
