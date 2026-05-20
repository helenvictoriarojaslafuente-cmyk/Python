def generate_acronym(org_name):
    connectors = ["of", "the", "and", "in", "for", "on", "a", "an"]
    acronym = [word[0].upper() for word in org_name.split() if word.lower() not in connectors]
    return "".join(acronym)
print(generate_acronym("World Health Organization"))