# Bucket = like a top-level folder or container.
# Blob = any object (file) stored inside the bucket

from google.cloud import storage

client = storage.Client()

bucket = client.bucket("nandini-storage-20260727")

blob = bucket.blob("sample.txt")

blob.delete()

print("Object deleted")