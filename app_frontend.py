from flask import Flask, render_template, request
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
        else:
                first_word = text_inputs.split()[0]
		text_outputs = dictionary_lookup(first_word)

    return render_template("index.html", text_input=text_inputs, text_output=text_outputs, error_output=error_outputs)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, debug=True)

