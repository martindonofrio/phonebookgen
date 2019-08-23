# phonebookgen
Generador de libreta de contactos para telefonos Yealink

+Aclaraciones

Se penso para ser usado en una implementacion de Freepbx, con el objetivo de obtener todas los numeros de extensiones de la implementacion con sus respectivos nombre.
Con esta información, armar el archivo XML necesario para poder importarlo (mediante aprovisionamiento) a los telefonos Yealink T19, T2X, T4X, etc.

+Instalacion de dependencias

yum install epel-release

yum install python-pip

pip install --upgrade pip

pip install sqlalchemy

pip install xml4h


+Logging

El resultado de la ejecucion del script lo podran ver en /var/log/phonebook_gen.log



