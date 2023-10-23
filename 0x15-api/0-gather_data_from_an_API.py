#!/usr/bin/python3
"""
Python script that given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests
from sys import argv


def employee_todo_progress(employee_id):
    """
    Method to retrieve the employee's TODO list and print progress
    """
    id = int(employee_id)
    # Make a GET request to retrieve the employee's information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user_response = requests.get(user_url)
    if user_response.status_code == 200:
        user_info = user_response.json()
        employee_name = user_info.get('name')

        # get employees TODO list
        todo_url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(todo_url)
        tasks = response.json()

        # calculate the progression
        total_tasks = 0
        completed_tasks = []
        for task in tasks:
            if task.get('userId') == id:
                total_tasks += 1
                if task.get('completed'):
                    completed_tasks.append(task)
        print("Employee {} is done with tasks({}/{}):".format(employee_name,
              len(completed_tasks), total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task.get('title')))


if __name__ == '__main__':
    try:
        employee_todo_progress(argv[1])
    except Exception:
        pass
