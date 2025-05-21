#REVERSE A GIVEN STRING MANUALLY
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

def main():
    user_input = input("Enter a string: ")
    reversed_string = reverse_string(user_input)
    print(f"The reversed string is: {reversed_string}")

if __name__ == "__main__":
    main()
