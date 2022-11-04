import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'asl-machinelearning-367219-7441be2611ac.json'

storage_client = storage.Client()

dir(storage_client)

"""
Create bucket
"""
bucket_name = "repo-image-training"
bucket = storage_client.bucket(bucket_name)
bucket.storage_class = 'COLDLINE' # Archive | Nearline | Standard
bucket.location = "US"
bucket = storage_client.create_bucket(bucket)
"""
Read from bucket (GET)
"""
print(vars(bucket))
bucket.name
bucket._properties['selfLink']
bucket._properties['id']
bucket._properties['location']
bucket._properties['timeCreated']
bucket._properties['storageClass']
bucket._properties['timeCreated']
bucket._properties['updated']
#Accessing to a specific Bucket
image_bucket = storage_client.get_bucket(bucket_name)
"""
Upload files to the bucket
"""
def upload_to_bucket(blob_name, file_path, bucket_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        return blob
    except Exception as e:
        print(e)
        return False

file_path =  r"E:\GCP firebase\storage\training-images-repo" #Editar
upload_to_bucket("/TrainingImages/image001", os.path.join(file_path, "sheep-test.jpeg"), bucket_name)

"""
Download Files
"""
def download_file_from_bucket(blog_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blog_name)
    with open(file_path, 'wb') as f:
        storage_client.download_blob_to_file(blob, f)
    print('Saved')

"""
List Buckets
list_buckets(max_results=None, page_token=None, prefix=None, projection='noAcl', fields=None, project=None, timeout=60, retry=<google.api_core.retry.Retry object>)
"""
for bucket in storage_client.list_buckets(max_results=100):
    print(bucket)