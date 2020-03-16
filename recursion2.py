some_list = [1, 2, 3]


def rec_list_len(some_list):
    if not some_list:
        return 0
    else:
        return 1 + rec_list_len(some_list[1:])


print(rec_list_len(some_list))