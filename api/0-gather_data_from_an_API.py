#!/usr/bin/python3
"""
This module fetches and displays an employee's TODO list progress using a REST API.
"""
import requests
import sys


def get_todo_progress(employee_id):
    """
    Fetches employee name and task data, then prints the formatted progress.
    """
    base_url = "https://typicode.com"

    # Fetch user data safely
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_res = requests.get(user_url)
    user_data = user_res.json()
    employee_name = user_data.get("name")

    # Fetch todo tasks data safely
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_res = requests.get(todos_url)
    tasks = todos_res.json()

    # Calculate task metrics
    total_tasks = len(tasks)
    done_tasks = [task for task in tasks if task.get("completed") is True]
    num_done_tasks = len(done_tasks)

    # Print summary header line
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_done_tasks, total_tasks
    ))

    # Print titles of completed tasks with 1 tab and 1 space
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            get_todo_progress(emp_id)
        except ValueError:
            pass

