# Word Frequency Counter

# collections.Counter can count words in one line:
# Counter(sentence.split())

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = "Python is fun and Python is easy to learn"

result = word_frequency(sentence)

# Sort by frequency (highest to lowest)
sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)

print("Word Frequency:\n")

for word, count in sorted_result:
    print(f"{word}: {count}")
