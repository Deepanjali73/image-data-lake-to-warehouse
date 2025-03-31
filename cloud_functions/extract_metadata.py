from google.cloud import storage
import json

def extract_metadata(event, context):
    file = event
    bucket_name = file['bucket']
    file_name = file['name']
    metadata = {
        "image_id": file_name.split('.')[0],
        "upload_timestamp": file['timeCreated'],
        "image_format": file_name.split('.')[-1],
        "size": int(file['size']),
        "category": file_name.split('/')[0] if '/' in file_name else "uncategorized"
    }
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"metadata/{file_name}.json")
    blob.upload_from_string(json.dumps(metadata))
    return f"Metadata extracted for {file_name}"
