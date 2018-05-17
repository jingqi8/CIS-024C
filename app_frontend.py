from flask import Flask, render_template, request, redirect
from app_spell_check import *
from app_dictionary import *

app=Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    text_inputs=""
    text_outputs=""
    error_outputs=""
    if request.method == 'POST':
       	text_inputs=request.form["text_area"]
	if request.form["action"] == "Check Spelling":
        	results = spell_check(text_inputs)
        	text_outputs = results[0]
        	error_outputs = results[1]
        elif request.form["action"] == "Maintenance":
                return redirect("/maintain")
        else:
               if len(text_inputs) != 0:
                	first_word = text_inputs.split()[0]
			text_outputs = dictionary_lookup(first_word)

    return render_template("index.html", text_input=text_inputs, text_output=text_outputs, error_output=error_outputs)

@app.route("/maintain", methods=['GET', 'POST'])
def maintain():
    word_inputs = ""
    duplicates = False
    adds = False
    if request.method == 'POST':
	if request.form["action"] == "Add Word":
                word_inputs=request.form["word_area"]
                if len(word_inputs) != 0:
                   result = add_word(word_inputs)
                   if result == 1:
                      duplicates = True
                   else:
                      adds = True
	elif request.form["action"] == "Back":
                return redirect("/")

    return render_template("/maintain.html", word=word_inputs, duplicate=duplicates, add=adds)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)

