# Define a class for tasks
class Task:
    def __init__(self,name,duration,priority):
        self.name = name # The name of the task
        self.duration = duration # The duration of the task in minutes
        self.priority = priority # The priority level of the task from 1 (highest) to 5 (lowest)

    def _str_(self):
        return f"{self.name} ({self.duration} minutes, priority {self.priority})"

# Define a list of tasks
tasks = [
    Task("Do homework", 60, 1),
    Task("Clean the room", 30, 2),
    Task("Call mom", 15, 3),
    Task("Watch a movie", 120, 4),
    Task("Play video games", 90, 5)
]

# Define a function to sort the tasks by priority and duration
def sort_tasks(tasks):
    # Use a lambda function to sort the tasks by priority first, then by duration in ascending order
    return sorted(tasks, key=lambda task: (task.priority, task.duration))

# Define a function to make a schedule based on the sorted tasks and the available time
def make_schedule(tasks, available_time):
    # Initialize an empty schedule
    schedule = []
    # Initialize the current time as zero
    current_time = 0
    # Loop through the sorted tasks
    for task in tasks:
        # Check if the task can fit in the available time
        if current_time + task.duration <= available_time:
            # Add the task to the schedule
            schedule.append(task)
            # Update the current time
            current_time += task.duration
        else:
            # Break the loop if the task cannot fit
            break
    # Return the schedule
    return schedule

# Sort the tasks by priority and duration
sorted_tasks = sort_tasks(tasks)
# Print the sorted tasks
print("Sorted tasks:")
for task in sorted_tasks:
    print(task)

# Make a schedule based on the sorted tasks and the available time of 180 minutes
schedule = make_schedule(sorted_tasks, 180)
# Print the schedule
print("Schedule:")
for task in schedule:
    print(task)
