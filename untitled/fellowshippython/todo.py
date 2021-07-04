import sys
from datetime import date

class MyException(Exception):
    message=''

    def __init__(self,message="MyException Occurred"):
        self.message=message
        super().__init__(self.message)

    def getMessage(self):
        return self.message

    def __str__(self):
        return (repr('MyException Occurred'))

def lsTask():
    with open('todo.txt','r') as file:
        todos=file.readlines()
        for todo in todos:
            print(f"{todos.index(todo)} {todo}",end='')

def addTask(task):
    with open('todo.txt','a') as file:
        file.write(task+"\n")
        print(f"Added todo: {task}")

def deleteTask(no):
    try:
        with open('todo.txt','r') as file:
            todos=file.readlines()
            if len(todos)<=no:
                raise MyException(f"Error: todo # {no} does not exist. Nothing deleted.")
            del todos[no]

        with open('todo.txt','w+') as file:
            file.writelines(todos)
            print(f"Deleted todo: {no}")

    except MyException as e:
        print(e.getMessage())

def doneTask(no):
    try:
        with open('todo.txt','r') as file:
            todos=file.readlines()
            if len(todos)<=no:
                raise MyException(f"Error: todo # {no} does not exist.")
            task=todos[no]
            del todos[no]

        with open('todo.txt','w+') as file:
            file.writelines(todos)

        with open('done.txt', 'w')as file:
            file.write(f'x {date.today().strftime("%Y/%m/%d")} {task}')
            print(f"Marked todo #{no} as done.")

    except MyException as e:
        print(e.getMessage())

args=sys.argv[1:]
if(args[0].lower()=="add"):
    try:
        if len(args)<2:
            raise MyException("Error : task not mentioned ")
        addTask(args[1])
    except MyException as e:
        print(e.getMessage())
elif (args[0].lower()=="done"):
    try:
        if len(args)<2:
            raise MyException("Error : task no not mentioned ")
        doneTask(int(args[1]))
    except MyException as e:
        print(e.getMessage())
elif(args[0].lower()=="delete"):
        try:
            if len(args)<2:
                raise MyException("Error : task no not mentioned ")
            deleteTask(int(args[1]))
        except MyException as e:
            print(e.getMessage())
elif(args[0].lower()=="ls"):
        lsTask()
else:
    print('end')
