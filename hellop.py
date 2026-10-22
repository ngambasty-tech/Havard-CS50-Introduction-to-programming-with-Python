# input("what is your name ?")
name = input("what is your name? ").strip().title()
#removing any spaces
# name = name.strip()
# input()

# print("hello, world")
# print("hello " + name)  this is printing one argument - concatinating(+) 
# print("hello,", name) printing 2 arguments "hello, " and name
print("hello, ", end = "") #ovewriting the default end ='\n'
print(name)
first, middle, last = name.split()
print(f'your family name is {first}, \nyour middle name is {middle}, \nand your name is {last}')
# print("hello,", name, end = "uuu")
# print("hello,", name, sep = "yyy")
answer = input("are you a \"nerd\"? ") #handling multiple quotes with back slashes

#format or f string

print(f"hello, {last}")