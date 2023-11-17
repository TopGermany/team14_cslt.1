x=float(input("Nhập một số: "))
guess=x/2
while True:
    new_guess=(guess+x/guess)/2
    if abs(new_guess * new_guess-x)<=10**-12:
        break
    guess=new_guess
print("Căn bậc hai của",x,"là",guess)
