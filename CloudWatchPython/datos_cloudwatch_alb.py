


import sys
import boto3



dic = {'requestContext': {'elb': {'targetGroupArn': 'arn:aws:elasticloadbalancing:us-east-1:070307590085:targetgroup/tg-lambda/20de418ff8a7c880'}}, 'httpMethod': 'GET', 'path': '/', 'queryStringParameters': {}, 'headers': {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'accept-encoding': 'gzip, deflate', 'accept-language': 'es-ES,es;q=0.9', 'cache-control': 'max-age=0', 'connection': 'keep-alive', 'host': 'demo-alb-lambda-502423307.us-east-1.elb.amazonaws.com', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36', 'x-amzn-trace-id': 'Root=1-626a739c-2b899e7f05f2d5c1709898e1', 'x-forwarded-for': '188.87.249.118', 'x-forwarded-port': '80', 'x-forwarded-proto': 'http'}, 'body': '', 'isBase64Encoded': False}

# ISP INTERNET SERVER PROVIDER

for key in dic.keys():

    print(dic[key])
'''

for element in dic.values():
    if isinstance(element, dict):
       for k, v in element.items():
           print(k,' ',v)

'''