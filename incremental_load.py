#brief idea about incremental data load

from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig

def incremental_load_to_bigquery(dataset_id, table_id, source_uri, schema):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = LoadJobConfig(schema=schema, source_format='CSV', write_disposition='WRITE_APPEND')
    
    load_job = client.load_table_from_uri(source_uri, table_ref, job_config=job_config)
    load_job.result()  # Waits for the job to complete.

    print(f'Incremental data loaded from {source_uri} to {dataset_id}.{table_id}')

if __name__ == "__main__":
    dataset_id = 'your_dataset_id'
    table_id = 'your_table_id'
    source_uri = 'gs://your_bucket_name/your_incremental_data.csv'
    schema = [
        bigquery.SchemaField('field1', 'STRING'),
        bigquery.SchemaField('field2', 'INTEGER'),
        # Add more fields as necessary
    ]
    
    incremental_load_to_bigquery(dataset_id, table_id, source_uri, schema)
