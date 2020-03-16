def quarter(xcoord, ycoord):
    if xcoord >= 0:
        if ycoord >= 0:
            print('1 quarter')
        else:
            print('4 quarter')
    else:
        if ycoord >= 0:
            print('2 quarter')
        else:
            print('3 quarter')
quarter(int(input()),int(input()))