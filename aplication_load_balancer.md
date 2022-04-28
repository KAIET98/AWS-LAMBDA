

Esta vez no es necesario haber hecho la primera formación de este repositorio Github. 

1. Creamos una función nueva 

Seleccionamos "author from scratch", 
nombre:

```
lambda-alb-tutorial
```
Como runtime escogemos el Python 3.8, o el más nuevo.

En cuanto al role seleccionamos el " Crate a new role with basic Lambda permissions"


Clickamos en Create function.

Si probamos nuestra función recientemente creada, le vamos a dar nomrbe al evento: 

```
DemoEventTutorial
```

y lo testeamos. Bien esto es lo que necesitamos obtener.

2. EC2: 

    Vamos a la pestaña de EC2, y nos posicionamos en el apartado de ALB

    Atención, a la hora de hacer este tutorial, si tienes otro ALB corriendo, y si estas en **Free tier**, ten en cuenta que por tener 2 ALBs AWS te va a cobrar por lo que tu decidiras que hacer. 

    1. Creamos el load balancer:

    Seleccionamos el application load balancer, clickamos en 'Create'. 

    2. En el nombre ponemos: 



    ```
    demo-alb-lambda
    ```

    En Cuanto al schema, es un "Internet Facing" load balancer, peusto que va  adar de vuelta reuqest de clientes usando Internet, NO UN IP PRIVADO.

    3. Listeners and routing: 

    Como es un HTTP, va a escuchar desd eel Puerto: 80

    4. Network Mapping: 

    Va a estar sobre 3 zonas de disponibilidad. 

    5. Security Group: 

    Vamos a crear un nuevo grupo de seguridad: 

        1. Security Group name: 

            ```
            load-balancer-wizard-1
            ```

        2. Description: 

            ```
            Este es un grupo de seguridad para poder crear el lambda con el ALB
            ```

        
        3. Inbound Rules: 

            -Type: HTTP
            Port: 80
            Source type: Anywhere-IPv4. 

            -Type: HTTPS
            Port: 80
            Source type: Anywhere-IPv4.  

        4. Creamos. 

    6. Target Group: 

    Una vez creado el ALB, tenemos que poder aplicarle este ALB a algo, a nuestra lambda. 

        1. Entramos en Target Groups, debajo de Load Balancers. 

        2. Create a Target Group

        3. Basic configuration

            - Choose a target type: Lambda
            - Name: 

            ```
            tg-lambda
            ```
            - HealthCheck: Nope

            Next. 

        4. Seleccionamos la lambda que acabamos de crear, y seleccionamos en ete caso "Version".

        5. Create a target group. 

3. Volvemos a Lambda: 

Seleccionamos el grupo de seguridad que acabamos de crear, con todo el jardín por detrás. Ten en cuenta eque en Listeners and routing, tendras que escoger el target group que acabas de crear es decir: 

```
tg-lambda
```


Vamosa modificar el coding, vamos a printear el evento, para ver que se pasa a la lambda cuando el ALB se invoca.

Pasamos de: 
```
import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

```
A
```
import json

def lambda_handler(event, context):
    
    
    print(event)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    
```
Nos devolvera un log event de este tipo: 

```
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
```

4. Output ALB:

Ahora tengo que esperar a que el ALB termine de 'provisionar', pues si vamos a la pestaña de ALB, veremos que esta 'Provisioning'. Bueno pasará de Provisioning, a Active. 

Si copiamos el DNS, y lo pegamos en una pestaña de Google, se nos va a descargar un fichero, que si abrimos en el block de ntoas vamos a obtener la respuesta de 

```
'Hello from Lambda!'
```

5. Cambio de tipo de output Lambda a ALB: 

Lo suyo sin emabrgo, seria que tuviesemos esa respuesta por pantalla HTML cuando ejecutamos la lambda, por lo que en si en si, tras mirar la documentación oficial nos damos cuetna que el formato sería: 


```
{
    "statusCode": 200,
    "statusDescription": "200 OK",
    "isBase64Encoded": False,
    "headers": {
        "Content-Type": "text/html"
    },
    "body": "<h1>Hello from Lambda!</h1>"
}

```
Por lo que lo copiamos, nos posicionamos en la Lambda, en el code y  en el return ponemos eso, pasamos de: 

```
import json

def lambda_handler(event, context):
    
    
    print(event)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    
    

```
a
```
import json

def lambda_handler(event, context):
    
    
    print(event)
    
    
    return {
        "statusCode": 200,
        "statusDescription": "200 OK",
        "isBase64Encoded": False,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": "<h1>Hello from Lambda!</h1>"
        }
    
    
```

le damos a deploy y luego a test. 

Volvemos a la pestaña con el enlace de DNS de ALB que teniamos antes y lo refrescamos, nos saldrá el output del lambda.

6. ¿Cuál es el evento del lambda?

Vamos a mirar quét ipo de evento se nos está ejecutando en el Lambda, por lo que volvemos al menú de lambda y lo miramos, Monitor>Logs>RecentInvocations y pillamos la primera línea, que es la última Invocation. 

(Si quieres saber más información sobre como obtener información sobre tus logs más en profundidad, visita la carpeta de CloudWatchPython, y mira los diferentes scripts que hay. )

Dentro de ese link, podemos sacar muchisima información, incluso la IP pública... 


7. Multi header support

Si volvemos a nuestros target groups, en EC2, podemos modificar atributes, dentro de 'ATRIBUTES', lo que vamos a hacer es modificar el apartado de 'Multi value headers', y ponerlos en Enabled. 

Vamos a ponerlo a prueba. Podemos incluirle en la url del DNS como name = foo y name = bar, y esto se vera reflejado luego en los logs de Cloudwatch. 

:)
