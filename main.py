import os, openai, key
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = key.OPENAI_API_KEY

user = "Name 5 animals"

@app.route("/", methods=("GET", "POST"))
def openAI():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
)
    output = response['choices'][0]['text'].split("\n")
    return render_template("index.html", responses=output, user=user)


if __name__=="__main__":
    app.run(debug=True)