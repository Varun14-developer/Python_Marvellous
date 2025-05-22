def main():

    print("Enter a letter : ")
    letter = input()

    if letter in "aeiou":
        print(letter, "is a vowel")

    else:
        print("It's a consonant")


if __name__ == "__main__":
    main()