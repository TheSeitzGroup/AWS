import boto3
      
AWS_ACCESS_KEY_ID="ALPHANUM"
AWS_SECRET_ACCESS_KEY="ALPHANUM"
AWS_SESSION_TOKEN="REDICULOUSLY-LONG-STRING"

session = boto3.session.Session(
  aws_access_key_id=AWS_ACCESS_KEY_ID,
  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, 
  aws_session_token=AWS_SESSION_TOKEN)

# proceed to create clients / resources from the session 
# for example, an s3 client:
 
# client = session.client('s3')      
