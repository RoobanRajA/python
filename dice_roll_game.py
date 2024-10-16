import random;

while True:
    option =input("Roll the dice? (y/n): ").upper();

    if option=='Y':
        a=random.randint(1,6);
        b=random.randint(1,6);
        print(f'({a},{b})');
    elif option=='N':
        print("Thanks for playing!");
        break;
    else:
        print("Invalid choice!");