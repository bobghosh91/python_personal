def sentence_maker(phrase):

    interrogative = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogative):
        return "{}.?".format(capitalized)
    else:
        return "{}.".format(capitalized)


print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))