import math
st=input("Nhap xau: ")
i = 0
s =""
for i in range(len(st)):
    if (ord(st[i]) >= 65 and ord(st[i]) <=90) or (ord(st[i]) >= 97 and ord(st[i]) <=122):
        s = s + st[i]
i = 0
test = True
kq = True
while test == True and i < math.trunc(len(s)):
    if (ord(s[i]) != ord(s[len(s)-i-1])) and (ord(s[i]) != (ord(s[len(s)-i-1])+32)) and (ord(s[i]) != (ord(s[len(s)-i-1])-32)):
        test = False
        kq = False
    i +=1
if kq == True:
    print("Xau doi xung")
    for i in range(len(s)):
        print(s[i], end='')
else: 
    print("Xau khong doi xung")
