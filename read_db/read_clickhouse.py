import pandahouse

connection = {
    'host': 'https://clickhouse.lab.karpov.courses',
    'password': 'dpo_python_2020',
    'user': 'student',
    'database': 'simulator_20230320'
}

q = 'SELECT * FROM {db}.feed_actions where toDate(time) = today() limit 100'

df = pandahouse.read_clickhouse(q, connection=connection)

print(df.head())