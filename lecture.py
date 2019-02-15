import numpy
import matplotlib.pyplot as plt

def read1():
    file = open("a_example.in", "r")
    lines = file.readlines()
    mappedLines = list(map(lambda line: line.replace("\n", ""), lines))
    print(mappedLines)
    return mappedLines

def read2():
    file = open("a_example.in", "r")
    lines = file.read().split("\n")[:-1]
    return lines

def ingredientToColor(ingredient):
    return 1 if ingredient == "T" else 0

def ingredientsToColor(ingredients):
    return list(map(ingredientToColor, ingredients))

def arrayToColor(array):
    return list(map(ingredientsToColor, array))


lines = read2()
print(lines)
coloredLines = arrayToColor(lines[1:])
fig, ax = plt.subplots()
ax.grid(True)
ax.imshow(coloredLines)
plt.show()