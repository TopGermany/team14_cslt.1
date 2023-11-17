from math import sqrt
perimeter=0
first_x_coordinate=float(input("Nhập phần x của tọa độ: "))
first_y_coordinate=float(input("Nhập phần y của tọa độ: "))
previous_x=first_x_coordinate
previous_y=first_y_coordinate
input_line=input("Nhập phần x của tọa độ: (trống để thoát): ")
while input_line!="":
    x=float(input_line)
    y=float(input("Nhập phần y của tọa độ: "))
    distance=sqrt((previous_x-x)**2+(previous_y-y)**2)
    perimeter+=distance
    previous_x=x
    previous_y=y
    input_line=input("Nhập phần x của tọa độ: (trống để thoát): ")
final_distance=sqrt((first_x_coordinate-x)**2+(first_y_coordinate-y)**2)
perimeter+=final_distance
print("The perimeter of that polygon is",perimeter)
