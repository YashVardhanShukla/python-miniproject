def forward_representation(number):
    return str(number)

def backward_representation(number):
    return str(number)[::-1]

def horizontal_representation(number):
    num_str = str(number)
    horizontal = ""
    for digit in num_str:
        horizontal += f"{digit} "
    return horizontal.strip()

def vertical_representation(number):
    num_str = str(number)
    vertical = ""
    for digit in num_str:
        vertical += f"{digit}\n"
    return vertical.strip()

def main():
    number = int(input("Enter a number: "))
    
    print("Forward Representation:", forward_representation(number))
    print("Backward Representation:", backward_representation(number))
    print("Horizontal Representation:", horizontal_representation(number))
    print("Vertical Representation:\n", vertical_representation(number))

if __name__ == "__main__":
    main()
