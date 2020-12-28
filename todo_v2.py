# v2

# Keep the following uncommented
todo_title = 'Welcome to our TODO APP!'
print(todo_title)
todos = ['wash the dishes', 'finish homework', 'go for a run']

#--------------------------------------------------------------------------------------------------------------------------------

# # Control flows

# # for loop - print the todos nicer
# # Note: Computers start counting from 0, so 0 is the first item
# print("List of Todos:")
# print("0 - ", todos[0])
# print('1 - ', todos[1])
# print('2 - ', todos[2])

# # However, this is very inefficient, and we are repeating ourselves
# # Instead, we can use a for loop to go over all elements in the list
# print('List of Todos:')
# for index, todo in enumerate(todos):
#     print(index, " - ", todo)
    
#--------------------------------------------------------------------------------------------

# Lets have more user interactions!

todo_options = """
Please select an option:
1 - Add a todo
2 - Delete a todo
3 - Change a todo
4 - quit
""" # Doc strings """ allow you to create a string accross multiple lines

# # if loop -- react to the user's input
# print(todo_options)
# user_input = input("Enter option: ")
# if (user_input == '1'): # == means equals
#     print("Adding a todo...")
# elif (user_input == '2'):
#     print("Deleting a todo...")
# elif (user_input == '3'):
#     print("Changing a todo...")
# elif (user_input == '4'):
#     print("Bye!")

# # Note: it is important to have the quotation marks around the options -- '1', to keep the string type consistent

# # Let's implement the above code using what we have leannt!

### -------------------------------------- SOLUTION --------------------------------------------

# # if loop -- react to the user's input
# user_input = input("Enter option: ")
# if (user_input == '1'): # == means equals
#     # Add a new todo ------ from v1
#     user_input = input("Enter a new todo: ") # We store the user input in a variable
#     todos.insert(0, user_input)
# elif (user_input == '2'):
#     # Delete a todo ------ from v1
#     user_input = int(input("Enter the index to remove todo: "))
#     todos.pop(user_input)
# elif (user_input == '3'):
#     # Change a todo ------ from v1
#     user_index = int(input("Enter the index to change todo: ")) 
#     new_todo = input("Enter a modified todo: ") 
#     todos[user_index] = new_todo
# elif (user_input == '4'):
#     print("Bye!")

# print('List of Todos:')
# for index, todo in enumerate(todos):
#     print(index, " - ", todo)

#--------------------------------------------------------------------------------------------

# # How to we ask for multiple options and not just only one?
# # While loop 
# user_input = input("Enter option: ")
# while (user_input != '4'): # The ! means not (negation)
#     print(todo_options)
#     user_input = input("Enter option: ") # What happens when we comment out this line? or wrongly indent it?
#     print("Your option is ", user_input)
# print('Bye!')


#--------------------------------------------------------------------------------------------------------------------------------

# suppose we remove the quotations around the options, what happens?
# user_input = input("Enter option: ")
# while (user_input != 4): # The ! means not (negation)
#     print(todo_options)
#     user_input = input("Enter option: ")
#     print("Your option is ", user_input)
# print('Bye!')

# Types -- different types are like comparing apples to oranges, they may both be spherical, but they are fundementally different
# user_input = input("Enter option: ")
# print(type(user_input))
# print(type(4))

# We can solve this issue through typecasting as well as using the quotes
# user_input = int(input("Enter option: "))
# print(type(user_input))
# print(type(4))

# Now it works fine... or does it?
# user_input = int(input("Enter option: "))
# while (user_input != 4): 
#     print(todo_options)
#     user_input = int(input("Enter option: "))
#     print("Your option is ", user_input)
# print('Bye!')
# What if the user enters something else for the typecasting option?? 


# Which option is better? -- '' would be better in this case as it handles more errors
# Note: there are multiple ways to solve a problem, good programming is about finding the best solution

#--------------------------------------------------------------------------------------------------------------------------------

# Lets bring everything together!

### -------------------------------------- SOLUTION --------------------------------------------

line_sperator = '--------------------------------' # Used for clarity and better asthetics

user_input = None # Start off with some arbitary number that is not 4, or None
while (user_input != '4'): # The ! means not (negation)
    # Print out all the options --- use the for loop from above
    print('List of Todos:')
    for index, todo in enumerate(todos):
        print(index, " - ", todo)
    print(line_sperator)
    # Combine from the solution from above!
    print(todo_options)
    user_input = input("Enter option: ")
    if (user_input == '1'):  
        # Add a new todo ------ from v1
        user_input = input("Enter a new todo: ") # We store the user input in a variable
        todos.insert(0, user_input)
    elif (user_input == '2'):
        # Delete a todo ------ from v1
        user_input = int(input("Enter the index to remove todo: "))
        todos.pop(user_input)
    elif (user_input == '3'):
        # Change a todo ------ from v1
        user_index = int(input("Enter the index to change todo: "))
        new_todo = input("Enter a modified todo: ")
        todos[user_index] = new_todo
    elif (user_input == '4'):
        print("Bye!")
    print(line_sperator) # To make things a bit clearer between different options
