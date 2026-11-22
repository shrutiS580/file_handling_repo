from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() to find squares
squares = list(map(lambda x: x * x, numbers))

# Using filter() to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Using reduce() to find sum
total = reduce(lambda x, y: x + y, numbers)

print("Squares:", squares)
print("Even Numbers:", even_numbers)
print("Sum:", total)