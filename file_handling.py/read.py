from pathlib import Path

path = Path(__file__).parent / "file.txt"

with open(path, "r") as file:
    content = file.read()

count = 0

for ch in content:
    if ch.lower() in "aeiou":
        count += 1

print("Total vowels:", count)
