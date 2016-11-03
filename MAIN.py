# Scheduling-Algorithms
#MAIN
#The main part that the user will interact with
import random
Tasks = [0,0,0,0,0]
def TaskFill(T, l, u):
    for i in range(0,len(T)):
        T[i] = random.randint(l,u)
TaskFill(Tasks, 0, 10)

def Task(n, i, l):
    while l >0:
        if i != 0:
            print("Task %s has %s runs remaining" %(n, i))
            Tasks[n-1] -= 1
        l -= 1

print(Tasks)

for i in range(1, len(Tasks)+1):
    Task(i, Task[i], Task[i])
