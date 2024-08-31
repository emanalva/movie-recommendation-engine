# Title: cosine_similarity
# Author: Emanuel Alvarez
# Origin Date: August 30, 2024

# Libraries
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances

# Count num of words per entry of list of string
def count_words_scikit(text):
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit the model and transform the text into a word count matrix
    word_count_matrix = vectorizer.fit_transform(text)
    
    # Convert the matrix to a dense format (list of lists) and get the feature names
    word_counts = word_count_matrix.toarray()
    # unique_words = vectorizer.get_feature_names_out() # list of unique words for visualization

    # Save cosine similarity before returning
    cos_sim = cosine_similarity(word_count_matrix)
    euc_dist = euclidean_distances(word_count_matrix)
    
    return word_counts, cos_sim, euc_dist
# end count_words_scikit()

# Input example: to be analyzed
text = ["London Paris London", "Paris Paris London"]

# Save list
word_count, cos_sim, euc_dis = count_words_scikit(text)
print(f"\n {word_count} \n\n {cos_sim} \n\n {euc_dis} \n")



