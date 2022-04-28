

from xml.dom import InvalidStateErr
import boto3
from numpy import isin
iam = boto3.resource('iam')

def get_policy_body(arn, version_id = None):

    if version_id:

        version = iam.PolicyVersion(arn, version_id), 

    else: 

        policy = iam.Policy(arn)

        version = policy.default_version

    return version.document

POLICY_ARN = "arn:aws:iam::070307590085:policy/service-role/AWSCodePipelineServiceRole-us-east-1-CodeC-EC2-S3"


body = get_policy_body(POLICY_ARN)

#print(body.keys())

#print(body['Statement'][0]['Condition'])

body = {'requestContext': {'elb': {'targetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:070307590085:targetgroup/tg-lambda/20de418ff8a7c880'}}, 'httpMethod': 'GET', 'path': '/', 'queryStringParameters': {}, 'headers': {'accept-encoding': 'gzip', 'host': 'example.com', 'user-agent': 'Go-http-client/1.1', 'x-amzn-trace-id': 'Root=1-626a7da4-252f362c3a2df46c476c7af4', 'x-forwarded-for': '45.148.10.81', 'x-forwarded-port': '80', 'x-forwarded-proto': 'http'}, 'body': '', 'isBase64Encoded': False}



for element in body.keys():

    print('\n ', 'Elemento: ', element, ' :: \n ')

    
    if isinstance(body[element], dict):

       for k, v in body[element].items():
           
           print('\t KEY PRINCIPAL: ', k,' || value:  ',v, ' ')

           if isinstance(body[element][k], dict): 

               for subkey, subvalue in body[element][k].items():

                   print(' \n', '\t \t SUB-KEY PRINCIPAL: ', subkey, ' ', subvalue)

                   if isinstance(body[element][k][subkey], dict):

                       for susubkey, subsubvalue in body[element][k][subkey].items():

                           print(' \n', '\t \t \t SUBSUB-KEY PRINCIPAL: ', susubkey, ' ', subsubvalue)

               #print('DIC')

    else: 

        print('\t \t Su elemento: ', body[element])

           


