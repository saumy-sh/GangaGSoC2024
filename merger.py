import sys
arg = sys.argv[1] #takes input of merged file which contains merged data of counts of "it" from subjobs
file = open(arg,"r")
text = file.read()
words = text.split(" ")
counter = 0
for text in words:
#this is to obtain integers from strings,i.e.,from "#\n1\n\n#" to "1"
    text = text.split("\n")
    if len(text) > 1:
        text = text[1]
    else:
        text = 0
####################################################################
    try:
        int(text)
        counter += int(text)
    except ValueError:
        pass
print(counter)