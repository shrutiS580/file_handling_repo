def execution_time(func):
    def wrapper(num):
        print("Function Started")

        func(num)

        print("Function Finished")

    return wrapper


@execution_time
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("Factorial =", fact)


factorial(5)