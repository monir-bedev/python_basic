### Variable (string type)

str = 'Lovely' # the string can't be change

print(len(str))

print(str[0:4])

print(str[0:-5])
# it means len(str)-5 and the value of this (5-5)=0. 0 index = L

print([*str])
# (*) method split all the char and return list. we also get it using loop

print(str.upper())
print(str.lower())

print(str.capitalize())

new_str = str.replace('Lovely', 'Love is life!!')
print(new_str)
# replace old values with new values

print(new_str.rstrip('!'))
# remove spacial characters

print(new_str.split(' '))
# return list after removing blank spaces

print(new_str.count('L'))
# return how many maching characters


### Variables (number types)

num1 = 10   # integer number
num2 = 20.20 # float number
num3 = '10' # string type number

print(num1, num2, num3)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2) # floor division
print(num1 % num2) # modulus
# but we cann't use num3. but we can use after conver string to intger

print(int(num3) + num2)
print(int(num3) - num2)
#......................

### Complex number types
number = complex(num1, num2)
print(number)

is_present = True
print(is_present) # boolean type

is_absent = False
print(is_absent) # boolean type
