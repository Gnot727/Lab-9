def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(num):
    encoded = ""
    for i in num:
        if int(i) >= 9:
            encoded_dig = (int(i) + 3) - 10
            encoded += str(encoded_dig)
        else:
            encoded_dig = (int(i) + 3)
            encoded += str(encoded_dig)

    return encoded

def decode(num):
    decoded = ""
    print(num)
    for i in num:
        if int(i) <= 2:
            decoded_dig = (int(i) + 7)
            decoded += str(decoded_dig)
            print(decoded_dig)
        else:
            decoded_dig = (int(i) - 3)
            decoded += str(decoded_dig)
            print(decoded_dig)

    return decoded




def main():
    while True:
        menu()
        choice = input("Please enter an option: ")
        if choice == "1":
            num = (input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            encoded = encode(num)
        if choice == "2":
            decoded = decode(num)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
if __name__ == "__main__":
    main()