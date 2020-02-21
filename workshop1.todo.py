class Todo:
    def __init__(self, name, description, points, complete = False):
        self.name = name
        self.description = description
        self.points = points
        self.complete = complete

class TodoList:
    def __init__(self, todo_list):
        self.todo_list = todo_list
    
    def sum_of_points(self):
        result = 0
        for todo in self.todo_list:
            result += todo.points
        return result
    def number_of_todos(self):
        return len(self.todo_list)

    def average_points(self):
        return self.sum_of_points() / self.number_of_todos()
    
    def completed(self):
        result = []
        for todo in self.todo_list:
            if todo.complete:
                result.append(todo)
        return result
    def incomplete(self):
        result = []
        for todo in self.todo_list:
            if not todo.complete:
                result.append(todo)
        return result
