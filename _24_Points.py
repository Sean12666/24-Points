import random

while 'y' in input("Play 24 Points? (Y/N)\n").lower():
    a = random.randint(1, 13)
    b = random.randint(1, 13)
    c = random.randint(1, 13)
    d = random.randint(1, 13)
    print("The four numbers are:", a, b, c, d)
    print("You have three tries.")
    times = 0
    flag = True
    while flag and times < 3:
        expr = input("Your expression: ")
        if str(a) in expr and str(b) in expr and str(c) in expr and str(d) in expr and eval(expr) == 24:
            flag = False
        else:
            print("Wrong answer. Please try again.")
        times += 1
    if times < 3:
        print("Great job! You did it!")
    else:
        print("Sorry, no more tries. Try harder next time. (Or maybe it has no solution.)")
    print("")
print("Good bye.")
