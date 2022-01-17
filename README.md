# Json Web Token 
El Json Web Token es una forma de propagar una sesiòn o credencial dentro de una aplicaciòn.

Su estructura general es ```header.payload.signature```.

## Uso en Python
- Importamos la libreria con ```import jwt```.
- Debemos tener una **SECRET_KEY** en nuestras variables del entorno y un tiempo para marcar la **expiraciòn**.

```python
token = jwt.encode({"payload":"todo nuestro payload","time":"ts"},
                    SECRET_KEY,
                    algorithm="HS256")
```