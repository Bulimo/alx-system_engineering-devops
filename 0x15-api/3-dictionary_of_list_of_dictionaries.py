#!/usr/bin/python3
"""
Python script that given employee ID, returns information
about his/her TODO list progress.
"""
import json
import requests


def employee_todo_progress():
    """
    Method to retrieve the employee's TODO list and print progress
    """
    # Make a GET request to retrieve the employee's information
    user_url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(user_url)

    # get employees TODO list
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todo_url)

    if user_response.status_code == 200 and response.status_code == 200:
        user_info = user_response.json()
        tasks = response.json()
        data = {}

        for user in user_info:
            employee_name = user.get('name')
            employee_id = user.get('id')

            # create dict of dicts
            user_tasks = []
            for task in tasks:
                json_task = {}
                if task.get('userId') == employee_id:
                    json_task = {
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": employee_name
                    }
                    user_tasks.append(json_task)
            data[employee_id] = user_tasks

        # Export to JSON
        file_name = "todo_all_employees.json"
        with open(file_name, 'w') as json_output:
            json.dump(data, json_output)


if __name__ == '__main__':
    employee_todo_progress()
