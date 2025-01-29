# TapatApp

[Descripcio del Projecte](descTapatApp.md)

[Requeriments Tècnics](reqTecTapatApp.md)

## [Prototip 1](/charts/diagrama.mermaid)

[HTTP Request]()
[HTTP Response](HTTPResponse.md)

### Definició dels EndPoints

| Descripció  | End-point     | Method     |Tipus de petició|Parametres| resposta|
| :---        |  :---        |  :---        |  :---         |  :---     |  :--- | 
| Obtenir dades d'un usuari  | /prototip1/getuser|GET | application/json   |  username (string) |  {   "email": "prova@gmail.com",   "id": 1,   "password":  "12345",   "user": "usuari1" } 200     | |
| Obtenir dades d'un usuari  | /prototip1/getuser|GET | application/json   |  username (string) |  {"error":f"User '{username}' not found"} 400| |
| Obtenir dades d'un usuari  | /prototip1/getuser|GET | application/json   |  username (string) | {"error": "Error inesperat", "details": str(e)} 404| |
