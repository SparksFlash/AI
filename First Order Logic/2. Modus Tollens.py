from itertools import product

def to_TF(val):
    return "T" if val else "F"

def print_table(headers, rows):
    print(" | ".join(headers))
    print("-" * (len(headers) * 8))
    for row in rows:
        print(" | ".join(str(r) for r in row))
    print("\n")



rows = []
for P, Q in product([True, False], repeat=2):
    implies = (not P) or Q
    not_Q = not Q
    result = not P if not_Q and implies else False
    rows.append([to_TF(P), to_TF(Q), to_TF(implies), to_TF(not_Q), to_TF(result)])
print("\n--- Modus Tollens ---")
print_table(["P", "Q", "P→Q", "¬Q", "Result(¬P)"], rows)