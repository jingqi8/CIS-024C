f = open("./static/20K.txt", "r")        # Open the file contains 20,000 English words
words = f.read()                # Read it into words varaible
f.close()
words_list = words.split()      # Convert into a List
words_dictionary = {}           # A Dictionary to store already corrected word for performance reason

def spell_check(sentence):
   result = ""
   correct_result = ""
   sentence_list = sentence.split()
   words_dictionary.clear()
   for word in sentence_list:
       word_lower = word.lower()
       if word[-1].isalpha() != True:   # Need to remove the non-alpha character    
          word_lower = word_lower[0:-1]

       word_back = auto_correction(word_lower)

       if word.istitle() == True:       # Need to change back the first upper case
          word_back = word_back.title()
       if word[-1].isalpha() != True:   # Need to add the non-alpha character at end
          word_back = word_back + word[-1]
       result = result + word_back + " "

       if len(words_dictionary) == 0:
          correct_result = "EXCELLENT JOB!\n\nTHERE IS NO ANY ERROR."
       else:
          correct_result = "HERE ARE THE CORRECTIONS:\n\n"
          for item in words_dictionary:
             correct_result = correct_result + item + " ---> " + words_dictionary[item] + "\n\n"

   return [result, correct_result]

# Correct the word based on the List of 20K words and the min edit distance
def auto_correction(word):
    if word in words_list or word.isdigit() == True:  # Check if this word is already in the Words List
        result = word
    elif words_dictionary.get(word) != None:          # Check if this word is already corrected before
        result = words_dictionary[word]
    else:
        distance = 9999             # Initial the distance
        result = ""                 # Initial the result
        for w in words_list:        # Calculate the min edit distance based on the 20K word List
            dis = edit_distance(word, w)
            if distance > dis:
                distance = dis
                result = w      
        words_dictionary[word] = result       # Store the correction for next time use

    return result

# Function to calculate the distance between 2 words
def edit_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

def add_word(word):
    if word.lower() in words_list:
       return 1 
    else:
       f = open("./static/20K.txt", "a+")       # Open the file contains 20,000 Eiglish words with "Append" mode
       f.write(word + "\n")          
       f.close()
       words_list.append(word)                  # Need to add this new word in to the list
       return 2

# ---------------------- Main Program -----------------------------------------------------
if __name__ == "__main__":
# === Sentence correction ==========
   sentence = raw_input("Please enter a Sentence: ")
   print spell_check(sentence)


