# XalDigitalChallenge
DE Challenge
Desarrollado por Eduardo Marquez

La imagen de "centosxd" es una imagen modificada de centos para tener todas las utilerías y configuraciones necesarias para este Challenge, 
se puede encontrar en mi repositorio de dockerhub "nose238/centosxd", por lo que lo único necesario para poner este ejercicio "up and running"
es ejecutar el docker-compose.yml y tener una conexión a internet para bajar la imagen.

Las rutas para la API son: 
   * GET: http://localhost/getElements que obtiene todos los registros de la BD postresql. En esta se pueden hacer filtros mediante la utilización de
    los parámetros first_name, last_name, city, state y deparment, además de fijar un límite de registros obtenidos. (no es obligatorio el uso de
    todos los parámetros para que la API funcione.)
    Algunos ejemplos: 
    http://localhost/getElements?first_name=Maryann
    http://localhost/getElements?limit=10
    http://localhost/getElements?state=LA&department=Marketing&limit=1
    
   * POST: http://localhost/insertElement en la cual se tiene que enviar en el body un JSON válido para insertarlo en la base de datos postgresql
   Por ejemplo: 
   {"first_name": "Eduardo", "last_name": "Marquez", "company_name": "Info", "address": "Miguel Hidalgo", "city": "Coyoacan", "state": "MX", "zip": "04260", 
   "phone1": "558-546-5128", "phone2": "", "email": "nose238@hotmail.com","department": "CYC"}
