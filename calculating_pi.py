# The mathematically sigf. number pi can be derived using a series of formulas
# One is the Leibniz formula which is implelemented here
# It posits that the convergence of the ff infifnte series is equal to pi
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11 ...

def calcualte_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        # comparing the value of the terms, to match the switching operations of the sequence
        if _ % 2.0 == 0.0:
            pi += operation * (numerator / denominator)
        elif _ % 2.0 != 0.0:
            pi -= operation * (numerator / denominator)
        denominator += 2.0
        operation *= 1.0
    return pi

if __name__ == "__main__":
    print(calcualte_pi(10000000)) # the higher the value of n_terms, the more accurate pi will be calculated 