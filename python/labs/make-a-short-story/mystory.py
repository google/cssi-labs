# Create a function for adjectives so I don't repeat myself in prompts.
def get_adjective():
    return raw_input("Give me an adjective: ")

def get_noun():
    return raw_input("Give me a noun: ")

def get_verb():
    return raw_input("Give me a verb: ")

adjective1 = get_adjective()
noun1 = get_noun()
verb1 = get_verb()
adjective2 = get_adjective()
noun2 = get_noun()
verb2 = get_verb()

# Use parentheses so Python will "know" the string has multiple lines
print ("At CSSI we were all " + adjective1 + " when a " + noun1 +
    " fell through the ceiling. See-Mong tried to " + verb1 + " it but it " +
    "was too " + adjective2 + ". Instead, Zack gave it a " + noun2 + " which " +
    "caused it to " + verb2 + ".")
