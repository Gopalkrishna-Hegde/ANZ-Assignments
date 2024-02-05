#Design idea about splitting the data
import os

historical_data_dir = 'gs://path/to/merchants_historical/data'
limit_gb = 30
total_size_gb = 600
num_chunks = total_size_gb / limit_gb
num_chunks = int(num_chunks)
chunk_size_bytes = limit_gb * 1024 * 1024 * 1024
output_dir = 'gs://path/to/output/merchants_historical/chunks'
os.makedirs(output_dir, exist_ok=True)


with open(os.path.join(historical_data_dir, 'merchants_historical_data.csv'), 'rb') as f:
    for i in range(num_chunks):
        chunk_data = f.read(chunk_size_bytes)
        if chunk_data:
            with open(os.path.join(output_dir, f'chunk_{i+1}.csv'), 'wb') as chunk_file:
                chunk_file.write(chunk_data)
        else:
            break

from google.cloud import bigquery
def create_table():
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat=,source_format skip_leading_rows=1, autodetect=True,
    )

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file=source_file, table_id=table_id, job_config=job_config)

job.result()

table = client.get_table(table_id)
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)

{
  "Load_data_into_bq": {
    "TYPE": "Python_operator"
    "source_path": "bucketname/file_name"
    "destination bucket":"bucketname/source_files/file_name"
    "Table_id":"test_table"
    
  }
    "GRAPH" : "start >> Load_data_into_bq >> end"
}


import os


daily_data_dir = '/path/to/daily/data'


chunk_size_limit_gb = 30


total_size_gb = 25
num_chunks = total_size_gb / limit_gb


num_chunks = int(num_chunks)


chunk_size_bytes = limit_gb * 1024 * 1024 * 1024

# Create a directory to store the chunks
output_dir = 'gs://path/to/merchants_historical/data'
os.makedirs(output_dir, exist_ok=True)

# Split the daily transaction data into chunks
with open(os.path.join(daily_data_dir, 'merchnats_data.csv'), 'rb') as f:
    for i in range(num_chunks):
        chunk_data = f.read(chunk_size_bytes)
        if chunk_data:
            with open(os.path.join(output_dir, f'chunk_{i+1}.csv'), 'wb') as chunk_file:
                chunk_file.write(chunk_data)
        else:
            break

print("Data splitting complete.")
