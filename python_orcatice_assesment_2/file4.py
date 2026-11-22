def calculate_salary(basic_salary, bonus=2000):
    total_salary = basic_salary + bonus
    print("Total Salary:", total_salary)


# Positional Arguments
calculate_salary(30000)

# Keyword Arguments
calculate_salary(basic_salary=32000, bonus=3000)

# Default Arguments
calculate_salary(25000)