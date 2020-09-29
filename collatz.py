def hs_even(x): # define function for even number
    seq.append(int(x / 2))
    return x / 2

def hs_uneven(x): # define function for uneven number
    seq.append(int(3 * x + 1))
    return 3 * x + 1

again = "y"

while again == "y": # loop for running multiple sequences
    print("Enter a number to get the Hailstone sequence (Collatz conjecture):")
    x = int(input())

    if x > 0:
        i = 0 # counter for stopping infinite loop after two finishing sequences (4, 2, 1)
        seq = []
        seq.append(x)
        
        while i < 2:
            if x != 1:
                
                if x % 2 == 0:
                    x = hs_even(x) 
                else:
                    x = hs_uneven(x)
        
            else:
                x = hs_uneven(x)
                i += 1
        print(f"Your sequence: {seq} \n Run again? (y/n)")
        again = input().lower()

    else:
        print("Input has to be int and > 0. Run again? (y/n)")
        again = input().lower()

print("Bye!")
