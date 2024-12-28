import time
import random

# Load sentences from a text file
def load_sentences():
    try:
        with open("sentences.txt", "r") as file:
            sentences = [line.strip() for line in file.readlines()]
        if not sentences:
            raise ValueError("The sentences file is empty.")
        return sentences
    except FileNotFoundError:
        print("Error: The file 'sentences.txt' was not found. Please create it with some sentences.")
        exit()
    except ValueError as e:
        print(f"Error: {e}")
        exit()

# Save score to leaderboard
def save_to_leaderboard(name, wpm, accuracy):
    try:
        with open("leaderboard.txt", "a") as file:
            file.write(f"{name},{wpm:.2f},{accuracy:.2f}\n")
    except Exception as e:
        print(f"Error saving to leaderboard: {e}")

# Display leaderboard
def display_leaderboard():
    print("\n--- Leaderboard ---")
    try:
        with open("leaderboard.txt", "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
            scores = sorted(scores, key=lambda x: float(x[1]), reverse=True)  # Sort by WPM
            print(f"{'Rank':<5}{'Name':<15}{'WPM':<10}{'Accuracy':<10}")
            for rank, (name, wpm, accuracy) in enumerate(scores[:10], start=1):
                print(f"{rank:<5}{name:<15}{wpm:<10}{accuracy:<10}")
    except FileNotFoundError:
        print("No leaderboard data available yet.")
    except Exception as e:
        print(f"Error reading leaderboard: {e}")

def typing_speed_test():
    # Load sentences from file
    sentences = load_sentences()

    # Choose a random sentence
    sentence = random.choice(sentences)

    # Display the sentence
    print("\nType the following sentence:")
    print(sentence)

    # Ask user to start
    input("\nPress Enter when you're ready to start typing...")

    # Record start time
    start_time = time.time()

    # Get user input for typing the sentence
    typed_sentence = input("\nStart typing here: ")

    # Record end time
    end_time = time.time()

    # Calculate elapsed time and speed
    elapsed_time = end_time - start_time
    word_count = len(sentence.split())
    wpm = (word_count / elapsed_time) * 60

    # Calculate accuracy
    original_words = sentence.split()
    typed_words = typed_sentence.split()

    correct_words = 0
    for orig, typed in zip(original_words, typed_words):
        if orig == typed:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100

    # Display results
    print(f"\nResults:")
    print(f"Time Taken: {elapsed_time:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

    # Get player's name
    name = input("\nEnter your name for the leaderboard: ")

    # Save to leaderboard
    save_to_leaderboard(name, wpm, accuracy)

    # Display leaderboard
    display_leaderboard()

# Run the typing test
typing_speed_test()
