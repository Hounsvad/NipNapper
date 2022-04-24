nipperColors = ['green', 'red', 'blue', 'yellow']
nipperInside = {
    1: 'Use recursion at least once in you next project',
    2: 'Use comic sans as your vscode font for an entire day',
    3: 'Use vim as your editor for an entire day',
    4: 'You can use your mouse for an entire day',
    5: 'Switch to a random keyboard layout for a day',
    6: 'Go out and touch grass',
    7: 'Switch your entire system to light mode for a day',
    8: 'Switch to a dvorak layout for a day'
}


def flip_flap():
    color = "NotTheRightColor"
    while color not in nipperColors:
        color = input("Please select a color (" +
                      ",".join(map(lambda color_option: color_option.capitalize(), nipperColors)) +
                      "): ").lower()
        if color not in nipperColors:
            print("The selected color is not available")
    for i in range(0, len(color)):
        if i % 2 == 0:
            print("flip")
        else:
            print("flap")

    available_numbers = []

    if len(color) % 2 == 0:
        available_numbers = [3, 4, 7, 8]
    else:
        available_numbers = [1, 2, 5, 6]

    selected_number = -1
    while selected_number not in available_numbers:
        selected_number = input("Please select a number (" + ",".join(map(str, available_numbers)) + "): ")
        if selected_number.isnumeric():
            selected_number = int(selected_number)
        else:
            print("The given value was not a number")
            continue
        if selected_number not in available_numbers:  # Possible Issue with selected number not being an int
            print("That was not a number that you could chose")
    print("You got: " + str(selected_number) + ". " + nipperInside[selected_number])


if __name__ == '__main__':
    yesResponses = ['yes', 'y', 'yup', 'sure']
    noResponses = ['no', 'n', 'nope', 'never']
    run = True
    while run:
        flip_flap()
        response = input("Would you like to play again (y/N): ").lower()
        if response in yesResponses:
            print("Sure thing, another game it is then")
        elif response in noResponses:
            print("Ok, that's it for now i suppose")
            run = False
        else:
            print("Hmm, that seems unrelated, about as unrelated as aglet i suppose, so well take that as a no then.")
            run = False
