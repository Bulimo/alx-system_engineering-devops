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
        username = user_info.get('username')

        # get employees TODO list
        todo_url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(todo_url)
        tasks = response.json()

        # calculate the progression
        user_tasks = []
        data = {}
        for task in tasks:
            json_task = {}
            if task.get('userId') == id:
                json_task = {
                    "task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": username
                }
                user_tasks.append(json_task)
        data[id] = user_tasks

        # Export to JSON
        file_name = "{}.json".format(id)
        with open(file_name, 'w') as json_output:
            json.dump(data, json_output)


if __name__ == '__main__':
    try:
        employee_todo_progress(argv[1])
    except Exception:
        pass
