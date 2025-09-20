# from itertools import product

# def to_TF(val):
#     return "T" if val else "F"

# def print_table(headers, rows):
#     print(" | ".join(headers))
#     print("-" * (len(headers) * 8))
#     for row in rows:
#         print(" | ".join(str(r) for r in row))
#     print("\n")


# rows = []
# for P, Q in product([True, False], repeat=2):
#     implies = (not P) or Q
#     result = P and implies
#     rows.append([to_TF(P), to_TF(Q), to_TF(implies), to_TF(result)])
# print("\n--- Modus Ponens ---")
# print_table(["P", "Q", "P→Q", "Result(Q)"], rows)



from itertools import product

def tf(val):
    if val is None:
        return '-'
    return 'T' if val else 'F'


def modus_ponens():
    print("Modus Ponens Truth Table")
    print(f"{'P':^3} {'Q':^3} {'P→Q':^5} {'Q (MP)':^7}")
    print('-'*22)
    for P, Q in product([True, False], repeat=2):
        implication = (not P) or Q
        result = Q if implication and P else None
        print(f"{tf(P):^3} {tf(Q):^3} {tf(implication):^5} {tf(result):^7}")


modus_ponens()