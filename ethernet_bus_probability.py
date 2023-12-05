import math

Nodes = 19
Attempts = 10
Number_Prob = 3

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

Combinations = nCr(Nodes,Number_Prob)
Probability_of_Picking_Zero = (1/(2**Attempts))**Number_Prob
Probability_of_Rest = (1-(1/(2**Attempts)))**(Nodes-Number_Prob)
Answer = Combinations * Probability_of_Picking_Zero * Probability_of_Rest

print(Answer)
#If it prints out something e-, then it is in scientific notation. and the answer is 0.000