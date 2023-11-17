n=int(input("Nhap gia tri: "))
if n < 2:
    print("Loi, vui long nhap lai gia tri khac")
else:
    print("ket qua: ")
    while n != 1:
        test = True
        i = 2
        while test == True:
            if n % i == 0:
                test = False
            i += 1
        i = i - 1
        print(i)
        n = n / i
