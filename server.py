from flask import Flask
from flask import request
# from playsound import playsound

server = Flask(__name__)

@server.route("/")
def index(methods = ["GET", "POST"]):
    print(request.method)
    if request.method == "POST": # fix this 🙏🙏🙏🙏
        print("going to play the sound located at:", sound_file)
        return

    if request.method == "GET":
        with open("index.html") as f:
            content = f.read()
            print(content)
            return content
        


server.run("0.0.0.0", "3000", debug=True)