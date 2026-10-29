def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what is x ? ")) #passing a str here will fail and so the x vallue getes no nothing assigned to it since it expects an int
            
        except ValueError:
            pass
            # print("x is not an integer")
        # else: #executed omly when the try is successful
            # return x

main()