import json
from pathlib import Path


notebooks = list(Path('.').rglob('*.ipynb'))
for notebook in notebooks:
    with notebook.open(encoding='utf-8') as stream:
        document = json.load(stream)
    if document.get('nbformat') not in {4, 5} or not isinstance(document.get('cells'), list):
        raise SystemExit(f'Notebook inválido: {notebook}')
print(f'{len(notebooks)} notebooks válidos')
