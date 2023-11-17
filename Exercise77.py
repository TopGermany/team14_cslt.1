binary_number=input()
if all(digit in '01' for digit in binary_number):
    decimal_number=0
    for bit in binary_number:
        decimal_number=decimal_number*2+int(bit)
    print("Số thập phân tương đương với số nhị phân là:", decimal_number)
else:
    print("Lỗi: Nhập số nhị phân hợp lệ")