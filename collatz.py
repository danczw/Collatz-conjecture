def hs_even(x):
    y.append(int(x / 2))
    return x / 2

def hs_uneven(x):
    y.append(int(3 * x + 1))
    return 3 * x + 1

again = "y"

while again == "y":
    print("Enter a number to get it Hailstone sequence:")
    x = int(input())

    if x > 0:
        i = 0
        y = []
        y.append(x)
        
        while i < 2:
            if x != 1:
                
                if x % 2 == 0:
                    x = hs_even(x) 
                else:
                    x = hs_uneven(x)
        
            else:
                x = hs_uneven(x)
                i += 1
        print(f"Your sequence: {y} \n Run again? (y/n)")
        again = input().lower()

    else:
        print("Input has to be int and > 0. Run again? (y/n)")
        again = input().lower()

print("Bye!")
