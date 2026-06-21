def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        # FIX: swapped the hint messages so "Too High" steers DOWN and "Too Low" steers UP
        if guess > secret:
            # Guess is above the secret, so the secret is lower.
            return "Too High", "📉 Go LOWER!"
        else:
            # Guess is below the secret, so the secret is higher.
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # FIX: coerce both sides to str so mixed int/str inputs compare instead of crashing
        g = str(guess)
        secret = str(secret)
        if g == secret:
            return "Win", "🎉 Correct!"
        # FIX: same swapped-hint correction applied to the fallback branch
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    A win awards points that scale down with how many attempts were used,
    but never below a meaningful floor, so a correct guess always increases
    the score. Wrong guesses cost a small, consistent penalty and can never
    push the score below zero (so a later win can still recover it).
    """
    if outcome == "Win":
        # FIX: corrected off-by-one (attempt_number - 1) so a fast win awards the full bonus
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    # FIX: both wrong outcomes now penalize equally and clamp at 0 (was rewarding even "Too High" and going negative)
    if outcome in ("Too High", "Too Low"):
        return max(0, current_score - 5)

    return current_score


def new_game_state(secret: int):
    """Build a fresh game state dict for the start of a new round.

    Starting a new game means clearing *every* piece of per-game state. The
    critical field is ``status``: it gates whether the app accepts input, and
    leaving a stale ``"won"``/``"lost"`` value behind was the New Game bug.
    With status not reset, the app's guard short-circuited via ``st.stop()``
    and the board appeared frozen — submitting did nothing, attempts never
    moved, and no hint showed. ``score`` and ``history`` are reset too so a new
    round does not inherit the previous game's totals, and ``attempts`` matches
    the initial session default so a reset game plays identically to a fresh
    load.
    """
    # FIX: reset status to "playing" (and clear score/history) so New Game no longer freezes the board
    return {
        "secret": secret,
        "attempts": 1,
        "score": 0,
        "status": "playing",
        "history": [],
    }
