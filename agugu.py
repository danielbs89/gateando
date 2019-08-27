import requests
url = 'https//:worldview.stratfor.com'
respuesta = requests.get(url)
contenido = respuesta.content
x = ' duque '
x in contenido
