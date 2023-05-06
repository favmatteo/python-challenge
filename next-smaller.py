from itertools import permutations

def next_smaller(n: int):
    num_str = str(n)
    res = set()
    for i in permutations(num_str, len(num_str)):
        if "".join(i)[0] != '0': 
            res.add(int("".join(i)))


    before = 0
    for num in res:
        if num > before and num < n:
            before = num
    
    return before if before > 0 else -1

print(next_smaller(907))

# 9 0 7

# 0 9 7
# 0 7 9

# 0 7 9
# 7 0 9

# 7 9 0
# 7 0 9

# 9 0 7
# 9 7 0


# 