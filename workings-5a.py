
input_str = '7,9 -> 9,7'

x1 = int(input_str[0:input_str.find(",")])
y1 = int(input_str[input_str.find(",")+1:input_str.find("->")])
x2 = int(input_str[input_str.find("->")+3:input_str.find(",", input_str.find(",")+1)])
y2 = int(input_str[input_str.find(",", input_str.find(",")+1)+1:])

print(x1, y1, x2, y2)

if x1 < x2:
    x_s = [x for x in range(x1, x2 + 1)]
elif x1 > x2:
    x_s = [x for x in range(x1, x2 - 1, -1)]
if y1 < y2:
    y_s = [y for y in range(y1, y2 + 1)]
elif y1 > y2:
    y_s = [x for x in range(y1, y2 - 1, -1)]
#print(x_s)
#print(y_s)

print(list(zip(x_s, y_s)))
