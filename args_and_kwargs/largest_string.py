def largest_string(*args):
    largest= args[0]

    for i in args:
        if len(i) > len(largest):
            largest= i

    print(largest)

largest_string("riya","shruti", "priya","sita")            
    
