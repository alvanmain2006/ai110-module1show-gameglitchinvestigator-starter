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

- [ ] Describe the game's purpose.
The game will give you some secret number that you must guess, you will be allow some attempts to guess based on the difficutlty of the game.
- [ ] Detail which bugs you found.
I found 3 bugs, if you guess higher it will give a hint and said lower. Another one is that it automatically convert our guesses into string for some reason. Lastly, the attempt count started at 1 instead of 0, which will offset the amount of attempts that we have.
- [ ] Explain what fixes you applied.
For bug 1, I just need to switch the hint string lower to higher and higher to lower.
For bug 2, I remove the code where it changed the guess into a string
For bug 3, I changed 1 back to 0 attempt
## 📸 Demo Walkthrough

1 Start the game by running streamlit run app.py, then choose Normal difficulty in the sidebar. The game should show the correct range and display 8 attempts left before any guess is submitted.
2 Test the attempt counter by entering your first guess, such as 50, and clicking Submit Guess. After submitting, the attempts left should decrease by exactly 1, so Normal mode should now show 7 attempts left, not start at 7 before playing.
3 Test the “too high” hint by using the debug secret number or picking a guess greater than the secret. For example, if the secret is 40, enter 60; the game should say the guess is Too High and tell the player to go lower.
4 Test the “too low” hint by entering a guess smaller than the secret. For example, if the secret is 40, enter 20; the game should say the guess is Too Low and tell the player to go higher.
5 Test the secret number type bug by making multiple guesses, including an even-numbered attempt. The game should compare guesses and the secret as numbers every time, so values like 9 and 10 should behave correctly instead of being compared like strings.


**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
