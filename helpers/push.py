import json
import random
from datetime import date

TOPIC_WORD_LIMIT = 100

tasks_file = 'files/in_progress.json'

tasks = []
input_file = f"files/theories.json"
data = json.load(open(input_file, "rt", encoding="UTF-8"))
for item in data:
    task = { 
        "name": item['name'],
        "text_prompt": f"Расскажи интересный факт про теорию '{item['name']}' из категории '{item['category']}' из области '{item['domain']}', используй не более {TOPIC_WORD_LIMIT} слов, используй смайлики",
        "image_prompt": f"Нарисуй рисунок, вдохновлённый теорией '{item['name']}' из категории '{item['category']}' из области '{item['domain']}'",
        "group": f"{item['domain']}/{item['category']}",
    }
    tasks.append(task)

random.seed(date.today().year)
random.shuffle(tasks)

for i, task in enumerate(tasks):
    task['index'] = i + 1

json.dump(tasks, open(tasks_file, 'wt', encoding='UTF-8'), indent=4, ensure_ascii=False)
print(f"{len(tasks)} tasks created")
