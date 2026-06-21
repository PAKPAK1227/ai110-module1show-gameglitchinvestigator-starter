# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- The game is intended to function as a light guessing game that gives hint to users to help them achieve their goal faster
- [ ] I found numerous bug such as: incorrect hints, incorrect score display, restart button causing the game to crash.
- [ ] I fixed the hints to help the user achieve the correct goal, let the score display correct positive scores when necessary, restart button now effectively achieves its purpose and doesn't shut down the game.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. **Launch the game.** Run `python -m streamlit run app.py`. The app opens with a sidebar where you pick a **Difficulty** (Easy, Normal, or Hard). Each difficulty sets the number range and how many attempts you get — e.g. Normal is 1–100 with 8 attempts.
2. **Read the game state.** The main panel shows how many attempts are left, and the "Developer Debug Info" expander reveals the secret number, current score, and your guess history — handy for verifying the fixes.
3. **Make a guess.** Type a number into the input box and click **Submit Guess**. The app parses your input, compares it to the secret, and shows a hint.
4. **Follow the (now correct) hints.** If your guess is too high, it tells you to **Go LOWER**; if too low, it tells you to **Go HIGHER** — the reversed-hint glitch is fixed, so the hints now point you toward the answer.
5. **Watch the score update.** A wrong guess costs 5 points but never drops the score below 0; a correct guess awards a bonus that's larger the fewer attempts you used, so winning always increases your score.
6. **Win the game.** When you guess the secret, the app celebrates with balloons, reveals the number, shows your final score, and marks the round as won.
7. **Start over.** Click **New Game** to reset the full state — secret, attempts, score, history, and status — so the board is immediately playable again (no more frozen screen after a finished game).

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
