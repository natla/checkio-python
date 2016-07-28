"""
Stephan and Sophia forget about security and use simple passwords for everything. Help Nikola develop a password security check module. The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it.
The password contains only ASCII latin letters or digits.

Input: A password as a string.
Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.

Example:
checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True

How it is used: If you are worried about the security of your app or service, you can check your users' passwords for complexity. You can use these skills to require that your users passwords meet more conditions (punctuations or unicode).
"""
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits


def checkio(data):
    if len(data) >= 10 and data.isalnum():
        for l in lowercase:
            if l in data:
                for u in uppercase:
                    if u in data:
                        for d in digits:
                            if d in data:
                                return True
    return False

print(checkio('A1213pokl'))
print(checkio('bAse730onE'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))
