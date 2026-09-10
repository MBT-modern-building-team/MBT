import sys

with open('Construz/scripts/gen_mbt_data.py', 'r') as f:
    content = f.read()

content = content.replace("        + _section('ARTICLES', arts) + '\n'\n        + _section('AWARDS', awards) + '\n'\n        + f'PHOTOS = {_dump(photos)}\n'", "        + _section('ARTICLES', arts) + '\\n'\n        + _section('AWARDS', awards) + '\\n'\n        + f'PHOTOS = {_dump(photos)}\\n'")

with open('Construz/scripts/gen_mbt_data.py', 'w') as f:
    f.write(content)
