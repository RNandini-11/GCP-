# Bucket = like a top-level folder or container.
# Blob = any object (file) stored inside the bucket

from google.cloud import storage

client = storage.Client()

bucket = client.bucket("nandini-storage-20260727")

source_blob = bucket.blob("sample.txt")

bucket.copy_blob(
    source_blob,    #The source file (blob) that you want to copy
    bucket,         # The destination bucket. It can be the same bucket or a different bucket.
    "backup.txt"    # The new name of the copied file in the destination bucket
)

print("Object copied")