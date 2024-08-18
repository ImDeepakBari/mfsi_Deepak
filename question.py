# wap to reverse a string using stack 

s = "I am writing this code for jenkins for running .py file in test stage!!"
print("Origninal String :", s)

s_list = s.split(" ")
empty_stack = []

for item in s_list:
    empty_stack.append(item)

reverse_stack = []

while empty_stack:
    reverse_stack.append(empty_stack.pop())
    

print("Reverse of String as :", " ".join(reverse_stack))
        