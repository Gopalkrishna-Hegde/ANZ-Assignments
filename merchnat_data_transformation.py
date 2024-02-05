import apache_beam as beam

options = {'project': <project>,
           'runner': 'DataflowRunner',
           'region': eroupe west 3,
           'setup_file': <setup.py file>}
pipeline_options = beam.pipeline.PipelineOptions(flags=[], **options)
pipeline = beam.Pipeline(options = pipeline_options)

rows = (p | 'ReadFromBQ' >> beam.io.Read(beam.io.BigQuerySource(query=QUERY, use_standard_sql=True))
        
        
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.value_provider import StaticValueProvider


pipeline_options = PipelineOptions(
    project='your-project-id',
    job_name='dataflow-job',
    staging_location='gs://your-bucket/staging',
    temp_location='gs://your-bucket/temp',
    runner='DataflowRunner'
)


p = beam.Pipeline(options=pipeline_options)


def read_from_bigquery():
    return (p
            | 'Read from BigQuery' >> beam.io.ReadFromBigQuery(
                query='SELECT * FROM `your-project-id.your-dataset.source_table`',
                use_standard_sql=True)
            )


def write_to_bigquery(data):
    return (data
            | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
                table='your-project-id.your-dataset.target_table',
                schema='column_1:string,column_2:integer,column_3:boolean',
                write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)
            )


data = (p
        | 'Read Data' >> beam.Create(['dummy'])  # Create a dummy input element
        | 'Trigger Read' >> beam.FlatMap(lambda x: read_from_bigquery())
        | 'Process Data' >> beam.Map(lambda row: (row['column_1'], row['column_2'], row['column_3']))
        )


write_to_bigquery(data)


p.run()
        
        
#Transformation logic avilable we can do with transformation

mport apache_beam as beam
schema-ID:STRING, City:STRING, Country:STRING'
p2-beam.Pipeline() attcount=(
p2
'Reading File'>> beam.io.ReadFrom Text('merchant_data.csv') |'Upper Case'>> beam.Map(lambda x: x.upper())
|'Splitting Lines'>>beam.Map(lambda x: x.split(',')) ['Convert to
Json'>>beam.Map(lambda x: {"ID":x[0], "City":x[ |'Write to BigQuery'>>beam.io.WriteToBigQuery('dataset.tab
)
p2.run()
