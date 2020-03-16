def find_mountain(heightsMap):
    l_coord = [[heightsMap.index(i), i.index(max(i))] for i in heightsMap]
    l_hmax = [max(i) for i in heightsMap]
    print (l_coord[l_hmax.index(max(l_hmax))])
find_mountain([[1, 2, 3], [4, 5, 7], [6, 8, 0]])