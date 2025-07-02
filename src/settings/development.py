from .base import *

DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '13.233.198.220',  # EC2 का public IP
    '51.21.201.93',
    'ec2-51-21-201-93.eu-north-1.compute.amazonaws.com',  # EC2 का DNS
]
