from flask import Flask, render_template, request, redirect, url_for
import subprocess

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/input")
def input():
    return render_template("input.html")

@app.route("/process", methods=['POST'])
def process():
    if request.method=="POST":
        path=request.form['path']
        name=request.form['name']
        if path:
            path = '@'+path
            if not name:
                name="output.txt"
            command = 'curl -X POST -F "video={}" -F "name={}" {}'
            link='ng-rok-link/lipreading'
            subprocess.call(command.format(path,name,link),shell=True)
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)
