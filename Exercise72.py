n1 = input('Nhập chữ cái palindrome: ')
n2 = ''
for i in range(len(n1)-1,-1,-1):
    n2 = n2 + n1[i] 
if n1 == n2:
    print('Là palindrome')
else:
    print('không phải là palindrome')