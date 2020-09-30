import numpy as np

def hs_even(x): # define function for even number
    seq.append(int(x / 2))
    return x / 2

def hs_uneven(x): # define function for uneven number
    seq.append(int(3 * x + 1))
    return 3 * x + 1

again = "y"

while again == "y": # loop for running multiple sequences
    print("\nEnter a start, stop and step value (all int > 0, ex.: \"2 8 2\") to get the Hailstone sequences (Collatz conjecture):")
    inp = input()

    inp_range = []
    inp_range.append([int(i) for i in inp.split()])

    for num in np.arange(inp_range[0][0],inp_range[0][1],inp_range[0][2]):
        i = 0 # counter for stopping infinite loop after two finishing sequences (4, 2, 1)
        seq = []
        seq.append(num)    
    
        while i < 2:
            if num != 1:
            
                if num % 2 == 0:
                    num = hs_even(num) 
                else:
                    num = hs_uneven(num)
    
            else:
                num = hs_uneven(num)
                i += 1
        print(f"Sequence: {seq}")
    print("\nRun again? (y/n)")
    again = input().lower()

print("Bye!")
