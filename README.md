# AWS-LAMBDA
Este repositorio tiene en sí varios tutoriales de como crear diferentes tipos de funciones lambda. Desde simpes, incluso con Application Load Balancer, Ashynchronus invocations, CloudWatchEventws, S3 Event Notifications, EventSourceMappings, SQS, Environment Varialbes, X-Ray Tracing, VPC, Function perfornamce, External Dependecnies, CloudFormation,  Lambda Container Images, Versions.  


Al final lambda te permite programar sin srevidores en un montón de lenguajes muy populares.

Las funciones lambda pueden ser invocadas por varios serviciosde AWS; y que este Lambda responda a eventos, es decir: a Monbile/Iot Backends, StreamingAnalytics, DataProcessing, ...

En cuanto al procesamiento, es muy eficiente tener una lambda tirando ahí todo el rato; lo que pasa es que tiene un máximo de 15 minutos de runtime. Es decir, si tu programa supera los 15 minutos, un lambda no es el adecuado para runearlo.

1. Mi Primera Lambda: tiene el tutorial como para crear una lambda function de 'hello-world' en formato de blueprint. También explica el tema de los logs como se pueden ver reflejados en CloudWatch, los permisos relativos, el tema del Monitoreo como la configuración de la capacidad de memoria de la función lambda como el timeout. 

2. synchronous_invocations: es decir, hay ciertos momentos donde nosotros podemos estar esperando un resultado por mediod de una call por ejemplo, y este resultado, venga en un momento dado en un formato. 

    Dicho de otra manera: el cliente puede invocar una API GATEWATY y este un 'proxy' llamando a un 'Lambda'. Esta fnción puede ejecutar una operación y  mandar la respuesta primero al API GATEWAY y luego este al cliente. 

    Bien, pues el cliente somos nosotros. 

    Las formas en las que se puede percibir esta operación en AWS son: 
    1. User invoked: 

    - ElasticLoadBalancer
    - Amazon API Gateway
    - CloudFront
    - S3 Batch

    2. Service Invoked: 
    - Amazon Cognito
    - Step Functions

    Nosotros no vamos a tocar nada de ello en ese readme, simplemente vamos a llamar a la Lamdbda por medio del CLI del cloud.

3. aplication_load_balancer: 

A veces quizas como usuario te parece exponer la funcion lamnda por medio de un endpoint HTTP(S), para ello tienes que tuilizar un Application Load Balancer / ALB, o un API Gateway. 

Nosotros lo haremos con un ALB.

El ALB convierte el HHTP request a Lambda, por medio de una transformación a JSON. 

En el JOSN nos aparecera: 
1. Información del ELB
2. El método de HTTP Method
3. El query string conlos parametros en formato de KEY value
4. Los headers como key value pairs. 
5. EL body, con indicaciones API propias (POST, PUT..) y si hay necesidad de hacer una decodificación 64. 

Paralelamente nuesgtro lambda, tambien devuelve un JSON, el ALB lo convierte a un HTTP. 

**Multi-header values**, si tenemos un cliente comnuicandose con nuestro ALB, si nos manda un cliente muchos strings, es decir muchos parametros, podemos convertir muchos parametros que sean de la misma familia en arrays.
