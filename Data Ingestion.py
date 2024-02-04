from google.cloud import storage

def upload_to_bucket(blob_name, path_to_file, bucket_name):
     storage_client = storage.Client.from_service_account_json('Merchant_data.csv')
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    return blob.public_url
