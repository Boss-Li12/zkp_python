import random

def get_witness(problem, assignment):
    """
    Division of Two Same Sum - add some ramdom noise
    Given an instance of a partition problem via a list of numbers (the problem) and a list of
    (-1, 1), we say that the assignment satisfies the problem if their dot product is 0.
    check whether problem can be divided into two parts which have the same sum
    """
    sum = 0
    mx = 0
    side_obfuscator = 1 - 2 * random.randint(0, 1)
    witness = [sum]
    assert len(problem) == len(assignment)
    for num, side in zip(problem, assignment):
        assert side == 1 or side == -1
        sum += side * num * side_obfuscator
        witness += [sum]
        mx = max(mx, num)
    # make sure that it is a satisfying assignment
    assert sum == 0
    shift = random.randint(0, mx)
    witness = [x + shift for x in witness]
    return witness

# Commiments
# What we need here is a mechanism that will:
# 1. Force the prover to write down all of the values of p before the verifier asks about them.
# 2. When asked, force the prover to return the required values from this previously written list.
# ps: p -> preSum with randomness