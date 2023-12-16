from flask import Flask,render_template,request
app = Flask(__name___)

@app.route('/')
def index():
  return render_template('waterWeb.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080)
