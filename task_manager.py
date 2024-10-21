import datetime
import os

# Initialize an empty list to store usernames
usernames = []

# Function to register a new user
def register_user():
    while True:
        # Ask the user for their username
        username_input = input('\nEnter your username: ').lower()

        # Check if the username is 'admin'
        if username_input == 'admin':
            print('\n***\t\tHi! admin\t\t* * *')
            password_input = input('\nPlease enter your password: ')

            # Check if the password matches for the admin
            if password_input == 'adm1n':
                print('\n* * *\t\tLogin Successful. Welcome, admin!\t\t* * *\n')
                break
            else:
                print('\n* * * * *\tLogin Details Do Not Match. Please Try Again.\t* * * * *\n')
        else:
            print('\n* * * * *\tUsername Not Found. Please Try Again.\t* * * * *\n')

    while True:
        # Ask for a new username to register
        new_username = input('\nEnter a new username to register: ').lower()

        # Check if the new username already exists
        if new_username in usernames:
            print('\n* * * * *\tUsername Already Exists. Please Choose A Different One.\t* * * * *\n')
        else:
            new_password = input('\nPlease create a new password: ')
            confirm_password = input('\nPlease confirm the password: ')

            # Check if the new password matches the confirmation
            if new_password == confirm_password:
                print('\n\n* * *\t\tNew Registration Confirmed!\t\t* * *\n')

                # Add the new user to a file
                with open('user.txt', 'a') as file:
                    file.write(f'\n{new_username}, {new_password}')

                # Add the new username to the list of usernames
                usernames.append(new_username)
                break
            else:
                print('\n* * * * *\tNew Registration Details Do Not Match. Please Try Again.\t* * * * *\n')

# Function to add a task
def add_task():
    # Ask for the username of the user who needs the task
    user_req = input('\nPlease enter the username: ').lower()
    task_title = input('\nEnter the task title: ').lower()
    task_descript = input('\nEnter the task description: ').lower()
    date_assigned = input('\nEnter the assigned date (e.g., 01 Jan 2023): ')
    date_due = input('\nEnter the due date (e.g., 01 Jan 2023): ')
    task_status = input('\nIs the task completed? (Yes/No): ').lower()

    # Add the task details to a file
    with open('tasks.txt', 'a') as file:
        file.write(f'\n{user_req}, {task_title}, {task_descript}, {date_assigned}, {date_due}, {task_status}')
        print('\n* * *\t\tTask Added Successfully.\t\t* * *\n')

# Function to view all tasks
def view_all():
    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip().split(', ')
            if len(line) == 6:
                print(f'\nTask: {line[1]}\nAssigned to: {line[0]}\nDue Date: {line[3]}\nTask Status: {line[4]}\nTask Description: {line[2]}\n')
            else:
                print('\n* * * * *\t\tInvalid data in tasks.txt\t\t* * * * *\n')

# Function to view tasks for a specific user
def view_user_tasks(current_user):
    task_count = 0
    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip().split(', ')
            if current_user == line[0]:
                print(f'\nTask: {line[1]}\nDue Date: {line[3]}\nTask Status: {line[4]}\nTask Description: {line[2]}\n')
                task_count += 1

# List to store task data
tasks = []

