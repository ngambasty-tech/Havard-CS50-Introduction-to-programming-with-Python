# x = 3
# y = 6
# z = x + y
# print(z)

#nesting functions( int fxn and input fxn)
'''
x = int(input('what is x? ')) # inner function gets called first
y = int(input('what is y? ')) # input fxn 1st before int
u = float(input('enter the u value: '))
z = x + y
f = round(x + u)
print(f)
print(f'{f:,}')
print(f'{f:.3f}')

print (z)
'''

# x = input('what is x? ')
# y = input('what is y? ')
# print(x + y) #without the str conversion to int

def main():
     number = int(input(" what is you digit? "))
     squared =  square(number)
     print(squared)

def square(x):
     return pow(x, 2)  # x*x, x **2

main()