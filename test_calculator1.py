from calculator1 import square


def main():
    test_square()

def test_square():
    try:
        assert square(4) == 16
    except AssertionError:
        print("test failed")
    try:
        assert square(5) == 25
    except AssertionError:
        print("test failed again")
    # if square(4) != 16:
    #     print("there is an issue with code, 4 square was not 16")
    # if square(5) != 25:
    #     print("there is an issue with code, try verifying")



if __name__ == "__main__":
    main()