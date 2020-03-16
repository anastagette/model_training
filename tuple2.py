n_list = []
m = int
for i in range(int(input())):
    n_list.append(int(input()))
nm = int(input())
for i in n_list:
    for j in n_list:
        if n_list.index(i) != n_list.index(j):
            if nm == i*j:
                m = nm
if nm != m:
    print('НЕТ')
else:
    print('ДА')
