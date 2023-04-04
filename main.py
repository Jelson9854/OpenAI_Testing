import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

user = "How do I get good grades in Software Development"

@app.route("/")
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