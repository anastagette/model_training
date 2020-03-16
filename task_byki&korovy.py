s1 = input()
s2 = input()
nb = 0
nk = 0
for i in s1:
    if i in s2:
        if s1.index(i) == s2.index(i):
            nb += 1
        else:
            nk += 1
print(nb, nk)

