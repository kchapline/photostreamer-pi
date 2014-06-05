import ConfigParser
from boto.s3.connection import S3Connection
from boto.s3.key import Key

def connect():
    config = ConfigParser.ConfigParser()
    config.readfp(open('config.cfg'))
    aws_access_key = config.get('s3', 'access_key')
    aws_secret_key = config.get('s3', 'secret_key')
    aws_s3_bucket = config.get('s3', 'bucket')
    conn = S3Connection(aws_access_key, aws_secret_key)
    bucket = conn.get_bucket(aws_s3_bucket)
    return bucket

def save(src, dest):
	bucket = connect()
    s3 = Key(bucket)
    s3.key = dest
    s3.set_contents_from_filename(src)
    return s3