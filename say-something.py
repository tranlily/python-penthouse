# Sample output:
# Say something: <user input>
# Say something: <user input>
# Say something: <user input>
# Say something: \end 
# <user input>. <user input?> user input.
# 
def sentence_maker(phrase):
    question = ("who", "what", "when", "where", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(question):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while (True):
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else: 
        results.append(sentence_maker(user_input))
        continue

print(" ".join(results))