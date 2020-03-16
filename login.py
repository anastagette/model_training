alp_lat = {chr(i) for i in range (ord('a'),ord('z')+1)}
print(alp_lat)
s = str(input())
for i in s:
    if i in alp_lat:
        print(i)