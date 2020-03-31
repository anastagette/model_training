#
# s = input().split(' ')
# for i in s:
#     if s.index(i) != len(s)-1:
#         print((str(int(s[s.index(i)-1]) + int(s[s.index(i)+1]))), end=' ')
#     elif len(s) == 1:
#         print(i)
#     else:
#         print((str(int(s[s.index(i) - 1]) + int(s[0]))))
# s = 'sdfghj'

# lst = input().split(' ')
# x = int(input())
# inds = []
# for i in lst:
#     if int(i) == x:
#         inds.append(str(lst.index(i)))
#         print(inds)
# if inds == False:
#     print('Отсутствует')
# else:
#     print(' '.join(inds))

# l1 = list()
# l2 = list()
#
# for i in input().split():
#     l1.append(int(i))
# for i in input().split():
#     l2.append(int(i))

n = int(input())
for i in range(n):
    w = input()
    for j in range(len(w)//2):
        if w[j] != w[-1-j]:
            print('false')
        else:
            print('true')

