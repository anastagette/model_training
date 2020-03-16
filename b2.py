def LetterUp(a):
    a_list = a.lower().split()
    ex = []
    for i in a_list:
        ex.append(i[0].upper() + i[1:])
    a = ' '.join(ex)
    return print(ex, a)
LetterUp(input())

# a_list = input().split()
# c_list = []
# a = str()
# for i in a_list:
#     b_list = []
#     for j in i:
#         if i.index(j) == 0:
#             b_list.append(j.upper())
#         else:
#             b_list.append(j)
#     i = ''.join(b_list)
#     c_list.append(i)
#     a = ' '.join(c_list)
# print(a)
