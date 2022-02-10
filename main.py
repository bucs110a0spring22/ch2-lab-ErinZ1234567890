import random

#Part A
weeks = 16
print("variable weeks:", weeks, type(weeks))
classes = 5
print("variable classes:", classes, type(classes))
tuition = 6000
print(tuition, type(tuition))
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classesPerWeek = 2
print("variable classesPerWeek", classesPerWeek, type(classesPerWeek))
costPerClass = cost_per_week / float(classesPerWeek)
print("Cost per class:", costPerClass)

#Part B
myList = ["strong", 100, "big", 0.5, 'l']
randList = random.choice(myList)
print(randList)