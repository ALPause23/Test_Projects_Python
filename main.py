from datetime import datetime as dt
import time
import json
from flask import Flask, request, render_template

app = Flask(__name__) #create new web-application

def load_chat():
    with open("chat.json", "r") as json_file:
        data = json.load(json_file) # load data from json_file in variable "data"
        return data["messages"] # cat masseges from data


all_messages = load_chat()


def save_chat():
    data = {"messages": all_messages} # json want use "{}" else it not found data
    with open("chat.json", "w") as json_file:
        json.dump(data, json_file)  #save dats in file


@app.route("/chat")
def display_chat():
    return render_template("form.html")

@app.route("/")
def index_page():
    return "Welcome to my messager"

@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}

#http://127.0.0.1:5000/send_message?name=Nick&text=Hi
@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]

    if len(sender) in range(3, 100):
        result_sender = "Sender_Lenght: OK \n"
    else:
        result_sender = "Sender_Lenght: ERROR \n"

    if len(text) in range(1, 1000):
        result_text = "Text_Lenght: OK \n"
    else:
        result_text = "Text_Lenght: ERROR \n"

    if result_sender == "Sender_Lenght: OK \n" and result_text == "Text_Lenght: OK \n":
        add_message(sender, text)
        save_chat()
    print(result_sender + result_text)
    return result_sender + result_text

@app.route("/info")
def num_message():
    num = len(all_messages)
    return f"number of messages: {num}"

def add_message(sender, text):
  all_messages.append({
      "sender": sender,
      "time": dt.now().strftime("%d.%m.%Y %H:%M"),
      "text": text
  })

add_message("Mike", "Test")

app.run()   #Starting application



