import os
import re

DB_DUMP = '/Users/marek-macbook/MBT/nowa strona/scratch/db_dump.sql'
MEDIA_DIR = '/Users/marek-macbook/MBT/nowa strona/MBTWebsite/media'

# Read the database dump
with open(DB_DUMP, 'r', encoding='utf-8') as f:
    db_text = f.read()

# Get all files in media directory
media_files = []
for root, dirs, files in os.walk(MEDIA_DIR):
    for f in files:
        if f.startswith('.'):
            continue
        rel_path = os.path.relpath(os.path.join(root, f), MEDIA_DIR)
        media_files.append(rel_path)

# Check which media files are referenced in the database dump
unused_media = []
for rel_path in media_files:
    # Look for the filename in the DB dump.
    filename = os.path.basename(rel_path)
    if filename not in db_text:
        unused_media.append(rel_path)

print(f"Total media files: {len(media_files)}")
print(f"Unused media files: {len(unused_media)}")

for u in unused_media:
    print(f"Removing: {u}")
    os.remove(os.path.join(MEDIA_DIR, u))
