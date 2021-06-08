def fib_gen(do_ktorej):
    fib=[1, 1]
    i = 1
    while i < do_ktorej:
        fib.append(fib[i-1]+fib[i])
        i += 1
    return fib[do_ktorej - 1]

print(fib_gen(int(input("Do której: "))))