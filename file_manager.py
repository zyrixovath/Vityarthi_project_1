import json
import os

FILE_NAME = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data.json"
)


def load_tasks():

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as file:
            return json.load(file)

    return []


def save_tasks(tasks):

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)