from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline! DIVYANSHU SINGH is here!\n Change: Checking if the pipeline is working fine."
    #return "Hello from CI/CD Pipeline!, my sapid is 500122856"

app.run(host="0.0.0.0", port=80)
