# i = 3

# while i != 0:
#     print("meow")
#     i -= 1


# for _ in  range(3):
#     print("meow")

'''
while True:
    n = int(input("what is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    number = get_number()
    wouff(number)


def get_number():
    while True:
        n = int(input("what is the numbere?"  ))
        if n > 0:
            break
    return n

def wouff(n):
    for _ in range(n):
        print("wouff")

main()