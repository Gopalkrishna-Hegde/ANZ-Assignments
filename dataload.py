#It is just code snippet and design idea need to develop more 

#load the data into datawarehouse
create_table = BigQueryCreateEmptyTableOperator(
    task_id="create_table",
    dataset_id=DATASET_NAME,
    table_id="test_table",
    schema_fields=[
        {"name": "Merchant_id", "type": "STRING", "mode": "REQUIRED"},
        {"name": "Merchant_Name", "type": "STRING", "mode": "REQUIRED"}
        
    ]
)
 bq_load = PythonOperator(
            task_id='bq_load_{}_{}'.format(table_name,table_config[1]),
            python_callable=
            bqimport,
            op_kwargs={'tablename':table_name,'schedule': schedule, 'ts':now, 'dag': dag},
            provide_context=True,
            dag=dag
        ) 
