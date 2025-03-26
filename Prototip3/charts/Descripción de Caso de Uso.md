# Descripción de Caso de Uso (Plantilla)

| \[UC2\] | \[Consulta Child\] |  |  |
| :---- | :---- | :---- | :---- |
| **Descripción** | El Tutor o el Cuidador consultan la información de un niño registrado en el sistema. Este caso de uso permite obtener información relevante del niño, como datos personales y registros previos. |  |  |
| **Actores** | Tutor, cuidador |  |  |
| **Pre condiciones** | El usuario debe haber iniciado sesión en el sistema (UC1). El niño debe estar registrado en la base de datos. |  |  |
| **Post condiciones** | Se muestra la información del niño al usuario. El sistema registra la consulta para auditoría. |  |  |
| **Secuencia Normal** | **\#** | **Acción (actor)** | **Reacción (sistema)** |
|  | 1 | El Tutor o Cuidador solicita consultar la información de un niño.	 | \[lo que responde el sistema\] |
|  | 2 | El Tutor o Cuidador ingresa la identificación del niño.	 | \[siguiente respuesta del sistema\] |
|  |  | Si el niño existe, el sistema recupera y muestra la información asociada.	 | Se muestra la información en pantalla.  |
|  | ... |  | ... |
|  | n |  | ... |
| **Excepciones** | \# | **Acción (actor)** | **Reacción (sistema)** |
|  | p | Si el niño no está registrado en la base de datos.	 | El sistema muestra un mensaje de error y no permite continuar. |
|  | q | Si hay un problema con la conexión a la base de datos.	 | El sistema informa el error y sugiere intentarlo más tarde. |
| **Rendimiento** | El sistema deberá mostrar la información del niño en un máximo de 2 segundos después de la solicitud. |  |  |
| **Frecuencia** | Este caso de uso se espera que se lleve a cabo una media de 10 veces al día. |  |  |
| **Importancia** | Importante |  |  |
| **Urgencia** | Inmediatamente, ya que la información del niño puede ser crucial |  |  |
| **Comentarios** | … |  |  |

