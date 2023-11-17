n = int(input('Số thập phân: '))
ketqua = ''
i = n
while i > 0:
    r = i % 2
    ketqua = str(r) + ketqua
    i = i // 2
print('Số nhị phân là:',ketqua)