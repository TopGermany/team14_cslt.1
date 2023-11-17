count=0
total=0
while True:
    number=int(input("Nhap mot so: "))
    if number==0:
        break
    if count==0:
        if number==0:
            print("Loi: Khong the tinh trung binh cua tap hop rong")
            break
    count=1
    total=number
average=total / count
print("Trung binh la",average)
