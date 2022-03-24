from todo import Todo
from task import Task

todo = Todo()

while True:
    action = int(input("Do you want to create a task (1) or complete a task(2) or print the list of tasks(3): "))


    if action == 1:
        task_name= input("Input the task name:")
        task_description= input("Input the task description:")

        task= Task(None,task_name, task_description )
        todo.new_task(task)

    if action == 2:
        id_task= input("Input the task id:")       

        todo.complete_task(id_task)

        print("Congratulations, task complete suscefully")
    
    if action == 3:
        print("task    name    description")
        for task in todo.get_tasks():
            print(task.pretty_print())
    
