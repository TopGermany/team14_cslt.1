import random
so = random.randint(1,100)
print(so)
max = so
i = 1
dem = 0
while i <= 99:
    so = random.randint(1,100)
    if max >= so:
        print(so)
    else:
        print(so ," <== update")
        max = so
        dem = dem + 1
    i += 1
print("So lon nhat la: ", max)
print("So lon nhat duoc cap nhat ", dem , " lan")
