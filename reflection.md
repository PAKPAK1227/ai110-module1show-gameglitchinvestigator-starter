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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
