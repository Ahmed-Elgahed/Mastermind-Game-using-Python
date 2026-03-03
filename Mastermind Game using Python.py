import random

num = random.randrange(1000, 10000)
n = int(input("Guess the 4-digit number: "))

if n == num:
    print("Great! You guessed the number in just 1 try! You're a mastermind!")
else:
    ctr = 1
    while n != num:
        ctr += 1
        count = 0
        correct = []

        n_str = str(n)
        num_str = str(num)

        for i in range(4):
            if n_str[i] == num_str[i]:
                count += 1
                correct.append(n_str[i])

        if count == 4:
            break
        elif count != 0:
            print(f"Not quite the number, but you got {count} digit(s) correct!")
            print("Also these numbers in your input were correct:")
            for k in correct:
                print(k, end=" ")
            print("\n")
        else:
            print("None of the numbers in your input match.")

        n = int(input("Enter your next choice of number: "))

    print("You've become a mastermind!")
    print(f"It took you only {ctr} tries!")