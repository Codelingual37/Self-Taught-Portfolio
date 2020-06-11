numbers = [37, 77, 21, 28, 20, 8]
print("Guess a number from the list or")

while True:
    try:
        print("type 'q' to quit.")
        ans = input()
        if ans == 'q':
            print("Okay, maybe some other time.")
            break
        else:
            ans = int(ans)
        if ans in numbers:
            print("You got one!")
            break
        else:
            print("Please try again or")
    except:
        print("Please type an integer or")
