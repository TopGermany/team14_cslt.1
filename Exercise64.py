total_cost = 0

while True:
    prices = []
    while True:
        price = input("Nhập giá (hoặc để trống để hoàn thành): ")
        if price == "":
            break
        prices.append(float(price))
    
    if not prices:
        break

    total_cost += sum(prices)

cash_payment = total_cost

remainder = cash_payment % 5
if remainder < 2.5:
    cash_payment -= remainder
else:
    cash_payment += (5 - remainder)

print("Tổng chi phí: $", total_cost)
print("Số tiền phải trả khi thanh toán bằng tiền mặt: $", cash_payment)