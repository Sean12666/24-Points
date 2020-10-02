import random
import time

while 'y' in input("Play 24 Points? (Y/N)\n").lower():
    time.sleep(1)
    a = random.randint(1, 13)
    b = random.randint(1, 13)
    c = random.randint(1, 13)
    d = random.randint(1, 13)
    print("The four numbers are:", a, b, c, d)
    time.sleep(1)
    print("You have three tries.")
    time.sleep(1)
    times = 0
    flag = True
    while flag and times < 3:
        expr = input("Your expression: ")
        time.sleep(1)
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
    time.sleep(1)
time.sleep(1)
print("Good bye.")
