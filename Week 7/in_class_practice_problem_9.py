from collections import deque

q = deque()


while(True):
    answer = int(input("\n\nChoose a number 1-4 to select an option:\n" \
    "1. Add customer to queue.\n" \
    "2. Serve next customer.\n" \
    "3. View current queue.\n" \
    "4. Exit.\n"))
    if answer == 1:
        name = input("Enter the name of the customer that you want to add: ")
        q.append(name)
        print(f"{name} was succesfully added to the queue.")
    elif answer == 2: 
        try:
            satisfied_customer = q.popleft()
        except Exception:
            print("Queue is empty. Can't popleft.")
        else:
            print(f"{satisfied_customer} was served.")
    elif answer == 3:
        print(f"This is the current queue: {q} ")
    elif answer == 4:
        print("Exiting program. Goodbye!")
        break
    else: 
        print("Invalid input.")