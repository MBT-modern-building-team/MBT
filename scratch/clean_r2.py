import os
import re
import boto3
from dotenv import load_dotenv

# Load env variables
load_dotenv('MBTWebsite/.env')

DB_DUMP = 'scratch/db_dump.sql'

with open(DB_DUMP, 'r', encoding='utf-8') as f:
    db_text = f.read()

# Cloudflare R2 Config
r2_account_id = os.getenv('R2_ACCOUNT_ID')
r2_access_key = os.getenv('R2_ACCESS_KEY_ID')
r2_secret_key = os.getenv('R2_SECRET_ACCESS_KEY')
r2_bucket = os.getenv('R2_BUCKET')

if not all([r2_account_id, r2_access_key, r2_secret_key, r2_bucket]):
    print("R2 credentials not fully set in .env")
    exit(1)

endpoint_url = f"https://{r2_account_id}.r2.cloudflarestorage.com"

s3 = boto3.client(
    's3',
    endpoint_url=endpoint_url,
    aws_access_key_id=r2_access_key,
    aws_secret_access_key=r2_secret_key,
    region_name='auto',
)

# List all objects
objects = []
paginator = s3.get_paginator('list_objects_v2')
for page in paginator.paginate(Bucket=r2_bucket):
    if 'Contents' in page:
        for obj in page['Contents']:
            objects.append(obj['Key'])

print(f"Total objects in R2 bucket '{r2_bucket}': {len(objects)}")

unused_objects = []
for key in objects:
    # the key is like media/uploads/file.jpg or uploads/file.jpg
    filename = os.path.basename(key)
    
    # Check if this filename appears in the db dump
    if filename and filename not in db_text:
        unused_objects.append(key)

print(f"Unused objects found: {len(unused_objects)}")

# Delete them
deleted_count = 0
for key in unused_objects:
    print(f"Deleting from R2: {key}")
    s3.delete_object(Bucket=r2_bucket, Key=key)
    deleted_count += 1

print(f"Total deleted from R2: {deleted_count}")

