
##########Chapter 1 - Part 1##########
"""An ISP has a packet-switched"""
import math

''' Problem 1 Solution '''

# Change this the total bandwidth for you problem
bandwidth = 140
user_bandwidth = 8.8
max_users = 140 // 8.8
print("Solution 1:")
print(f"- Maximum number of users: {max_users}\n")

''' 
  Problem 2 Solution 
  THIS WILL ONLY GET YOU 6/8 POINTS
'''
# Number of users (CHANGE THIS FOR YOUR PROBLEM)
n = 22

# Probability of a single user accessing the network
# User subscribed for {p} percent of time
p = 0.2

def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def binomial_distribution(n, k, exact=True):
  if exact:
    return binomial_coefficient(n, k) * (p ** k) * ((1 - p) ** (n - k))
  else:
    sum = 0
    for i in range(k, n+1):
      sum += binomial_coefficient(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return sum

# Calculate the probabilities
probability_0_users = round(binomial_distribution(n, 0), 5)
probability_1_user = round(binomial_distribution(n, 1, False), 5)
probability_exactly_1_user = round(binomial_distribution(n, 1), 5)
probability_2_users = round(binomial_distribution(n, 2, False), 5)
probability_exactly_2_users = round(binomial_distribution(n, 2), 5)

# Print the results
print("Solution 2:")
print(f"- Probability that no user is accessing the network: {probability_0_users}")
print(f"- Probability that one particular user is accessing the network: {probability_1_user}")
print(f"- Probability that exactly one user (any one) is accessing the network: {probability_exactly_1_user}")
print(f"- Probability that two particular users are accessing the network: {probability_2_users}")
print(f"- Probability that exactly two users (any two) are accessing the network: {probability_exactly_2_users}\n")

''' Problem 3 Solution '''
# Number of users (CHANGE THIS FOR PROBLEM 3)
n_3 = 70

def binomial_coefficient1(n_3, k):
    return math.factorial(n_3) / (math.factorial(k) * math.factorial(n_3 - k))

def calculate_probability1(N):
    probability = 0
    for k in range(N, n_3 + 1):
        probability += binomial_coefficient1(n_3, k) * (p ** k) * ((1 - p) ** (n_3 - k))
    return round(probability, 5)

# Calculate the probability for at least 18 users accessing the network
N = int(max_users) + 1
probability_at_least_18_users = calculate_probability1(N)

# Print the result
print("Solution 3:")
print(f"- Probability that at least {N} users are accessing the network: {probability_at_least_18_users}\n")

''' Problem 4 Solution '''
low = N
high = n_3
while calculate_probability1(N) > 0.0001:
  n_3 -= 1

print("Solution 4:")
print(f"- Maximum number of users for 99.99% congestion free: {n_3}")