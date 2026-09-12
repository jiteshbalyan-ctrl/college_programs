print("----- MENU -----")
print("1. Burger - Rs 100")
print("2. Pizza - Rs 250")
print("3. Pasta - Rs 150")
print("4. Sandwich - Rs 80")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("You ordered Burger - Rs 100")
elif choice == 2:
    print("You ordered Pizza - Rs 250")
elif choice == 3:
    print("You ordered Pasta - Rs 150")
elif choice == 4:
    print("You ordered Sandwich - Rs 80")
else:
    print("Invalid choice")