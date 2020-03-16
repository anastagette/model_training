def rec_lineral_sum(some_list):
    if not some_list:
        return 0
    else:
        return some_list[0] + rec_lineral_sum(some_list[1:])

some_list = [1.09, 2.05, 3.89]

print(rec_lineral_sum(some_list))