# Function to generate task reports
def generate_reports(admin_username):
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    with open('tasks.txt', 'r') as file:
        for line in file:
            line = line.strip().split(', ')
            tasks.append(line)
            total_tasks += 1

            # Check if the task is completed
            if line[4] == 'Yes':
                completed_tasks += 1
            else:
                uncompleted_tasks += 1

                # Check if the task is overdue
                due_date = datetime.datetime.strptime(line[3], '%d %b %Y')
                today = datetime.datetime.now()
                if today > due_date:
                    overdue_tasks += 1

    # Calculate task statistics
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
    overdue_percentage = (overdue_tasks / total_tasks) * 100

    # Write task overview report to a file
    with open('task_overview.txt', 'w') as task_file:
        task_file.write('\n* * *\t\t\tTasks Overview:\t\t\t* * *\n')
        task_file.write(f'\nTotal number of tasks: {total_tasks}\n')
        task_file.write(f'Total number of completed tasks: {completed_tasks}\n')
        task_file.write(f'Total number of uncompleted tasks: {uncompleted_tasks}\n')
        task_file.write(f'Total number of overdue tasks: {overdue_tasks}\n')
        task_file.write(f'\nPercentage of incompleted tasks: {incomplete_percentage:.2f}%\n')
        task_file.write(f'Percentage of overdue tasks: {overdue_percentage:.2f}%\n')

    # Dictionary to store user task data
    user_tasks = {}

    for task in tasks:
        user = task[0]
        if user not in user_tasks:
            user_tasks[user] = 0
        user_tasks[user] += 1

    total_users = len(user_tasks)

    # Write user overview report to a file
    with open('user_overview.txt', 'w') as user_file:
        user_file.write(f'\nTotal number of users: {total_users}\n')
        user_file.write(f'Total number of tasks generated and tracked: {total_tasks}\n')
        # user_file.write('\n* * *\t\t\tUSER Overview Report\t:\t\t\t* * *\n')

        for user, task_count in user_tasks.items():
            # Calculate user-specific statistics
            percentage_of_total = (task_count / total_tasks) * 100
            completed = sum(1 for task in tasks if task[0] == user and task[4] == 'Yes')
            incomplete = task_count - completed
            overdue = sum(1 for task in tasks if task[0] == user and task[4] == 'No' and today > datetime.datetime.strptime(task[3], '%d %b %Y'))
            user_file.write(f'\nUser: {user}')
            user_file.write(f'\n\nTotal tasks assigned: {task_count}\n')
            user_file.write(f'\nPercentage of total tasks: {percentage_of_total:.2f}%\n')
            user_file.write(f'Percentage of tasks completed: {(completed / task_count) * 100:.2f}%\n')
            user_file.write(f'Percentage of tasks to be completed: {(incomplete / task_count) * 100:.2f}%\n')
            user_file.write(f'Percentage of overdue tasks: {(overdue / task_count) * 100:.2f}%\n')

# Function to display statistics
def display_stats(username_input):
    if username_input == 'admin':
        if not (os.path.isfile('task_overview.txt') and os.path.isfile('user_overview.txt')):
            generate_reports('admin')

        with open('task_overview.txt', 'r') as task_file, open('user_overview.txt', 'r') as user_file:
            task_report = task_file.read()
            user_report = user_file.read()

        # print('\n* * *\t\tTask Overview Report\t:\t\t* * *\n')
        print(task_report)
        print('\n* * *\t\t\tUser Overview\t:\t\t* * *\n')
        print(user_report)
    else:
        print('\n* * * * *\tOnly The Admin Can Access Statistics.\t* * * * *\n')

# Main menu
while True:
    if 'username_input' not in locals() or 'username_input' not in globals():
        username_input = input('\nEnter your username: ').strip().lower()
        if username_input == 'admin':
            print('\n* * *\t\t\tWelcome, admin!\t\t* * *\n')
            entered_password = input('\nPlease enter your password: ').strip()
            if entered_password == 'adm1n':
                print('\n* * * * *\t\tLogin Successful. Welcome, admin!\t\t* * * * *\n')
                continue
            else:
                print('\n* * * * *\tLogin Details Do Not Match. Please Try Again.\t* * * * *\n')
                continue

    menu = input('Select one of the following options:\n'
                 'r - Register a user\n'
                 'a - Add a task\n'
                 'va - View all tasks\n'
                 'vm - View my tasks\n'
                 'gr - Generate reports\n'
                 'ds - Display statistics\n'
                 'e - Exit\n: ').lower()

    if menu == 'r':
        register_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        username_input = input('\nPlease enter your username: ').lower()
        # if username_input == 'admin':
        view_user_tasks(username_input)
            
    elif menu == 'gr':
        username_input = input('\nEnter your username: ').strip().lower()
        entered_password = input('\nEnter your password: ').strip()
        if username_input == 'admin' and entered_password == 'adm1n':
            admin_username = 'admin'
            generate_reports(admin_username)
            print('\nReports Generated. You Can View Them In task_overview.txt And user_overview.txt\n')
        else:
            print('\n* * * * *\tAccess Denied! Invalid Username or Password.\t* * * * *\n')
    elif menu == 'ds':
        username_input = input('\nEnter your username: ').strip().lower()
        if username_input == 'admin':
            entered_password = input('\nEnter your password: ').strip()
            if entered_password == 'adm1n':
                display_stats(username_input)
            else:
                print('\n* * * * *\tAccess Denied! Wrong Password.\t* * * * *\n')
        else:
            print('\n* * * * *\t\tAccess Denied!\t\t* * * * *\n')
    elif menu == 'e':
        print('\n* * *\tGoodbye!\t* * *\n')
        exit()
    else:
        print('\n* * * * *\tInvalid Input. Please Try Again.\t* * * * *\n')
