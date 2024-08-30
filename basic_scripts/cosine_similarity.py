# Title: cosine_similarity
# Author: Emanuel Alvarez
# Origin Date: August 30, 2024

# Libraries
from collections import Counter

# Function to count the number of occurrences of words within a string, within each entry of a 2D list
def count_words_per_entry(text):
    # Get a set of unique words in the entire text array
    unique_words = set(' '.join(text).split())

    # Convert the set to a sorted list for consistent ordering
    unique_words = sorted(unique_words)

    # Prepare an outer list to hold the word counts for each entry
    word_counts_per_entry = []

    # Loop through each entry in the text array
    for entry in text:
        # Split the entry into individual words
        words = entry.split()
        
        # Count the occurrences of each unique word in the entry
        word_counts = [words.count(word) for word in unique_words]

        # Append the word counts list to the outer list
        word_counts_per_entry.append(word_counts)

    return word_counts_per_entry
# end count_words_per_entry()

# Input example: to be analyzed
text = ["London Paris London", "Paris Paris London"]

# Save list
word_count = count_words_per_entry(text)
print(word_count)