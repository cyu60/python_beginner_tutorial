# v3 final

# Declare constants
todo_title = 'Welcome to our TODO APP!'
todos = ['wash the dishes', 'finish homework', 'go for a run']

todo_options = """
Please select an option:
1 - Add a todo
2 - Delete a todo
3 - Change a todo
4 - quit
"""
# Used for clarity and better asthetics
line_sperator = '--------------------------------'

# Define the functions
def check_index_within_bounds(user_index, todo_list):
    true_or_false = False
    if user_index is not None:  # need to check that it is not none
        true_or_false = len(todo_list) > user_index >= 0
    # Note: we can return the statement above directly, I am just assinging it to a var for clarity
    return true_or_false

def get_user_index(todo_list):
    user_index = None
    while (user_index is None or check_index_within_bounds(user_index, todo_list) is False):
        try:
            user_index = int(input("Enter the index to change todo: "))
        except Exception as e:  # if there is an error execute this code
            print('Please enter an integer index from the list of todos')
    return user_index

def print_todos(todos_list: list) -> None:
    print('List of Todos:')
    for index, todo in enumerate(todos_list):
        print(index, " - ", todo)

def add_todo(todos_list):
    user_input = input("Enter a new todo: ")
    todos_list.insert(0, user_input)

# We need to change the parameters for the get_user_index!
def delete_todo(todos_list):
    user_index = get_user_index(todos_list)
    todos_list.pop(user_index)

def change_todo(todos_list):
    user_index = get_user_index(todos_list)
    new_todo = input("Enter a modified todo: ")
    todos_list[user_index] = new_todo
    
def execute_user_input(user_input, todos_list):
    if (user_input == '1'):
        add_todo(todos_list)
    elif (user_input == '2'):
        delete_todo(todos_list)
    elif (user_input == '3'):
        change_todo(todos_list)
    elif (user_input == '4'):
        print("Bye!")
    print(line_sperator)  # To make things a bit clearer between different options


# Note this special decorator --- we only run the program if it is ran from main!
if __name__ == "__main__":    
    
    print(todo_title)

    user_input = None
    
    while (user_input != '4'):
        print_todos(todos)
        print(todo_options)
        user_input = input("Enter option: ")
        execute_user_input(user_input, todos)
