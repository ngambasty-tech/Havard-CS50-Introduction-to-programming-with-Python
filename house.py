name = input("what is yiur name? ")

match name:
    case "Sabastine" | "Juliet" | "Queen" | "Conscience":
        print("Nyah")
    case "Emmanuel" | "Liberty" | "Guilbert":
        print("Ngam")
    case _:
        print("Who...? ")