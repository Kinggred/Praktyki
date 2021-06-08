fib = [0, 1]


def ciag(ile):
    if ile < 3:
        return fib[ile-1]
    else:
        while ile >= len(fib)+1:
            if ile > len(fib)+1:
                ciag(ile-1)
            elif ile == len(fib)+1:
                fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    return fib[ile - 1]


print(ciag(int(input("Podaj wartosc: "))))
