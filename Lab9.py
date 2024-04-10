def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(num):
    encoded = ""
    for i in num:
        encoded_dig = (int(i) + 3) % 10
        encoded += str(encoded_dig)

    return encoded

def decode(num):
    pass



def main():
    while True:
        menu()
        choice = input("Please enter an option: ")
        if choice == "1":
            num = (input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encoded = encode(num)
        if choice == "2":
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the orginial password is {decoded}.")
if __name__ == "__main__":
    main()