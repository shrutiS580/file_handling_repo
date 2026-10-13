from pathlib import Path
file_path = Path(__file__).parent / "file.txt"
with open(file_path, "r") as file:
    content = file.read()
words = content.split()
print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)
