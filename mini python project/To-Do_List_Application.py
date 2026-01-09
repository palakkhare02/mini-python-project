def add_task(tasks):
    """Function to add a new task to the task list."""
    task = input("Enter a new task: ").strip()  # Get user input for the new task
    if task:  # Check if the task is not empty
        tasks.append(task)  # Add the task to the list
        print(f'Task added: "{task}"')  # Confirm the addition
    else:
        print("Empty task cannot be added.")  # Handle empty input

def view_tasks(tasks):
    """Function to display all tasks in the task list."""
    if not tasks:  # Check if the task list is empty
        print("No tasks in the list.")  # Inform the user
    else:
        print("\nYour To-Do List:")  # Header for the task list
        for idx, task in enumerate(tasks, 1):  # Enumerate through tasks with index
            print(f"{idx}. {task}")  # Print each task with its index
        print("")  # Print a newline for better readability

def remove_task(tasks):
    """Function to remove a task from the task list by its number."""
    if not tasks:  # Check if the task list is empty
        print("No tasks to remove.")  # Inform the user
        return  # Exit the function
    view_tasks(tasks)  # Display current tasks
    try:
        task_num = int(input("Enter the number of the task to remove: "))  # Get user input for task number
        if 1 <= task_num <= len(tasks):  # Validate the task number
            removed = tasks.pop(task_num - 1)  # Remove the task from the list
            print(f'Removed task: "{removed}"')  # Confirm the removal
        else:
            print("Invalid task number.")  # Handle invalid input
    except ValueError:
        print("Please enter a valid number.")  # Handle non-integer input

def main():
    """Main function to run the To-Do List application."""
    tasks = []  # Initialize an empty list to store tasks
    while True:  # Infinite loop for the menu
        print("\nTo-Do List Application")  # Application title
        print("1. Add Task")  # Option to add a task
        print("2. View Tasks")  # Option to view tasks
        print("3. Remove Task")  # Option to remove a task
        print("4. Exit")  # Option to exit the application
        choice = input("Choose an option (1-4): ").strip()  # Get user choice
        if choice == "1":
            add_task(tasks)  # Call function to add a task
        elif choice == "2":
            view_tasks(tasks)  # Call function to view tasks
        elif choice == "3":
            remove_task(tasks)  # Call function to remove a task
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid choice. Please select 1, 2, 3 or 4.")  # Handle invalid choice

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
