from flask import Flask, render_template, Response, request, redirect, url_for
import spaceAPI

app = Flask(__name__)
print(app)
@app.route('/')
def index():
    #return 'Method used %s' %request.method
    return render_template("index.html")

@app.route('/getPhoto', methods=['GET'])
def getPhoto():
    spaceAPI.getCoolPicture()
    return render_template("index.html")

app.run(debug=True)