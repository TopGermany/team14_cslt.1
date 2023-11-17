st=input("Nhap van ban can ma hoa: ")
n= int(input("Nhap so ma hoa:" ))
i=1
while i <=len(st):
    if (((ord(st[i-1]) >= 65) and (ord(st[i-1]) <=90)) or ((ord(st[i-1]) >= 97) and (ord(st[i-1]) <=122))):
        kq = ord(st[i-1]) + n
        if (((kq < 65) or ((kq < 97) and (kq > 90))) and (n < 0)):
            kq = kq + 26
        if  ((((kq < 97) and (kq > 90)) or (kq > 122)) and (n > 0)):
            kq = kq - 26
    else: 
        kq = ord(st[i-1])
    print(chr(kq), end="" )
    i = i +1

