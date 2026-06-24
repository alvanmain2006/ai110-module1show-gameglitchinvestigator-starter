# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked like a normal Streamlit number guessing game with a sidebar for difficulty, a text box for my guess, and buttons to submit or start a new game. I also saw a developer debug section that showed the secret number, attempts, score, difficulty, and history, which made the game easy to spoil. The first concrete bug I noticed was that the hints were backwards: a guess that was too high told me to go higher, and a guess that was too low told me to go lower. I also noticed that the attempts started at 1 instead of 0, so the game showed one fewer attempt than expected before I even submitted a guess. Another issue was that the game sometimes converted the secret number into a string on even attempts, which caused unreliable comparisons.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Secret is `50`, guess `60` | The game should say the guess is too high and tell the player to go lower. | The game returned `"Too High"` but displayed `"📈 Go HIGHER!"`, which pointed in the wrong direction. | none |
| Secret is `50`, guess `40` | The game should say the guess is too low and tell the player to go higher. | The game returned `"Too Low"` but displayed `"📉 Go LOWER!"`, which pointed in the wrong direction. | none |
| Start a Normal game without entering a guess | The game should show `8` attempts left because Normal mode allows 8 attempts. | The game started attempts at `1`, so it showed only `7` attempts left before the first guess. | none |
| On an even attempt with secret `10`, guess `9` | The game should compare both values as numbers and say the guess is too low. | The secret was converted to the string `"10"`, so comparison could fall back to string logic and give the wrong result. | none |
| Click `New Game` after already playing | The secret, attempts, score, status, and history should all reset for a fresh game. | Only attempts and secret reset; score, status, and history could carry over from the previous round. | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I am giving ChatGPT my code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
It gave me suggestion on how some code just have bad logic issues like attempts count being wrong, and type conversion being wrong. I verified the result by just chceking the code and playing the game multiple time
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
There was no misleading suggestion yet
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I tested it with pytest from Claude and played the game myself multiple times to assured
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I test the attempts logic by playing many games in a row as well as using pytest
- Did AI help you design or understand any tests? How?
It just generated specific test cases for specific situation that I am looking for.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Rerun is just a restart of the whole app everytime user interact with it, so new variable would be created each click.
Session state is what we need to keep the memory of the variable every rerun so we dont forget our old variable, for example: our secret number is 30 session state remembered that so every rerun does not create a new one

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Always ask AI to explain what it is intending to do, and why it is doing it. Also read your code clearly and read the readme clearly. I think I learned a lot from this project on how to use AI assissted coding. I now have to make sure I understand what my agent is doing, so I don't end up messed up my whole code base. I also need to think more as a captain and lead the AI in my favor.
