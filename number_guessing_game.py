import random;

magicNumber=random.randint(1,100);

while True:
    try:
        number = int(input("Guess the number between 1 and 100: "));
        if number==magicNumber:
            print("Congratulations! You guessed the number.");
            break;
        elif number>magicNumber:
            print("Too high!");
        else:
            print("Too low!");
    except ValueError:
        print("Please enter a valid number");
