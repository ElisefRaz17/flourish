from flask import Flask, render_template, send_from_directory



app = Flask(__name__)





@app.get("/")
def home():
     return render_template('home.html')

@app.get("/signup")
def signup():
     return render_template('signup.html')

@app.get("/login")
def login():
     return render_template('login.html')

@app.get("/howitworks")
def howitworks():
     return render_template('howitworks.html')

@app.get("/getstarted")
def getstarted():
     return render_template('getstarted.html')

@app.route('/chooseChannel', methods=['GET'])
def chooseChannel():
    channels = ['Personal', 'Work', 'School', 'Family','Relationships']
    return render_template('chooseChannel.html', channels=channels)

@app.route("/<path:name>")
def download_file(name):
    return send_from_directory(
        "static/", name, as_attachment=True
    )



if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)