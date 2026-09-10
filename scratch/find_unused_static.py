import os
import re

STATIC_DIR = '/Users/marek-macbook/MBT/nowa strona/MBTWebsite/MBTApp/static'
PROJECT_DIR = '/Users/marek-macbook/MBT/nowa strona/MBTWebsite'

# get all static files
static_files = []
for root, dirs, files in os.walk(STATIC_DIR):
    for f in files:
        if f.startswith('.'):
            continue
        rel_path = os.path.relpath(os.path.join(root, f), STATIC_DIR)
        static_files.append(rel_path)

# find all code files (.html, .css, .js, .py)
code_files = []
for root, dirs, files in os.walk(PROJECT_DIR):
    if 'node_modules' in root or '.venv' in root or '.git' in root or 'migrations' in root or 'staticfiles' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js', '.py')):
            code_files.append(os.path.join(root, f))

# read all code
all_code = ""
for cf in code_files:
    try:
        with open(cf, 'r', encoding='utf-8') as file:
            all_code += file.read() + "\n"
    except Exception as e:
        pass

unused_static = []
for rel_path in static_files:
    filename = os.path.basename(rel_path)
    # search for the filename in the code. This is a heuristic.
    # if the filename is not in all_code, it's definitely unused.
    if filename not in all_code:
        unused_static.append(rel_path)
    
print(f"Total static files: {len(static_files)}")
print(f"Unused static files: {len(unused_static)}")
with open('/Users/marek-macbook/MBT/nowa strona/scratch/unused_static.txt', 'w') as f:
    for u in unused_static:
        f.write(u + '\n')
