import json
import random

with open('dbpedia_samples.jsonl','r') as FILE_:
    lines = FILE_.readlines()

selections = random.choices(lines, k=10)

for idx, selection in enumerate(selections):
    paragraph = (json.loads(selection)).get('text', None)
    if paragraph:
        with open(f'file{str(idx)}.txt','w') as sample:
            sample.write(paragraph)
