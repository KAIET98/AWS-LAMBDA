from tkinter import E
import boto3
import json

#Le pones la zona en la que tienes creadas los recursos de CloudWatch

AWS_REGION = "us-east-1"

client = boto3.client('logs', region_name=AWS_REGION)


# Extraemos los logs.
response = client.describe_log_groups()

#print(json.dumps(response, indent=4))

#Los guardamos en un formato manejable

body = response['logGroups']

#print(body)
#En el archivo desgranaje_cloud_role.py, hemos creado un anidaje de diccionarios para sacar la información de
#este tipo de outputs que nos da AWS, lo metemos en una función:

def desgranaje(body):
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



#Aplicamos el conocimiento a lo que tenemos, es decir, si lo qeu nos da es un diccionario, 
#lo pasamos por la formula:

if isinstance(body, dict):

    desgranaje(body)

    
 
else: 

    #si no lo es es que es una lista, pero si l alista tiene un diccionario dentro, tambien lo hacemos pasar.

    for each_line in body:


        #print(each_line)

        if isinstance(each_line, dict):

            desgranaje(each_line)

        else: 

            print(each_line)


#Este conocimiento también lo metemos en una función 

def desgranaje_log_cloudwatch(elemento):

    if isinstance(elemento, dict):

     desgranaje(elemento)

    
 
    else: 

        #si no lo es es que es una lista, pero si l alista tiene un diccionario dentro, tambien lo hacemos pasar.

        for each_line in elemento:


            #print(each_line)

            if isinstance(each_line, dict):

                desgranaje(each_line)

            else: 

                print(each_line)

print('\n', ' ################################# ', '\n ')

#desgranaje_log_cloudwatch(body)           





#---------- FILTRADO DE LOG GROUPS-----------


print('\n AHORA CON EL FILTRADO: ############')

'''
Queremos ver el que acabamos de crear en el tutorial de ALB
'''

response = client.describe_log_groups(
    logGroupNamePrefix='/aws/lambda/lambda-alb-tutorial'
)

#print(response)

for keys, value in response.items():

    print('Key: ', keys, ' || value ', value, '\n')


#La metadadta:
#  

print('                         LA METADATA               ')

body = response['ResponseMetadata']

desgranaje_log_cloudwatch(body) 

#Log groups

print('                         LOSGROUPS              ')
body = response['logGroups']

desgranaje_log_cloudwatch(body) 