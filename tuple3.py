n_list = []
for i in range(int(input())):
    n_list.append(int(input()))
for i in range(len(n_list)):
    print(max(n_list))
    n_list.remove(max(n_list))