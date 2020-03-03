from SearchPoint import SearchPoint
import math

print("Введите ширину начальной сетки: ")
net_w = int(input())
x_up_lim = net_w
x_down_lim = 0
print("Введите высоту начальной сетки: ")
net_h = int(input())
y_up_lim = net_h
y_down_lim = 0
print("Введите координату X: ")
srch_x = int(input())
print("Введите координату Y: ")
srch_y = int(input())

SP = SearchPoint(net_w, net_h)
result = SP.where_is_point(srch_x,srch_y)
while result:
    print(str(srch_x)+" "+str(srch_y)+" "+result)
    if result.find("L") >= 0:
        x_up_lim = srch_x
        srch_x = srch_x - math.ceil((srch_x-x_down_lim)/2)
    elif result.find("R") >= 0:
        x_down_lim = srch_x
        srch_x = srch_x + math.ceil((x_up_lim-srch_x)/2)
    if result.find("D") >= 0:
        y_up_lim = srch_y
        srch_y = srch_y - math.ceil((srch_y-y_down_lim)/2)
    elif result.find("U") >= 0:
        y_down_lim = srch_y
        srch_y = srch_y + math.ceil((y_up_lim-srch_y)/2)
    result = SP.where_is_point(srch_x,srch_y)
print("Искомая точка: ("+str(srch_x)+", "+str(srch_y)+")")
