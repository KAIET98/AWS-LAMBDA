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


