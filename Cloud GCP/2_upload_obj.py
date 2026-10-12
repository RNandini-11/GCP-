
# Bucket = like a top-level folder or container.
# Blob = any object (file) stored inside the bucket
from google.cloud import storage

client = storage.Client()

bucket = client.bucket("nandini-storage-20260727")

#A blob is Google Cloud Storage's name for an object (file).
blob = bucket.blob("sample.txt") 

#uploads the local file from your computer to the blob in the bucket
blob.upload_from_filename(r"D:\files\sample.txt")

print("File uploaded")

#bucket = a folder
#blob = a file inside that folder