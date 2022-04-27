def regression(n):
    if n == 1:
        return 0
    if n % 3 == 0:
        n/3
        print(n)
        return regression(n)
    if n % 2 == 0:
        n/2
        print(n)
        return regression(n)
    if n % 5 == 0:
        n/5
        print(n)
        return regression(n)


a = input("Введите число:")
print(regression(a))
