prices=[4.95, 9.95, 14.95, 19.95, 24.95]
i=0
while True:
    if i==len(prices):
        break
    price=prices[i]
    discount=price*0.6
    new_price=price-discount
    print("Giá Gốc:$",round(price,2))
    print("Số Tiền Giảm Giá:$",round(discount,2))
    print("Giá Mới:$",round(new_price,2))
    print()
    i+=1
