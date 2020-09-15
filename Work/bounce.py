# bounce.py
#
# Exercise 1.5

start_height = 100
reduction_factor = 0.6

for i in range(1, 11):
    print(i, round(start_height * reduction_factor**i, 4))
