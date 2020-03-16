def check(login, i):
    if i < len(login):
        if not login[i] in alp_lat and login[i].isdigit() != True and login[i] != "_":
            print(login[i])
            return None
        check(login, i+1)
    else:
        print('OK')
        return None
alp_lat = {chr(i) for i in range (ord('a'),ord('z')+1)}
check(input(), 0)