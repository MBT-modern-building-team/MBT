import re

with open('MBTWebsite/MBTApp/mbt_data.py', 'r') as f:
    content = f.read()

# We need to insert Lukasz Liszka into SALES_REPS
new_rep = """ {'email': 'l.liszka@mbt.pl',
  'name': 'Łukasz Liszka',
  'order': 4,
  'phone': '+48 881 202 306',
  'photo': '',
  'position': 'Manager ds. handlowych/Business Development Manager',
  't_p': {}}]"""

content = re.sub(r"'t_p': {}}\]", "'t_p': {}},\n" + new_rep, content, count=1)

with open('MBTWebsite/MBTApp/mbt_data.py', 'w') as f:
    f.write(content)
