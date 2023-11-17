child_price="14.00"
senior_price="18.00"
adult_price="23.00"
total_cost="0.00"
while True:
    age=input("Nhap tuoi cua khach: ")
    if age=="":
        break
    age=int(age)
    if age<=2:
        admission_cost=0.00
    elif age <= 12:
        admission_cost = child_price
    elif age >= 65:
        admission_cost = senior_price
    else:
        admission_cost = adult_price
    total_cost = admission_cost
print("Chi phi ve vao cua cua nhom: ",total_cost)
