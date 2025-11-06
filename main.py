import time
import datetime
from puzzle_generator import generate_puzzle
from tracker import Tracker
from adaptive_engine import next_difficulty

def ask_float(prompt):
    """Helper function to safely get a number input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number (like 12 or 3.5).")

def run_session():
    print("✨ Welcome to Math Adventures — Adaptive Learning App ✨\n")

    # Get learner info
    name = input("Enter student name: ").strip() or "Student"
    level = input("Choose starting difficulty (Easy / Medium / Hard): ").title()
    if level not in ("Easy", "Medium", "Hard"):
        print("Invalid choice, defaulting to Easy.")
        level = "Easy"

    tracker = Tracker()
    puzzles_per_round = 5

    for i in range(puzzles_per_round):
        question, answer = generate_puzzle(level)
        print(f"\nPuzzle {i+1}/{puzzles_per_round} (Level: {level}) ➤  {question}")
        start_time = time.time()
        user_ans = ask_float("Your answer: ")
        end_time = time.time()

        time_taken = end_time - start_time
        correct = False
        if answer is not None and abs(user_ans - answer) < 0.01:
            correct = True

        tracker.record(correct, time_taken)
        if correct:
            print(f"✅ Correct! (Time taken: {time_taken:.2f}s)")
        else:
            print(f"❌ Wrong! Correct answer: {answer} (You took {time_taken:.2f}s)")

    # ---- Summary Section ----
    accuracy, avg_time = tracker.summary()
    recommended = next_difficulty(level, accuracy, avg_time)

    print("\n📊 --- SESSION SUMMARY --- 📊")
    print(f"Student Name: {name}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Average Time per Puzzle: {avg_time:.2f} seconds")
    print(f"Difficulty Transition: {level} → {recommended}")
    print("\nThank you for playing! 🌟 Keep learning and improving!")

    # ---- Save session log ----
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = (
        f"Date: {timestamp}\n"
        f"Student: {name}\n"
        f"Starting Level: {level}\n"
        f"Recommended Level: {recommended}\n"
        f"Accuracy: {accuracy:.2f}%\n"
        f"Average Time: {avg_time:.2f} sec\n"
        "--------------------------------------\n"
    )

    with open("session_log.txt", "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    run_session()
