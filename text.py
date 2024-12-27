import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing speed tests are fun and challenging.",
    "Practice makes a person perfect at typing.",
    "Coding every day improves problem-solving skills."
]

sentence = random.choice(sentences)

print("\nType the following sentence:")
print(sentence)
input("\nPress Enter when you're ready to start...")

start_time = time.time()

typed_sentence = input("\nStart typing here: ")

end_time = time.time()

elapsed_time = end_time - start_time
word_count = len(sentence.split())
wpm = (word_count / elapsed_time) * 60

original_words = sentence.split()
typed_words = typed_sentence.split()

correct_words = 0
for orig, typed in zip(original_words, typed_words):
    if orig == typed:
        correct_words += 1

accuracy = (correct_words / len(original_words)) * 100

print(f"\nResults:")
print(f"Time Taken: {elapsed_time:.2f} seconds")
print(f"Typing Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")

