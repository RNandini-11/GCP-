from google.cloud import storage

client = storage.Client()

#----create bucket
bucket = client.create_bucket("gcp-nandini-1103")
print(bucket.name)

#----upload_obj
bucket = client.bucket("gcp-nandini-1103")
blob = bucket.blob("2_upload_obj.py")
blob.upload_from_filename(r"D:\nandini\Cloud GCP\2_upload_obj.py")
print("File uploaded...!")

#----copy_object
bucket = client.bucket("gcp-nandini-1103")
source_blob = bucket.blob("2_upload_obj.py")
bucket.copy_blob(
    source_blob,
    bucket,
    "3_upload_obj.py"
)
print("Object copied successfully...!")

# ---move object
bucket = client.bucket("gcp-nandini-1103")
source_blob = bucket.blob("2_upload_obj.py")
bucket.copy_blob(
    source_blob,
    bucket,
    "Archive/2_upload_obj.py"
)
source_blob.delete()
print("Blob moved successfully...!")

#---delete object
bucket = client.bucket("gcp-nandini-1103")
blob = bucket.blob("3_upload_obj.py")
blob.delete()
print("Object deleted successfully...!")

#---delete bucket
bucket_name = "gcp-nandini-1103"
bucket = client.get_bucket(bucket_name)
bucket.delete()
print(f"Bucket {bucket_name} deleted.")


