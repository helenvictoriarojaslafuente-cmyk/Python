def extract_domain(email):
    domain = email.split("@")[1]
    return domain
print(extract_domain("helen@empresa.com"))