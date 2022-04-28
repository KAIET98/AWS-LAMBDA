

Vamos a crear nuestra primera lambda super simple. 

## Creación de Lambda


AWS nos da varias funcionalidades a la hora de crear las lambdas: 

1. Author from scratch: Es decir, que lo creamos nosotros mismos. 

2. Use a blueprint: al final, quiere decir que lancemos un proceso con un sample code y con unas configuraciones que ya vienen dadas. 

3. Container image: seleccionamos un container, y lo ejecutamos desde nuestra funcion.


1. En nuestro caso vamos a proceder a hacerlo en "Use a blueprint", por lo que filtraremos el "Blueprint", con: 

```
hello-world
```

Con ello, seleccioaremos la función de python correspondiente. Y le damos a "Configure"

2. Nombre: 

```
demo-lambda-world
```

En cuanto al 'Execution role', vamos a seleccionar el: 

```
Create a new role with basic Lambda permissions
```
Tal cual nos importa, lo tomamtos. 


3. Testeamos la función: 

Vamos a testearla, clickamos en "Test", y le decimos que 

- Test Event action: Create new event

- Nombre: 
```
Demo-Helloworld-Event
```

Una vez que hemos hecho eso, vamos a probar la función, clicamos en Test.

4. Partes importantes del menú: 

-- En nuestra función en 'Configuration', se nos despliega una barra a la izquierda que nos permite ejecutar diferentes funcionalidades con la lambda. 

Una de las más importantes es: 

- General Configuration: 

Dentro de este menú tenemos una caracterísitca muy importante: 'Run Memory', es decir, podmeos tener una memoria entre 128 MB hasta 10240 MB; cuanta más memoria tengas podras construir más. 

'Timeout', podemos configurar un Timeout a nuestro gusto, pero con el **límite máximo de 15 minutos** como hemos comentado anteriormente. 


Finalmente, el execution role, es decir, podemos optar por una que cree by default o crear una nueva, desdee AWS policies. 

Nosotros djearemos la de by defaulta para este tutorial. 


-- En 'Monitoring', podemos ver ue pasa con la lambda, cuantas veces se llama, cuanto dura, cuantos errores o successes tenemos y tal. Bien el monitoreo general, los logs y tal. 

Podemos refreshear y ver los logs. Si clickamos en una en específico, nos manda a CloudWatch (Si no sabes que es y quieres saber más sobre ello, chequea este tutorial: https://github.com/KAIET98/AWS-CLOUDWATCH).

Esto se posibilita porque si, accedemos a 'Permissions', veremos que tenemos un rol, que se enlaza con CloudWatch, este rol se ha creado por medio de Lambda. Si clicckamos en el nos llevará a IAM, a su rol correspondiente, y si miramos el policy, en el policy summary, versa que tenemos acceso a escribir en CloudWatch.


-- Menu general de Lambda, podemos ver el 'Runtime settings', nos dhace un breve resumen de lo que estamos lanzando: por ejemplo: 
1. Python 3.7
2. Handler: lambda_function.lambda_handler, que viene a decir que, esta llamando la función con el nombre de 'lambda_handler' y lo que llama es 'lambda_function'. 




