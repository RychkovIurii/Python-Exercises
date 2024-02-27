# While Loop
count = 0

while count < 5:
    print(count)
    count += 1
"""
While Loop: Repeats a block of code as long as the specified condition is true.
In this example, the loop continues as long as the variable count is less than 5.
The print statement inside the loop displays the current value of count.
The count += 1 statement increments the value of count in each iteration, preventing an infinite loop.
"""
# For Loop going through a list
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)

"""
For Loop: Iterates over a sequence (e.g., a list) and executes a block of code for each element.
In this example, the loop iterates through each element (fruit) in the fruits list.
The print statement inside the loop displays each fruit.
"""

# For Loop with range()
for i in range(0, 10, 1):
    print("Index:", i)

"""
For Loop with range(): Creates a loop that iterates over a sequence of numbers.
range(0, 10, 1) generates numbers starting from 0 (inclusive) up to 10 (exclusive), with a step of 1.
In each iteration, the loop variable i takes on the values produced by range().
The print("Index:", i) statement inside the loop displays the current value of i in each iteration.
It's worth noting that the range(0, 10, 1) can be simplified to range(10) because the start value is 0 by default,
and the step value is 1 by default. So, range(10) produces the same sequence of numbers from 0 to 9.

Not: Reverses the result of a condition.
And: Returns True if both conditions are true.
Or: Returns True if at least one condition is true.
"""

# And if we have a loop that we want to get out of we use "Break"
while True:
    print("This will only run once!")
    break # Break will exit the loop
