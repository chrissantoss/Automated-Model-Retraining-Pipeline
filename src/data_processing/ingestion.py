import boto3
import json
from datetime import datetime

def ingest_data(stream_name, data):
    kinesis_client = boto3.client('kinesis')
    
    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(data),
        PartitionKey=str(datetime.now().timestamp())
    )
    
    return response

def main():
    stream_name = 'your-stream-name'
    
    # Example data - replace with your actual data source
    data = {
        'timestamp': str(datetime.now()),
        'value': 42,
        # Add other relevant fields
    }
    
    response = ingest_data(stream_name, data)
    print(f"Data ingested. Sequence number: {response['SequenceNumber']}")

if __name__ == "__main__":
    main()