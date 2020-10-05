list = [i for i in range(20)]
with open('todos.txt', "a") as tasks:
    for chore in list:
        tasks.write(str(chore)+ '/n')