def is_palindrome(t):
    return (s := "".join(t.split()).lower()) == s[::-1]
phrase = input("Enter a phrase: ")
if is_palindrome(phrase):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")