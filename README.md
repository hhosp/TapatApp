# TapatApp  HOLA

[Descripcio del Projecte](descTapatApp.md)

[Requeriments Tècnics](reqTecTapatApp.md)

## Prototip 1

[Prototip 1](/charts/diagrama.mermaid)

[HTTP Request](HTTPRequest.md)<br>
[HTTP Response](HTTPResponse.md)

### Definició dels EndPoints

| Descripció  | End-point     | Method     |Tipus de petició|Parametres| 200| 400 | 404 |
| :---        |  :---        |  :---        |  :---         |  :---     |  :--- |  :--- |  :--- |   
| Obtenir dades d'un usuari  | /prototip1/getuser|GET | application/json   |  username (string) |  {   "email": "prova@gmail.com",   "id": 1,   "password":  "12345",   "user": "usuari1" } 200     | {"error":f"User '{username}' not found"} 400|  {"error": "Error inesperat", "details": str(e)} 404  | 

