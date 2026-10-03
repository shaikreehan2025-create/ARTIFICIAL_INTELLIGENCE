import itertools

def solve_cryptarithmetic():
    # Puzzle: SEND + MORE = MONEY
    letters = 'SENDMORY'

    print("Solving Crypt-Arithmetic Puzzle: SEND + MORE = MONEY\n")

    # Generate permutations of digits 0-9 for the 8 unique letters
    for perm in itertools.permutations(range(10), len(letters)):
        s, e, n, d, m, o, r, y = perm

        # Leading letters cannot be zero
        if s == 0 or m == 0:
            continue

        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y

        if send + more == money:
            mapping = {char: digit for char, digit in zip(letters, perm)}
            return mapping, send, more, money

    return None, None, None, None

mapping, send, more, money = solve_cryptarithmetic()

if mapping:
    print("Solution Found!")
    print("Letter Assignments:")
    for letter in sorted(mapping.keys()):
        print(f"  {letter} = {mapping[letter]}")
    print(f"\nArithmetic Verification:")
    print(f"   {send}  (SEND)")
    print(f"+  {more}  (MORE)")
    print(f"---------")
    print(f"  {money}  (MONEY)")
else:
    print("No solution exists.")