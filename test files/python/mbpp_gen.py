import json
import random

import requests

data = requests.get('https://raw.githubusercontent.com/google-research/google-research/master/mbpp/mbpp.jsonl')

problems = data.text.splitlines()

training_problems = random.choices(problems[600:],k=7)
start = 4

readme_lines = []
for file_no, line in enumerate(training_problems):
    problem = json.loads(line)
    task_id = problem['task_id']
    text = problem['text']
    code = problem['code']
    file_name = f'file{file_no + start}.py'
    readme_line = f'{file_name} = task_id {task_id} - {text}'
    with open(f'test files/python/{file_name}', 'w') as FILE_:
        FILE_.write(code)
    
    readme_lines.append(readme_line)

with open(f'test files/python/README','a') as FILE_:
    FILE_.write('\n'.join(readme_lines))
# text

# for range(4,training_problems)

# file3.py = task_id 824 - Write a python function to remove even numbers from a given list.