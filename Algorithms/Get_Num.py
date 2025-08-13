# Imprime el numero faltante mas pequeño mayor que cero en un arreglo de números

import random

min = -10
max = 10

random_nums = [random.randint(min, max) for n in range(16)] 

def get_nums(nums):   
    nums = sorted(nums)
    print(nums)

    for n in nums:

        if n >= 0:  
            n += 1
            if n not in nums:
                print(n)
                return n
        elif n != 0:
            n -= (n - 1)
            if n not in nums:
                print(n)
                return n
        
get_nums(random_nums)

