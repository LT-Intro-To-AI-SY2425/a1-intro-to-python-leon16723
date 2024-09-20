# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num
n = int(input(6))

def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
numbers = [4, 2, 5, 3, 1]
target = 3
result = linear_search(numbers, target)
print("Target found at index:", result) 

def decide(action):
    if action == "walk":
        return "You chose to walk. Enjoy your walk!"
    elif action == "run":
        return "You chose to run. Keep up the pace!"
    elif action == "sit":
        return "You chose to sit. Take a break!"
    else:
        return "Invalid action."

# Example usage
user_action = "run"
decision = decide(user_action)
print(decision)

a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
 
assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

