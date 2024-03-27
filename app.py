from flask import Flask 
app = Flask (__name__)

@app.route ('/')
def hello_geek():
  return '<h1>hola</h1>'

if __name__ == "main":
  app.run(debug = True)
