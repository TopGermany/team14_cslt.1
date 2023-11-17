n = int(input('Số thứ nhất: ')) 
m = int(input('Số thứ hai: '))
d = min(n, m)
if n < 0 or m <0:
    print('Không hợp lệ yêu cầu nhập lại')
while d > 0:
    if n%d == 0 and m%d == 0 :
        print('ước chung lớn nhất','=',d)
        break
    d = d - 1

    
   
    
    
        
    
      