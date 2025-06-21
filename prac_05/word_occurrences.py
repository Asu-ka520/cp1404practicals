"""
Word Occurrences Counter
Estimate: 25 minutes
Actual: 20 minutes
"""

# 1. Ask for user input
text = input("Text: ")

# 2. Split text into words
words = text.split()

# 3. Count word occurrences using a dictionary
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

# 4. Get a list of words, sorted alphabetically
sorted_words = sorted(counts.keys())

# 5. Find the length of the longest word for alignment
max_word_length = max(len(word) for word in sorted_words)

# 6. Print the results, aligned
for word in sorted_words:
    print(f"{word:<{max_word_length}} : {counts[word]}")