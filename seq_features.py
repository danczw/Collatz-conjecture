# features engineering for hailstone sequence length prediction
import pandas as pd
import numpy as np

collatz_df = pd.DataFrame()

def hailstone_sequence(n): # create hailstone sequence
    seq = [n]
    while n != 1:
        parity = int(n % 2)
        # Odd step
        if parity:
            n = (3 * n + 1) 
        # Even step
        else:
            n /= 2
        seq.append(int(n))
    return seq

def count_even(list): # count amount of even numbers in a list
    counter = 0
    for num in list:
        if num % 2 == 0:
            counter += 1
    return counter

def count_uneven(list): # count amount of uneven numbers in a list
    counter = 0
    for num in list:
        if num % 2 != 0:
            counter += 1
    return counter

def primes(list): # create list of primes from a list
    primes = []
    for num in list:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
        else:
            pass
    return primes


# input numbers (sequence starting numbers) TODO: adjust range below
start = 1 # define start of range for input number n / caution: do not start with 0
stop = 100000 # define stop of range for input number n
step = 1 # define step of range for input number n

n = np.arange(start, stop, step)
collatz_df['n'] = n
print('1/10 - n done!')

# add column with sequence for each n
collatz_df['seq'] = [hailstone_sequence(i) for i in collatz_df['n']]
print('2/10 - seq done!')

# add column with len of each sequence
collatz_df['seq_len'] = [len(i) for i in collatz_df['seq']]
print('3/10 - seq_len done!')

# add column with is even of each n
collatz_df['is_even'] = [1 if i % 2 == 0 else 0 for i in collatz_df['n']]
print('4/10 - is_even done!')

# count even and uneven sequence values
collatz_df['amount_even'] = [count_even(i) for i in collatz_df['seq']]
print('5/10 - amount_even done!')
collatz_df['amount_uneven'] = [count_uneven(i) for i in collatz_df['seq']]
print('6/10 - amount_uneven done!')

# prime numbers in sequence
collatz_df['primes'] = [primes(i) for i in collatz_df['seq']]
print('7/10 - primes done!')

# count prime numbers in sequence
collatz_df['amount_prime'] = [len(i) for i in collatz_df['seq']]
print('8/10 - amount_prime done!')

# max prime number in sequence
collatz_df['max_prime'] = [max(i) for i in collatz_df['seq']]
print('9/10 - max_prime done!')

# min prime number in sequence
collatz_df['min_prime'] = [int(sorted(i[0:1])[0]) if len(i) > 1 else None for i in collatz_df['primes']]
print('10/10 - min_prime done!')

print(collatz_df.head(5))
collatz_df.to_csv("collatz_features.csv", sep=";")
