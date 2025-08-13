# Escribe una función para filtrar números pares en una lista

import random 

min = 0
max = 50

random_nums = [random.randint(min, max) for n in range(16)] 

def even_nums(nums):
   nums = sorted(nums)
   print(nums)

   for n in nums:
        even_nums = n % 2
        if even_nums == 0:
            print(n)

even_nums(random_nums)