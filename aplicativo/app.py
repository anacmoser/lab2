from flask import Flask
app=Flask(__name__)
@app.route('/')
def olamundo():
    return "Olá Mundo!"
if __name__ == '__main__':
    app.run(debug=True)
