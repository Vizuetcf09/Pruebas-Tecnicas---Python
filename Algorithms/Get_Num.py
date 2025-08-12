# Imprime el numero faltante mas pequeño mayor que cero en un arreglo de números

nums = [12, -5, 7, -42, 19, 0, 1, 6, 7, -8, 34, -15, 23, -91, 56, -3, 88, -77, 14, -29, 65, 0, -54, 37, -12, 49, -66, 81]

def get_nums(nums):
    nums = sorted(nums)
    print(nums)

    for n in nums:
        if n >= 0:  
            n += 1
            if n not in nums:
                print(n)
                return n
                
get_nums(nums)
