import os, openai, key
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = key.OPENAI_API_KEY

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method=="POST":
        user = request.form["user"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))
    
    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__=="__main__":
    app.run(debug=True)