def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_pairs(numbers):
    lcm_pairs = []
    for i in range(0, len(numbers), 2):
        if i + 1 < len(numbers):
            lcm_pairs.append(lcm(numbers[i], numbers[i + 1]))
    return lcm_pairs

numbers = [2, 7, 3, 9, 4, 6]
print(find_lcm_pairs(numbers))
