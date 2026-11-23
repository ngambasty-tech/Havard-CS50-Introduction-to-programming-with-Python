def main():
    hello("ngam")
    goodbye("Nyah")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


# __name__ is a special python variable with value set by python to be "__main__" when you run a program from the command line.
if __name__ == "__main__":
    main()