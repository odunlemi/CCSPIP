# The Towers of Hanoi is an intriguing problem and a classic case of the implementation of recursive algorithms.

# This approach is corroborated by these simple steps to recursive problem-solving; making it exponentially easier;
# Let f(n) be a recursive function;
# 1. Design a solution that works for f called on the input 1; often referred to as the _base case_
# 2. _Assume_ f called on the input (n - 1) works
# 3. Show f(n) works using f(n - 1)

# In this problem there's the simple _base_ case of moving one disc and the recursive case of moving more than one disc between the towers.
# We could break down this recursive case into three(3) steps;
# 1. Move the upper (n - 1) discs from tower A to B (the temporary tower), using tower C as the in-between.
# 2. Move the single lowest, which is also the widest, disc from tower A to C.
# 3. Move the (n - 1) discs from tower B to C, using tower A as the in-between.

# All the steps are equally necessary. You want to get the base case right, and then make sure the other cases work too.

# A function hanoi
hanoi(n, start, end) := pm(start, end)  # pm - print move