from flask import Flask 


app=Flask(__name__)

@app.route('/')

def index():
    return "ECHO FROM APP.PY"

if __name__ == "__main__":
    app.run()


