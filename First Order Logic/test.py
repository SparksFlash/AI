from itertools import product

def to_TF(val):
    return "T" if val else "F"

def print_table(headers, rows):
    # Print headers
    print(" | ".join(headers))
    print("-" * (len(headers) * 8))
    # Print rows
    for row in rows:
        print(" | ".join(str(r) for r in row))
    print("\n")

# 1. Modus Ponens
rows = []
for P, Q in product([True, False], repeat=2):
    implies = (not P) or Q
    result = P and implies
    rows.append([to_TF(P), to_TF(Q), to_TF(implies), to_TF(result)])
print("\n--- Modus Ponens ---")
print_table(["P", "Q", "P→Q", "Result(Q)"], rows)

# 2. Modus Tollens
rows = []
for P, Q in product([True, False], repeat=2):
    implies = (not P) or Q
    not_Q = not Q
    result = not P if not_Q and implies else False
    rows.append([to_TF(P), to_TF(Q), to_TF(implies), to_TF(not_Q), to_TF(result)])
print("\n--- Modus Tollens ---")
print_table(["P", "Q", "P→Q", "¬Q", "Result(¬P)"], rows)

# 3. Hypothetical Syllogism
rows = []
for P, Q, R in product([True, False], repeat=3):
    PtoQ = (not P) or Q
    QtoR = (not Q) or R
    PtoR = (not P) or R
    rows.append([to_TF(P), to_TF(Q), to_TF(R), to_TF(PtoQ), to_TF(QtoR), to_TF(PtoR)])
print("\n--- Hypothetical Syllogism ---")
print_table(["P", "Q", "R", "P→Q", "Q→R", "P→R"], rows)

# 4. Disjunctive Syllogism
rows = []
for P, Q in product([True, False], repeat=2):
    P_or_Q = P or Q
    not_P = not P
    result = Q if not_P and P_or_Q else False
    rows.append([to_TF(P), to_TF(Q), to_TF(P_or_Q), to_TF(not_P), to_TF(result)])
print("\n--- Disjunctive Syllogism ---")
print_table(["P", "Q", "P∨Q", "¬P", "Result(Q)"], rows)

# 5. Addition
rows = []
for P, Q in product([True, False], repeat=2):
    rows.append([to_TF(P), to_TF(Q), to_TF(P or Q)])
print("\n--- Addition ---")
print_table(["P", "Q", "P∨Q"], rows)

# 6. Simplification
rows = []
for P, Q in product([True, False], repeat=2):
    P_and_Q = P and Q
    result = P if P_and_Q else False
    rows.append([to_TF(P), to_TF(Q), to_TF(P_and_Q), to_TF(result)])
print("\n--- Simplification ---")
print_table(["P", "Q", "P∧Q", "Result(P)"], rows)

# 7. Resolution
rows = []
for P, Q, R in product([True, False], repeat=3):
    P_or_Q = P or Q
    notP_or_R = (not P) or R
    Q_or_R = Q or R
    rows.append([to_TF(P), to_TF(Q), to_TF(R), to_TF(P_or_Q), to_TF(notP_or_R), to_TF(Q_or_R)])
print("\n--- Resolution ---")
print_table(["P", "Q", "R", "P∨Q", "¬P∨R", "Q∨R"], rows)
