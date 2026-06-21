# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

1. The game looked clean when I first ran it simple format and ready to go
2. - The Hint was off as it would tell me to go higher when the answer was lower than my guess and go lower
     when the answer was higher than my guess

   - After clicking the new game button the game crashes. I enter a new guess and press submit but nothing happens
     my attempts number doesn't go down and a new hint doesn't appear. Nothing even happens when I enter the right number I simply have to restart

   - Additonally the score system is off when I finished guessing a correct answer my score didnt increase and it in fact remained negative



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input              | Expected Behavior          | Actual Behavior                | Console Output / Error |
|--------------------|----------------------------|--------------------------------|------------------------|
| guess 60           |     ("Too High" hint)      |      ("Too Low" hint)          |        "None"
|click restart button|      Game Restarts         |        Game Crashed            |        "None"
| guess right answer.|      Score increases       |.      Score stays negative.    |        "None"    

---

## 2. How did you use AI as a teammate?

- Claude chatbot & Claude Code
- "AI suggested I swap the string suggestions in the HIGH/LOW conditional check to fix the bug and it turned out to be the right approachl I verified the result by writitng a test case and also running the program myself to see if the logic made sense
- "AI suggested I created two seperate test files and I actually did at first but then that caused a lot of confusion, hence, I went back to the original version and appended all logic in the original test file"

---

## 3. Debugging and testing your fixes

- I generated a test case to see if it passed and also ran the program myself in streamlit to see if the logic made sense myself and was actually working at runtime
- One manual test I ran is the correct Hint test. I guessed lower than the actual score and it told me to go higher and vice versa
- Yes AI helped me design and generate some test cases to run in test_game_logic.py using specific logic it gave me and used to fix it

---

## 4. What did you learn about Streamlit and state?

- I learned that streamlit reruns the entire script top-to-bottom on every interaction: Every time you click a button, type in a box etc. st.session_state is the only thing that survives a rerun: its a dictionary that streamlit keeps alive across reruns.
---

## 5. Looking ahead: your developer habits

- I want to implement refactoring and generating test cases into my habits when building personal projects.
- I would read the code myself fully initially to try and make sense of it myself fully before moving to the chatbot.
- This project made me realize that humans are very much in the loop eventhough AI has automated a lot of the process that was previously done by humans
