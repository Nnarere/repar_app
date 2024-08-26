DESCRIPCIÓN DEL PROYECTO

REPAR es una aplicación desarrollada para encontrar información de vehículos utilizando el código de su patente o el número VIN

TECNOLOGÍAS UTILIZADAS
Frontend: Bootstrap.
Backend: Flask y MySQL.

FUNCIONALIDADES

Autenticación:
Página de inicio de sesión con validación y encriptación de contraseñas. Mensaje de confirmación para usuarios registrados exitosamente.

Búsqueda de Vehículos: 
Página para buscar vehículos por placa patente y número VIN.

Gestión de Vehículos: 
Formularios para añadir nuevos vehículos a la base de datos.

Listado de Vehículos:
Página que muestra todos los vehículos añadidos.

Resultados de Búsqueda:
Páginas para mostrar los resultados de las búsquedas específicas por placa patente y número VIN.

CONSIDERACIONES TÉCNICAS

Para la búsqueda de vehículos no se utilizó el método LIKE de MySQL, asumiendo que las búsquedas serían específicas y no parciales.
Todos los métodos y funcionalidades han sido probados, y hay datos de muestra cargados para referencia.

INSTALACIÓN
Para ejecutar la aplicación en sus computadoras, siga estos pasos:

1. Instalar MySQL Server y Python: Asegúrese de tener MySQL Server y Python instalados en su sistema.

2. Instalar pipenv:

    En Windows: pip install pipenv
    En macOS: pip3 install pipenv

3. Instalar dependencias:

    pipenv install flask pymysql flask-bcrypt

4. Ejecutar la aplicación:

    python server.py

NOTA ADICIONALES

Asegúrese de configurar correctamente la conexión a la base de datos MySQL en su archivo de configuración de Flask (debe cambiar el usuario y contraseña del archivo mysqlconnection.py de la carpeta config en flask_app, con el usuario y contraseña de su MYSQL).