# Part C
# -----1-----
names = ["Karim", "Klaus", "Klara", "Kelvin", "Klaudia"]

for index, name in enumerate(names):
    print(f"[{index + 1}] Hello, {name}")

# -----2-----
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 230,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
]

for num in numbers:
    if num % 2 == 0:
        print(num)
      
# -----3-----
nums = [8, 4, 17, 12, 3, 24, 9]
nums_sum = 0

for num in nums:
    nums_sum += num

print(nums_sum)

# -----4-----
nums = [8, 4, 17, 12, 3, 24, 9]
maximum = nums[0] 

for num in nums:
    if num > maximum:
        maximum = num

print(maximum)

# -----5-----
words = ["Glossary", "Spitbug", "Snot", "Jam", "Acceleration", "Critical", "Blizzard", "Spike"]

count = 0
for word in words:
    if len(word) > 5:
        count += 1

print(count)

# -----6-----
scores = [35, 90, 95, 70, 69, 0, 75]
passes = 0 
failures = 0

for score in scores:
    if score >= 70:
        passes += 1
    else:
        failures += 1

print(f"no. passes: {passes}, no. failures: {failures}")

# -----7-----
people = {"kyla" : 38,
          "olof" : 22,
          "drake" : 39}

#1: Key
for k in people.keys():
    print(k)

#2: Value
for v in people.values():
    print(v)

#3: Item
for i in people.items():
    print(i)