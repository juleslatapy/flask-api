from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''
    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Hello World</title>
        <style>
            body {
                background-color: blue; /* Couleur de fond rouge */
                color: white; /* Couleur du texte */
                text-align: center; /* Centre le texte */
                font-family: Arial, sans-serif; /* Police */
                padding: 50px; /* Ajoute du padding */
            }
        </style>
    </head>
    <body>
        <h1>Hello World! v1.0.0.6</h1>
    </body>
    </html>
    '''