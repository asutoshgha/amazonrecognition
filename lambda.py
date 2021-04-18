import json
import boto3

def lambda_handler(event,context):
    
    client=boto3.client("rekognition")
    s3=boto3.client("s3")
    fileObj=s3.get_object(Bucket="imagekilllo",Key="girlfu.jpeg")
    file_content=fileObj["Body"].read()
    response=client.detect_labels(Image={"S3Object":{"Bucket":"imagekilllo","Name":"girlfu.jpeg"}},MaxLabels=3,MinConfidence=70)
    print(response)
    return{ "statusCode":200,"body":json.dumps("hello from lambda") }
    
