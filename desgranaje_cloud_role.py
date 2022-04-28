

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




for element in body.keys():

    print('\n ', 'Elemento: ', element, ' :: \n ')

    
    if isinstance(body[element][0], dict):

       for k, v in body[element][0].items():
           
           print('\t KEY PRINCIPAL: ', k,' || value:  ',v, ' ')

           if isinstance(body[element][0][k], dict): 

               for subkey, subvalue in body[element][0][k].items():

                   print(' \n', '\t \t SUB-KEY PRINCIPAL: ', subkey, ' ', subvalue)

                   if isinstance(body[element][0][k][subkey], dict):

                       for susubkey, subsubvalue in body[element][0][k][subkey].items():

                           print(' \n', '\t \t \t SUBSUB-KEY PRINCIPAL: ', susubkey, ' ', subsubvalue)

               #print('DIC')

           


