def recc(a, n):
    if n == 0:
        return
    else:
        return a * recc(a, n - 1)


print(recc(int(input()),int(input())))