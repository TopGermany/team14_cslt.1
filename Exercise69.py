sopi = 3
a = 2
b = 3
c = 4
for i in range(1,16,1):
    sopi = sopi + (4/(a * b * c) - 4/((a + 2) * (b + 2) * (c + 2)))
    a = a + 4
    b = b + 4
    c = c + 4
print('π','≈',sopi)
    
    

    
    
   

    