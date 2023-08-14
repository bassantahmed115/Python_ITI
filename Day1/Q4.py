word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "}{"
word6 = "so"
word7 = "far?"
word7_modified = word7.replace("?", "!")
sentence = word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7

# Display the sentence in C language format
print("printf(\"{}\\n\");".format(sentence))
