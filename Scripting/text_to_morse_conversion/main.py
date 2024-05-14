from text_to_morse_data import *

def main():
    programme_active = True

    def get_morse(word):
        encoded_letters = []
        previous_letter = None
        for character in word:
            if character == ' ':
                # If there is a space between Words in our string we add a 'Major space' then break from current iteration
                encoded_letters.append(MAJOR_SPACE)
                previous_letter = MAJOR_SPACE
                continue

            for k, v in MORSE.items():
                if character in k:
                    if character == previous_letter:
                        # if character is the same as previous letter add twin space then new letter
                        encoded_letters.append(TWIN_SPACE)
                        encoded_letters.append(v)
                        continue
                    # After we've got the correct character we add 'minor space' after
                    if len(encoded_letters) == 0:
                        # if this is the 1st iteration don't put a space
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
                    elif previous_letter == MAJOR_SPACE:
                        # If the last letter was a major space don't put a minor space
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
                    else:
                        # if it's not the first iteration. if the previous letter is not the same, if the current
                        # letter is not a space, if the previous letter is not a major space
                        encoded_letters.append(MINOR_SPACE)
                        encoded_letters.append(v)
                        previous_letter = character
                        continue
        return encoded_letters

    def output(code):
        empty_string = ''
        return empty_string.join(encoded_message)

    def user_input():
        response = str(input('Please provide a String to convert?\n'))
        return response

    def exit_input():
        response = input('Would you like to encode another message?\nType (Y/N)\n').lower()
        return response

    print(WELCOME_MESSAGE)
    print('Welcome to Morse Code Encoder !! ')

    while programme_active:

        user_response = user_input()
        # Converter functionality
        encoded_message = get_morse(user_response)
        # Output Morse Code
        morse_code_message = output(encoded_message)
        print(morse_code_message)

        # Program Exit
        valid_response = False
        while not valid_response:
            exit_response = exit_input()

            if exit_response == 'n':
                programme_active = False
                valid_response = True
                print('Thank you for using Morse Code Converter')
                print(GOODBYE_MESSAGE)
                break

            elif exit_response == 'y':
                valid_response = True
                break
            else:
                continue


if __name__ == '__main__':
    main()