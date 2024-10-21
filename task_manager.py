#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# This program will work with two text files, user.txt and tasks.txt. 
# Open each of the files accompanying this project and note the following:
#       tasks.txt stores a list of all the tasks the team is working on.
#       user.txt stores the username and password for each user that has permission to use your program (task_manager.py).

# This program should allow users to do the following:

#               Prompt the user to enter a username and password.
#               Display an appropriate error message if the user enters a username that is not listed in user.txt or enters a valid username but not a valid password.
#               The user should repeatedly be asked to enter a valid username and password until they provide appropriate credentials.


# The data about the new task should be written to tasks.txt.
# The date on which the task is assigned should be the current date.
# Also, assume that whenever you add a new task, the value that indicates whether the task has been completed or not defaults to ‘No’.
# If the user chooses va to view all tasks, display the information for each task on the screen in an easy-to-read format.
# If the user chooses vm to view the tasks that are assigned to them, only display the tasks that have been assigned to the current user in an easy-to-read format.
# 

username = []
password = []


with open('user.txt', 'a') as file:
    
    while True:
        username_input = input('''Enter your user name : ''').lower()

        if username_input == 'admin':
            '''Admin please enter your password: '''
            print(f"Hi {username_input}.")
            password_input = input('''\nPlease enter your password : ''')
            if password_input == 'adm1n':
                print("Login details match. Welcome Admin! \n")
                break
            else:
                print("Login details don't match. Please try again.\n")
                
        
        else:
            print("User name not found. Please try again\n")

# file.close()


# The following menu should be displayed once the user has successfully logged in [See Capstone 2 PDF]
# If the user chooses r to register a user, they should be prompted for a new username and password.
# User should also be asked to confirm the password.
# If the value entered to confirm the password matches the value of the password,
# Username and password should be written to user.txt in the appropriate format.

# user_req = ()
# user_reg = ()

while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    s - statistics report
    e - exit
    : ''').lower()

    if menu == 'r':
        user_reg = input("\nTo register, please enter user name : ").lower()
        user_password = input("\nPlease enter password : ")
        confirm_password = input("\nPlease enter password once more : ")
        if user_password == confirm_password:
            print("\nNew registration confirmed.")

            with open('user.txt', 'a') as file:
                file.write(f'\n{user_reg}, {user_password}')

        else:
            print("New Registration Details Don't Match.")

        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username =
            - Request input of a new password =
            - Request input of password confirmation. =
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
                otherwise present a relevant message'''

    elif menu == 'a':
        # The data about the new task should be written to - tasks.txt.
        # Request the username of the person the task is assigned to
        # print("\nPlease enter your relevant details below...")        
        user_req = input("\nPlease enter user name\t\t:\t").lower()
        # Request the title of the task
        # The data about the new task should be written to tasks.txt.
        task_title = input("\nTask Title\t\t\t:\t").lower()
        # Request a description of the task
        task_descript = input("\nTask Description\t\t:\t").lower()
        # Request the due date of the task.
        # The date on which the task is assigned should be the current date.
        # Also, assume the value that indicates whether the task has been completed or not defaults to ‘No’.
        date_due = input("\nDue Date\t\t\t:\t").lower()
        current_date = input("\nCurrent Date\t\t\t:\t").lower()
        task_status = input("\nTask Status\t\t\t:\t").lower()
        
        with open('tasks.txt', 'a') as file:
            file.write(f'\n{user_req}, {task_title}, {task_descript}, {date_due}, {current_date}, {task_status}')  

            '''This code block will allow a user to add a new task to task.txt file
            - You can use these steps:
                - Prompt a user for the following: 
                    - the username of the person whom the task is assigned to,
                    - the title of the task,
                    - the description of the task, and 
                    - the due date of the task.
                - Then, get the current date.
                - Add the data to the file task.txt
                - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
        with open('tasks.txt', 'r') as file:
        # Display the information for each task on the screen in an easy-to-read format.
            for line in file:
                line = line.strip()
                line = line.split(', ')
                print(f'\nTask:\t\t\t{line[1]}\nAssigned to:\t\t{line[0]}\nDate Assigned:\t\t{line[3]}\nDue Date:\t\t{line[4]}\nTask Complete?\t\t{line[5]}\nTask Description:\t{line[2]}')
        
        '''This code block will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the PDF
        You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
# 
    elif menu == 'vm':                
        with open('tasks.txt', 'r') as file:
      
            for line in file:
                line = line.strip()
                line = line.split(', ')
                if username_input == line[0]:
                    print(f'\n\nTask:\t\t\t{line[1]}\nDate Assigned:\t\t{line[3]}\nDue Date:\t\t{line[4]}\nTask Complete?\t\t{line[5]}\nTask Description:\t{line[2]}')
    # TASK 2 : 
    elif menu == 's':
        if username_input == 'admin':
            with open('user.txt', 'r') as user_file, open('tasks.txt', 'r') as task_file:
                total_users = len(user_file.readlines())
                total_tasks = len(task_file.readlines())
                # User-friendly Display
                print("\n\t\tS T A T S    R E P O R T : ")
                print(f"\n\nTotal Users: {total_users}")
                print(f"\nTotal Tasks: {total_tasks}")
        else:
            print("\nOnly the admin can access statistics.")            

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made entered an invalid input. Please try again")

    file.close()

