# Bucket = like a top-level folder or container.
# Blob = any object (file) stored inside the bucket

from google.cloud import storage

client = storage.Client()

bucket = client.bucket("nandini-storage-20260727")

source_blob = bucket.blob("sample.txt")

bucket.copy_blob(
    source_blob,            # The source file (blob) that you want to copy
    bucket,                 # The destination bucket
    "archive/sample.txt"    # # Store the copied file inside the "archive" folder
)

source_blob.delete()

print("Object moved")