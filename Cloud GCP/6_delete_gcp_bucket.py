# Imports the Google Cloud client library
from google.cloud import storage

storage_client = storage.Client()

bucket_name = "gcp-nandini-1103"

# Retrieves the existing bucket
bucket = storage_client.get_bucket(bucket_name)

bucket.delete()

print(f"Bucket {bucket_name} deleted.")
