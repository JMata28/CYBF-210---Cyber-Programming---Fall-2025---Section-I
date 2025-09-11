my_phonebook = {
    "Ross": "1112223333",
    "Ronald": "9990007777",
    "Ryan" : "3334445555"
    }
while(True):
    answer = input("Choose '1' to add a new number. Choose '2' to look up a person in the phonebook.")
    if (answer == "1"):
        key = input("Enter the name of the person: ")
        value = input(f"Enter the number of {key}: ")
        my_phonebook[key] = value
    else: #We are assuming that the answer is either 1 or 2, which is why we're not checking for any other input options
        name = input("Enter the name of the person you're looking for: ")
        if (name in my_phonebook):
            print(f"{name} has the phone number: {my_phonebook[name]}")
        else: 
            print("The name you entered is not in the phonebook. Please try again.")
