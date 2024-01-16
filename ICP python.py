def replace_with_pythons(sentence):
    sentence = sentence.replace("python", "pythons")
    sentence = sentence.replace("Python", "Pythons")
    sentence = sentence.replace("PYTHON", "PYTHONS")
    return sentence
user_input_sentence = input("Enter a sentence: ")
resulting_sentence = replace_with_pythons(user_input_sentence)
print("Converted Sentence:", resulting_sentence)
