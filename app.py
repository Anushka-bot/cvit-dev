from flask import Flask, render_template, request, redirect, url_for
import subprocess,os
from werkzeug.utils import secure_filename

app=Flask(__name__)

url="https://xyz.com/"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/process", methods=['POST'])
def process():
    if request.method=="POST":
        f=request.files['video']
        file_name = secure_filename(f.filename)
        filepath = os.path.join("static/",file_name)
        f.save(filepath)
        if f:
            path = '@'+ filepath
            link=f'{url}lipreading'
            command = f'curl -X POST -F "video={path}" {link}'
            print(command)
            #subprocess.call(command.format(path,link),shell=True)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)

