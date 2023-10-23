#!/usr/bin/python3
"""
Python script that given employee ID, returns information
about his/her TODO list progress.
"""
import csv
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
        user_tasks = []
        for task in tasks:
            if task.get('userId') == id:
                user_tasks.append(task)

        # Export to CSV
        file_name = "{}.csv".format(id)
        with open(file_name, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME",
                          "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(
                csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL
            )
            writer.writeheader()

            for task in user_tasks:
                task_status = "True" if task.get('completed') else "False"
                writer.writerow({
                    "USER_ID": id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": task_status,
                    "TASK_TITLE": task.get('title')
                })


if __name__ == '__main__':
    try:
        employee_todo_progress(argv[1])
    except Exception:
        pass
