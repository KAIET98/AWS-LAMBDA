

Tras haber hecho el tutorial nº1 de este repositorio seguimos adelante. 

Como nos hemos comunicado con el servicio de AWS hasta ahora, podemos hacerlo por medio de la cloudshell

1. Vemos las lambdas que tenemos 

´´´
aws lambda list-functions
´´´

Además, puedo añadir la region para obtener las funciones propias a dicha region: 

´´´
aws lambda list-functions --region us-east-1
´´´


2. Vamos a realizar una llamada synchrona por mediod e linux: 

Para ello vamosa teclear lo siguiente: 

```
aws lambda invoke --function-name NOMBRE_FUNCION --cli-binary-format raw-in-base64-out --payload '{"key1": "value1", "key2": "value2", "key3": "value3" }' --region <REGION> response.json

```

Modificamos la sentencia con la region en la que estemos, junto al nomrbe de la funcion


```
aws lambda invoke --function-name demo-lambda-world --cli-binary-format raw-in-base64-out --payload '{"key1": "value1", "key2": "value2", "key3": "value3" }' --region us-east-1 response.json
```
Si todo va bien, deberiamos de recibir una respuesta como esta

```
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```
Podemos entrar a la respuesta poniendo

```
cat response.json
```
Y la respuesta que obtenemos es efectivamente:

```
"value1"
```

Que coincide con la configuración del tutorial anterior.

:).
