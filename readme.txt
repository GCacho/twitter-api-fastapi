#API que simula a la aplicación **Twitter** 

###Para instalar los requerimientos de la aplicación: 
    - pip install -r requirements.txt

#Para correr el framework y la documentación dinámica.
    - uvicorn main:app --reload  --> Corre el server.
    - 127.0.0.1:8000/docs  --> Abrir la documentación dinámica.

### En este ejemplo guardamos a los usuarios en archivos .json, lo ideal
    sería crear una base de datos y hacer una conexión para almacenarlos a través de SQL,
    pero eso será pa la otra.