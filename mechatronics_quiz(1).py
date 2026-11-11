# Author: Adeniran Francis Adeyemi
# Mechatronics Quiz App
# A short multiple-choice quiz on mechatronics basics.
# My own twist: questions are shuffled each time, and at the end the
# program shows a review of the questions I got wrong, with explanations.

import random  # used to shuffle the order of the questions

# ---------------------------------------------------------------
# QUESTION BANK (stored in lists)
# ---------------------------------------------------------------
questions = [
    "What does a resistor do in a circuit?",
    "Which component converts electrical energy into rotational motion?",
    "What does a sensor do in a mechatronic system?",
    "What is the unit of electrical current?",
    "Which device is the 'brain' of many mechatronic systems?",
    "Ohm's law states that V equals...",
    "Which sensor would you use to detect how close an object is without touching it?",
    "What does LED stand for?",
]

# Each inner list holds the 4 choices for the question at the same position
options = [
    ["Stores electric charge", "Opposes the flow of current", "Amplifies voltage", "Produces light"],
    ["Capacitor", "Diode", "Electric motor", "Transformer"],
    ["Moves a load", "Stores energy", "Measures a physical quantity", "Cuts power"],
    ["Volt", "Ampere", "Ohm", "Watt"],
    ["Microcontroller", "Resistor", "Switch", "Fuse"],
    ["I divided by R", "I multiplied by R", "R multiplied by P", "I plus R"],
    ["Potentiometer", "Thermistor", "Ultrasonic sensor", "Push button"],
    ["Low Energy Diode", "Light Emitting Diode", "Linear Electric Device", "Light Energy Display"],
]

# The correct choice number (1 to 4) for each question
answers = [2, 3, 3, 2, 1, 2, 3, 2]

# A short explanation for each question, used in the review
explanations = [
    "A resistor opposes (limits) the flow of current.",
    "An electric motor turns electrical energy into rotation.",
    "Sensors measure things like temperature, distance or light.",
    "Current is measured in amperes (amps).",
    "A microcontroller reads inputs and controls outputs.",
    "Ohm's law: V = I x R.",
    "An ultrasonic sensor measures distance using sound waves.",
    "LED means Light Emitting Diode.",
]


# ---------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------
def get_choice(number_of_options):
    """Keep asking until the user types a valid number. Returns an int."""
    while True:
        text = input("Your answer (1-" + str(number_of_options) + "): ").strip()
        try:
            choice = int(text)  # convert the typed text to a whole number
        except ValueError:
            print("  Please type a number, not letters or symbols.")
            continue
        if 1 <= choice <= number_of_options:
            return choice
        print("  That number is not an option. Choose 1 to " + str(number_of_options) + ".")


def get_grade(percentage):
    """Return a grade and a message based on the percentage score."""
    if percentage >= 80:
        return "Excellent! Grade A - you think like a mechatronics engineer."
    elif percentage >= 60:
        return "Good job! Grade B - a little more revision and you will be top."
    elif percentage >= 40:
        return "Fair. Grade C - go back over your notes and try again."
    else:
        return "Keep practising. Grade F - do not give up, try again!"


def run_quiz():
    """Run one full round of the quiz. Returns the score as a percentage."""
    score = 0
    wrong_ones = []  # list of question numbers answered wrongly

    # Shuffle the order of the questions (my own twist)
    order = list(range(len(questions)))
    random.shuffle(order)

    # Loop through every question in the shuffled order
    for number, i in enumerate(order, start=1):
        print("\nQuestion " + str(number) + " of " + str(len(order)))
        print(questions[i])
        for position, choice_text in enumerate(options[i], start=1):
            print("  " + str(position) + ". " + choice_text)

        choice = get_choice(len(options[i]))

        # Check the answer
        if choice == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong. The right answer was " + str(answers[i]) + ". " + options[i][answers[i] - 1])
            wrong_ones.append(i)

    # Work out and show the final result
    percentage = score / len(order) * 100
    print("\n" + "=" * 40)
    print("You scored " + str(score) + " out of " + str(len(order)))
    print("Percentage: " + str(round(percentage, 1)) + "%")
    print(get_grade(percentage))

    # Review of mistakes (my own twist)
    if len(wrong_ones) > 0:
        print("\nREVIEW - questions you missed:")
        for i in wrong_ones:
            print("- " + questions[i])
            print("  " + explanations[i])
    else:
        print("\nPerfect score, nothing to review!")

    return percentage


# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------
print("=== MECHATRONICS QUIZ APP ===")
print("Type the number of the answer you think is correct.")

best_score = 0  # keeps the best percentage in this session

playing = True
while playing:
    result = run_quiz()
    if result > best_score:
        best_score = result
    print("Best score this session: " + str(round(best_score, 1)) + "%")

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        playing = False

print("Thanks for playing. Goodbye!")
