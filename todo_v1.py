
# SHOULD CREATE A JUPYTER NOTEBOOK???

# v1

# Print
print("TODO App") # "" Anything in quotes are called strings

#--------------------------------------------------------------------------------------------------------------------------------

# Vars
todo_title = 'Welcome to our TODO APP!'

print(todo_title)
# Note: you can't assign vars 'TODO App' = todo_title doesn't work!
# Spaces are important to the machine, don't accidentally leave a space -- they are considered arguments

#--------------------------------------------------------------------------------------------------------------------------------

# Lets now work on the actual todo lists!

# lists
# We will store our todos in the form of lists
# A list/array is a list of items 
todos = ['wash the dishes', 'finish homework', 'go for a run']


# Pop - removes items from the list
# todos.pop(0) # 0 is the first element
# print(todos)

# Insert - adds items to the list
# todos.insert(0, 'new task')
# print(todos)

#--------------------------------------------------------------------------------------------------------------------------------
# Get user input
user_input = input("Enter a new todo: ") # We store the user input in a variable
print("Your new todo is: ", user_input)

#--------------------------------------------------------------------------------------------------------------------------------
# Lets have some user interaction -- bring everything together

# Show current list
print("Current list of todo: ", todos)

# Add a new todo
user_input = input("Enter a new todo: ") # We store the user input in a variable
print("The new todo is: ", user_input)
todos.insert(0, user_input)

print("New list of todos: ", todos)

# Delete a todo
user_input = int(input("Enter the index to remove todo: ")) # We store the user input in a variable
# Note: I am changing the type to an int... why am I doing so?

print("The index is: ", user_input)
todos.pop(user_input)

print("New list of todos: ", todos)

# How can we use the above to allow people to change a todo?

### -------------------------------------- SOLUTION --------------------------------------------

# Change = Delete + Add!
user_index = int(input("Enter the index to change todo: ")) # We store the user input in a variable

print("The index is: ", user_index)
todos.pop(user_index)
new_todo = input("Enter a modified todo: ") # We are creating an illusion of modification
print("The modified todo is: ", new_todo)
todos.insert(user_index, new_todo)

print("New list of todos: ", todos)

# Or, we can be more efficient and change the todo directly!
# We can access individual items based on their indicies Name_Of_List[Index number]
print("First todo: ", todos[0])
todos[user_index] = new_todo

# Congradulations! You have created the most basic form of a todo app

#--------------------------------------------------------------------------------------------------------------------------------


