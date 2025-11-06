class Task:
    def __init__(self, description, next_task=None):
        self.description = description
        self.next_task = next_task
    
class ToDoList:
    def __init__(self, first_task):
        self.first_task = first_task
    
    def addTask(self, new_task):
        curr = self.first_task
        while(curr): #Go until the last task in the list
            if curr.next_task == None:
                break
            curr = curr.next_task
        curr.next_task = new_task
        return self.first_task
    
    def showTasks(self):
        curr = self.first_task
        list_of_tasks = []
        while(curr): 
            list_of_tasks.append(str(curr.description))
            curr = curr.next_task
        print(' -> '.join(list_of_tasks))

    def deleteTask(self, description):

        curr = self.first_task

        # Edge case: list is empty
        if curr is None:
            print("The list is empty!")
            return None

        # Edge case: deleting the head node
        if curr.description == description:
            self.first_task = curr.next_task
            print(f"{description} Task was removed from the list!")
            return self.first_task

        # Traverse the list
        while curr.next_task:
            if curr.next_task.description == description:
                curr.next_task = curr.next_task.next_task
                print(f"{description} Task was removed from the list!")
                return self.first_task
            curr = curr.next_task
            
        print(f"{description} Task is not on the list so it can't be removed!")
        return self.first_task

A = Task("Buy laundry detergent.")
B = Task("Buy laundry softener.")
C = Task("Do laundry.")

monday_list = ToDoList(A)
new_first_task = monday_list.addTask(B)
new_first_task = monday_list.addTask(C)
monday_list.showTasks()

monday_list.deleteTask("Buy soap.")
monday_list.deleteTask("Buy laundry softener.")