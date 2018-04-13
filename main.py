
import sys
from sorthelper import sortNumbers

if __name__ == "__main__":
    l1 = []
    total = len(sys.argv)
    if total < 2:
        print "Please enter at least 1 argument. Try again!" # Make sure there is at least 1 parameter   
    else:
        for i in range(1, total):
            try:
                l1.append(int(sys.argv[i]))                  # Form a List
            except:
                print "You must use Integer. Please try again!" # If input is not an Integer, then exit
                exit()
            
        print "Your input is: ", l1
        print "Your output is: ", sortNumbers(l1)