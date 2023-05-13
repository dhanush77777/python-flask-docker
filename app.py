from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "Dockerizing the flask app v1"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int("3000"),debug=True)
