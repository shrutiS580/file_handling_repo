sentence = input("Enter a sentence: ")

words = sentence.split()

print("List of words:", words)

longest = max(words, key=len)

print("Longest word:", longest)
