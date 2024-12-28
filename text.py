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

def typing_speed_test():
    # Step 1: Load sentences from file
    sentences = load_sentences()

    # Step 2: Choose a random sentence
    sentence = random.choice(sentences)

    # Step 3: Display the sentence
    print("\nType the following sentence:")
    print(sentence)

    # Step 4: Ask user to start
    input("\nPress Enter when you're ready to start typing...")

    # Step 5: Record start time
    start_time = time.time()

    # Step 6: Get user input for typing the sentence
    typed_sentence = input("\nStart typing here: ")

    # Step 7: Record end time
    end_time = time.time()

    # Step 8: Calculate elapsed time and speed
    elapsed_time = end_time - start_time
    word_count = len(sentence.split())
    wpm = (word_count / elapsed_time) * 60

    # Step 9: Calculate accuracy
    original_words = sentence.split()
    typed_words = typed_sentence.split()

    correct_words = 0
    for orig, typed in zip(original_words, typed_words):
        if orig == typed:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100

    # Step 10: Display results
    print(f"\nResults:")
    print(f"Time Taken: {elapsed_time:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")

# Run the typing test
typing_speed_test()