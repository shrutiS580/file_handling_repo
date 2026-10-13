from pathlib import Path

file_path = Path(__file__).parent / "file.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 4:
    print("2nd line:", lines[1].strip())
    print("4th line:", lines[3].strip())
else:
    print("The file must contain at least 4 lines.")
