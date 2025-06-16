# PYPI.ORG FOR PYTHON PACKAGES
# pretty table - package for creating tables

import random

print("hello world")
# input("whats your age?")
# print("hello" + input("whats your name?"))
print("hello"[0])
print("hello"[-1])
# normally - 1,00,000
# in py - 1_00_000
print(type(123))
print("my age is " + str(12))
round(1.3)
int(-5.9)
score = 8
print(f"your score is = {score}")
print(2 ** 3)
print(5//3)
print(random.randint(1, 3))
print(random.random())
print(random.random() * 10)
print(random.uniform(1, 10))
fruits = ["kiwi", "apple", "peach"]
print(random.choice(fruits))
colors = ["red", "blue", "green"]
print(colors[-1])
colors.append("yellow")
print(colors)
colors.extend(["orange", "black"])
print(colors)
colors.insert(1, "brown")
print(colors)
colors.insert(len(colors), "grey")
print(colors)
colors.remove("red")
print(colors)
colors.pop(2)
print(colors.count("blue"))
print(colors)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
f_list = [list1, list2]
print(f_list)

scores = [10, 11, 17, 20]
sum_of_scores = sum(scores)
max_of_scores = max(scores)
Max = 0
for score in scores:
    if score > Max:
        Max = score
print(Max)

for number in range(1, 10):
    print(number)

# multiline commands
result = 1 + 2 + 3 + \
         4 + 5 + 6
print(result)  # Output: 21

message = """This is a
multiline string."""
print(message)

travel = {
    "france": ["paris", "lille"],
    "germany": ["berlin"]
}
# travel["france"] = 4
print(travel["france"][1])


enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(enemies)
increase_enemies()

if result > 20:
    pass

