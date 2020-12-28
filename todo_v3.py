# v3

# So far, we have been practicing LINEAR PROGRAMMING
# This is what our app looks like so far... it works, but it seems very messy
# It is what so would call spagetti code, it is diffult to manage, and there is a lot of room for error

# Declare constants
todo_title = 'Welcome to our TODO APP!'
print(todo_title)
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

# #-----------------------------------------------------------------------------------------------

# # Get user input --- this is the really confusing part!
# user_input = None  # Start off with some arbitary number that is not 4, or None
# while (user_input != '4'):  # The ! means not (negation)
#     # Print out all the options --- use the for loop from above
#     print('List of Todos:')
#     for index, todo in enumerate(todos):
#         print(index, " - ", todo)
#     print(line_sperator)
#     # Combine from the solution from above!
#     print(todo_options)
#     user_input = input("Enter option: ")
#     if (user_input == '1'):
#         # Add a new todo ------ from v1
#         user_input = input("Enter a new todo: ")
#         todos.insert(0, user_input)
#     elif (user_input == '2'):
#         # Delete a todo ------ from v1
#         user_input = int(input("Enter the index to remove todo: "))
#         todos.pop(user_input)
#     elif (user_input == '3'):
#         # Change a todo ------ from v1
#         user_index = int(input("Enter the index to change todo: "))
#         new_todo = input("Enter a modified todo: ")
#         todos[user_index] = new_todo
#     elif (user_input == '4'):
#         print("Bye!")
#     print(line_sperator)  # To make things a bit clearer between different options
    
# # Instead, lets start to break it apart into more smaller bits of code!
# # Advantages of factoring into modular code -- Functional Programming
# # - You can resue it in many places
# # - You don't have to change all occurances of it, easier to manage errors
# # - You can make your code shorter and more concise more easily

# # This is what a function looks like, it is kind of like maths!
# def funcname(parameter_list):
#     """
#     docstring
#     """
#     pass # This is what it does

# # For example, this function print all the todos
# def print_todos(todos_list: list) -> None: # We can specify the type of arg and return type for clarity, it's good practice, though uneccessary at this stage
#     print('List of Todos:')
#     for index, todo in enumerate(todos_list):
#         print(index, " - ", todo)    

# print_todos(todos_list=todos) # We can call it this way!

# # Let's create functions for the first 3 user options above!

# def add_todo(todos_list):
#     user_input = input("Enter a new todo: ")
#     todos_list.insert(0, user_input)

# # You can pass in any variable that is the correct for of argument (List)
# # print_todos(5) # This would lead to an error as it is not a list!
# test_todo = []
# add_todo(todos_list=test_todo) # We can specify which argument we are passing in the variable for though it is usually uneccessary unless we have a lot of arguments 
# print_todos(test_todo)

# # Try and figure out the rest on your own! Call the function and use print todos to check if you are correct

# ### -------------------------------------- SOLUTION --------------------------------------------

# def delete_todo(todos_list):
#     # Delete a todo ------ from v1
#     user_index = int(input("Enter the index to remove todo: "))
#     todos_list.pop(user_index)
    
# def change_todo(todos_list):
#     # Change a todo ------ from v1
#     user_index = int(input("Enter the index to change todo: "))
#     new_todo = input("Enter a modified todo: ")
#     todos_list[user_index] = new_todo
    
# #-----------------------------------------------------------------------------------------------

# # Note: we can combine functions in other functions!

# def execute_user_input(user_input, todos_list): # We can pass muplitpule parameters into the argument
#     if (user_input == '1'):
#         add_todo(todos_list)
#     elif (user_input == '2'):
#         delete_todo(todos_list)
#     elif (user_input == '3'):
#         change_todo(todos_list)
#     elif (user_input == '4'):
#         print("Bye!")
#     print(line_sperator)  # To make things a bit clearer between different options
    

# # Now, our while loop can look a lot cleaner!
# user_input = None
# while (user_input != '4'):
#     print_todos(todos)    
#     print(todo_options)
#     user_input = input("Enter option: ")
#     execute_user_input(user_input, todos)
    
# # This process of pulling out code into seperate parts is called refactoring and is a great coding practice!

#-----------------------------------------------------------------------------------------------

# # Note: Scopes --- a funky behavior
# # When we call a function, if it creates variables within the function, it is not shown throughout the program
# # This is good because it does not cause "side effects", and hides uneccessary details, but can be a bit confusing

# # Lets see some exmples
# # print(todos_list) # gives an error as while we have used todo_list, we have never declared it globally

# user_index = 0
# def get_user_index_not_working(): # We can choose to pass no arguments
#     # If you see a squiggly underscore, then there is usually an issue!
#     user_index = int(input("Enter the index to change todo: "))
# get_user_index_not_working()
# print(user_index) # Why is this still 0?

# # We can use a return statement if we want to pass the variable on

# user_index = 0
# def get_user_index():  # We can choose to pass no arguments
#     user_index = int(input("Enter the index to change todo: "))
#     return user_index


# # Now, we can reassign the variable based on the returning function!
# user_index = get_user_index()
# print(user_index)

# # Lets refactor the code from above!

# def delete_todo(todos_list):
#     # Delete a todo ------ from v1
#     user_index = get_user_index()
#     todos_list.pop(user_index)
    
# def change_todo(todos_list):
#     # Change a todo ------ from v1
#     user_index = get_user_index()
#     new_todo = input("Enter a modified todo: ")
#     todos_list[user_index] = new_todo
    
#-----------------------------------------------------------------------------------------------
 
# Error handling 

# Remember the type issue that we had in v3? We are going to fix it now!
# What happens when the user enters an index that has not been listed?

def check_index_within_bounds(user_index, todo_list):
    true_or_false = False
    if user_index is not None: # need to check that it is not none
        true_or_false = len(todo_list) > user_index >= 0
    return true_or_false # Note: we can return the statement above directly, I am just assinging it to a var for clarity

# Test it! -- try and use edge cases
# False cases
print(check_index_within_bounds(3, todos))
print(check_index_within_bounds(-1, todos))
print(check_index_within_bounds(None, todos))

# True cases
print(check_index_within_bounds(0, todos))
print(check_index_within_bounds(2, todos))

#------------------------------------------------------------------

# Sometimes, you need cannot handle the error just with an if loop
# We need to use - try, catch blocks

# What happens when the user enters something other than a number for the index?

# def get_user_index():  
#     try: # We are going to try and get user input!
#         user_index = int(input("Enter the index to change todo: "))
#         return user_index
#     except Exception as e: # if there is an error execute this code
#         print(e)
#         return -1 # -1 is usually used to signify error from computers

# test = get_user_index()
# print("test: ", test)

#---------------------------------------------------------------------

# Lets acutally handle the error!

def get_user_index(todo_list):
    user_index = None
    while (user_index is None or check_index_within_bounds(user_index, todo_list) is False):
        try:  
            user_index = int(input("Enter the index to change todo: "))
        except Exception as e:  # if there is an error execute this code
            print('Please enter an integer index from the list of todos')
    return user_index

test = get_user_index(todos)
print("test: ", test)

# Ex: Let's reorganize the functions together!

# Bonus: Try and look over v2 with the direct integer comparison, and see if you can fix up the code for it!
