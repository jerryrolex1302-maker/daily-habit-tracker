habits = {}

while True:
    print("\n1. Add Habit\n2. View Habits\n3. Mark Habit Done\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        habit = input("Enter habit name: ")
        habits[habit] = False
        print(f"Habit '{habit}' added!")
    elif choice == "2":
        print("\nYour Habits:")
        for h, done in habits.items():
            status = "Done" if done else "Pending"
            print(f"{h}: {status}")
    elif choice == "3":
        habit = input("Enter habit to mark done: ")
        if habit in habits:
            habits[habit] = True
            print(f"Habit '{habit}' marked as done!")
        else:
            print("Habit not found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice")
