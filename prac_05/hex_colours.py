COLOR_HEX_CODES = {"aliceblue": "#f0f8ff","antiquewhite": "#faebd7","aqua": "#00ffff","beige": "#f5f5dc","black": "#000000","blue": "#0000ff","coral": "#ff7f50","crimson": "#dc143c","gold": "#ffd700","hotpink": "#ff69b4"}

def main():
    print("Look up a hex colour code! (Press Enter to quit)")
    while True:
        user_input = input("Enter a colour name: ").strip().lower()
        if user_input == "":
            print("Exiting!")
            break
        code = COLOR_HEX_CODES.get(user_input)
        if code:
            print(f"The hex code for '{user_input}' is {code}.")
        else:
            print("Sorry, that colour is not in the dictionary.")

if __name__ == "__main__":
    main()