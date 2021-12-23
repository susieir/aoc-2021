input_str = '657,934 -> 657,926'

x1 = input_str[0:input_str.find(",")]
y1 = input_str[input_str.find(",")+1:input_str.find("->")]
x2 = input_str[input_str.find("->")+3:input_str.find(",", input_str.find(",")+1)]
y2 = input_str[input_str.find(",", input_str.find(",")+1)+1:]

print(x1, y1, x2, y2)