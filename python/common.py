import requests
from requests import Response
from typing import Callable

def get_auth_headers(user_key):
    headers = {
        'X-Redmine-API-Key': user_key,
        'Content-Type': 'application/json'
    }
    return headers

def get_all(url:str, headers:dict, parse_data:Callable[[Response],list]):
    dreturn = []
    total = 1
    offset = 0
    limit = 100
    while total > offset:
        params = {
            'limit':limit,
            'offset': offset
        }
        r = requests.get(url, headers=headers, params=params)
        data = r.json()

        total = int(data['total_count'])
        offset = int(data['offset'])
        limit = int(data['limit'])
        offset += limit

        dreturn.extend(parse_data(data))
    return dreturn


def format_issue(project:int, parent: int, task:str):
    issue = {
        'project_id': project,
        'subject': task,
        'parent_issue_id': parent
    }
    return issue

def create_issue(base_url:str, auth_headers, task):
    url = f"https://{base_url}/issues.json"
    r = requests.post(url, headers=auth_headers, json={'issue':task})
    if not r.ok:
        raise Exception(r.content)
    return r.json()


def create_issue_tree(base_url:str, auth_headers:dict, project, parent_id, task):
    subject = task['task']
    task_project = task['project'] if 'project' in task else project
    issue = format_issue(task_project, parent_id, subject)
    created_issue = create_issue(auth_headers, issue)
    created_issue_id = created_issue['issue']['id']

    if 'subtasks' in task:
        for subtask in task['subtasks']:
            create_issue_tree(base_url, auth_headers, project, created_issue_id, subtask)
