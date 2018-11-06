lst = [x for x in range(1,101,1)]
prime_lst =[]

for x in lst:
    
    count = 0
    previous = list(range(2,x,1))

    
    # We are verifying that 'x' is not evenly divisible by any number
    # between 1 and x-1.
    for i in previous:
        
        if (x%i) != 0:
            # Count adds 1 every time 'x' is not evenly divisible by one
            # of the numbers that came before it, i.e., the range 1 to x-1
            count += 1
        else:
            break

    # The for loop above checked to see if 'x' was evenly divisible by
    # any number between 1 to x-1. 'Count' added 1 each time this wasn't true.
    # If (x) mod (every number that came before it) was never 0, then 'x'
    # is prime.
    if count == len(previous) and (x!=1):
        prime_lst.append(x)
    else:
        continue

print(prime_lst)
