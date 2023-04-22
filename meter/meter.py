def meter():
    metrical_data = input("Enter the metrical data in the form of stressed (/)"
                          "and unstressed (⌣) accents spacing out the feet: ")
    print('\n')

    if len(metrical_data) == 4:
        print("The foot is a dimeter.")

    if len(metrical_data) == 6:
        print("The foot is a trimeter.")

    if len(metrical_data) == 8:
        print("The foot is a tetrameter.")

    if len(metrical_data) == 10:
        print("The foot is a pentameter.")

    if len(metrical_data) == 12:
        print("The foot is a hexameter.")

    if len(metrical_data) > 12:
        print("This foot is a heptameter or above.")

    else:

        "The foot does not have a standard meter length, or you did not enter the correct form of the meter."

    print('\n')

    if metrical_data.startswith("⌣/"):
        print("The meter is iambic.")

    elif metrical_data.startswith("/⌣"):
        print("The meter is trochaic.")

    else:
        print("This foot is neither iambic nor trochaic.")


meter()
