import json
from difflib import get_close_matches

data = json.load(open("./static/data.json", "r"))
def dictionary_lookup(word):
    msg = ""
    close_w = ""
    out = ""
    w = word.lower()
    if w in data:
        msg = data[w]
    else:
        if len(get_close_matches(w, data.keys())) > 0:
           close_w = get_close_matches(w, data.keys())[0]
           msg = data[close_w]

    if msg == "":              # Nothing found or matched
        return "THE 1'ST WORD DOESN'T EXIST OR MATCH ANY CLOSED WORD. PLEASE DOUBLE CHECK!"
    else:
        if close_w != "":      # Found the closed match
           out = "WE FOUND THE MOST CLOSED WORD: " + close_w + "\n\n"
        else:                  # Found in the dictionary
           out = "THE MEANING OF THE 1'ST WORD: " + word + "\n\n" 
        if type(msg) == list:
           for item in msg:
               out = out + "-" + item + "\n\n"
        else:
           out = out + msg
        return out

# ---------------------- Main Program -----------------------------------------------------
if __name__ == "__main__":
   word = ""
   while word != "exit":
      word = raw_input("Enter a Word ('exit' to End): ")
      print dictionary_lookup(word)
        
