from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
statement0 = And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnave, AKnight),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, statement0),
    Implication(AKnave, Not(statement0))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
statement1 = And(AKnave, BKnave)
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnave, AKnight)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, statement1),
    Implication(AKnave, Not(statement1))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
same_kind = Or((And(AKnight,BKnight)), And(AKnave, BKnave))
different_kind = Or((And(AKnight, BKnave)), And(AKnave, BKnight))
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, same_kind),
    Implication(AKnave, Not(same_kind)),
    Implication(BKnight, different_kind),
    Implication(BKnave, Not(different_kind))
    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
Asaid_knight = Symbol("A said 'I am a knight'")
Asaid_knave = Symbol("A said 'I am a knave'")

knowledge3 = And(
    # Identity rules
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A said either "I am a knight" or "I am a knave"
    Or(Asaid_knight, Asaid_knave),
    Not(And(Asaid_knight, Asaid_knave)),
    # A made one of the two statements

    Implication(Asaid_knight, Implication(AKnight, AKnight)),  # redundant but fine
    Implication(Asaid_knight, Implication(AKnave, Not(AKnight))),

    # If A said "I am a knave"
    Implication(Asaid_knave, Implication(AKnight, AKnave)),
    Implication(Asaid_knave, Implication(AKnave, Not(AKnave))),

    # B says A said "I am a knave"
    Implication(BKnight, Asaid_knave),
    Implication(BKnave, Not(Asaid_knave)),

    # B says "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave,  Asaid_knight, Asaid_knave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
