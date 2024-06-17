def highest_frequency_char_count(sentence):
    # Split the sentence into words
    words = sentence.split()


# store the length of the word in list
    lengths = [len(word) for word in words]
    return max(lengths)
    
sentence = input()
highest_freq = highest_frequency_char_count(sentence)
print(f"The highest occurrences of word lengths is:", highest_freq)