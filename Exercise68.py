data=input()
while data!="":
    if len(data)!=8:
        print("Lỗi: Nhập 8 bit")
    else:
        parity=0
        for bit in data:
            parity^=int(bit)
        if parity==0:
            print("Bit chẵn lẻ phải là 0")
        else:
            print("Bit chẵn lẻ phải là 1")
    data=input()