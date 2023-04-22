def accent_checker():

    # First allowing user input

    print("Hello, please input the word which you would like to check if it is accented or not.")
    user_input_word = input("Please enter the word which you would like to check whether it is accented or not: ")

    if 'à' or 'è' 'ì' 'ò' or 'ù' or 'À' or 'È' or 'Ì' or 'Ò' or 'Ù' in user_input_word:
        print('\n')
        print("The word contains an acute accent ")
    elif 'â' or 'ê' or 'î' or 'ô' or 'û' or 'Â' or 'Ê' or 'Î' or 'Ô' or 'Û' in user_input_word:
        print('\n')
        print("The word contains a circumflex accent ")

    else:
        print("The word is unaccented.")


accent_checker()
