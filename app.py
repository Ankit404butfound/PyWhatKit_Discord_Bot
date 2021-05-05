from google.cloud import bigquery
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config.json"
client = bigquery.Client()

query = """
   SELECT count(*) as Downloads
FROM `bigquery-public-data.pypi.file_downloads`
WHERE file.project = 'pywhatkit'
  -- Only query the last 30 days of history
  AND DATE(timestamp)
    BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 0 DAY)
    AND CURRENT_DATE()
"""
query_job = client.query(query)  # Make an API request.

print("The query data:")
row = [*query_job][0]
print(row[0])

