# Mechatronics Quiz App

## What it does
This is a short multiple-choice quiz on mechatronics basics. It asks 8 questions, checks each answer, keeps score, then shows a final percentage with a grade and message.

## How to run it
Install Python 3, then run: python mechatronics_quiz.py

## Sample output
```
=== MECHATRONICS QUIZ APP ===
Type the number of the answer you think is correct.

Question 1 of 8
What is the unit of electrical current?
  1. Volt
  2. Ampere
  3. Ohm
  4. Watt
Your answer (1-4): 2
Correct!

...

========================================
You scored 6 out of 8
Percentage: 75.0%
Good job! Grade B - a little more revision and you will be top.

REVIEW - questions you missed:
- Which device is the 'brain' of many mechatronic systems?
  A microcontroller reads inputs and controls outputs.
```

## My own twist
- Questions are shuffled every round, so no two rounds are the same.
- After the quiz, the program reviews the questions I got wrong and explains each correct answer.
- I can play again, and the program tracks my best score for the session.

## What I learned
- How to store questions, options and answers in parallel lists.
- How to check user input with try/except so the program does not crash when I type a letter instead of a number.

## Author
Adeniran Francis Adeyemi, ND1 Mechatronics Engineering Engineering, YabaTech.
