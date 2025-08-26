import re
import pyhibp
from pyhibp import pwnedpasswords as pw
import math
pyhibp.set_user_agent("MyPythonApp/1.0")

#~~~~~~Get user password~~~~~~#
password = input("Hi can you provide the password? ")

#~~~~~~~Calculate the Shannon entropy of the password~~~~~~#
def shannon_entropy(password):
    prob = [float(password.count(c)) / len(password) for c in set(password)]
    return -sum(p * math.log2(p) for p in prob)
entropy = shannon_entropy(password)

#~~~~~~~Crack time estimation~~~~~~~~~~#
def crack_time(password):
    charset = 0
    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32
    if charset == 0:
      return "Instantly (no valid charset detected)"
    guesses = charset ** len(password)
    guesses_per_second = 1e9
    seconds = guesses / guesses_per_second
    years = seconds / (60 * 60 * 24 * 365.25)
    if years < 1:return f"{seconds:.2f} seconds"
    elif years < 100: return f"{years:.2f} years"
    else: return f">{int(years)} years"

#~~~~~~Strength checker~~~~~~#
def strength_checker(password, entropy):
    score = 0
    report = []

#~~~~~~~Dictionary check~~~~~~~~~~~#
    pwned_count = pw.is_password_breached(password)
    if pwned_count:
        report.append(f"Password has been breached {pwned_count} times.")
        print("\n~~~ Password Strength Report ~~~")
        for r in report:
         print(r)
        print("Password is automatically marked WEAK due to breach.")
        return
    else:
         report.append("Password has not been breached.")
    
#~~~~~~~Length check~~~~~~~~~~~#
    if len(password) < 8:
         score -= 1
         report.append("Password is too short.")
    elif 8 <= len(password) <= 12:
            score += 2
            report.append("password length is good.")
    elif 13 <= len(password) < 20:
         score += 2
         report.append("Password length is very good.")
    elif len(password) >= 20:
         score += 3
         report.append("Password length is excellent.")

#~~~~~~~~~Character variety check~~~~~~~~~#
    if any(char.isdigit() for char in password):
         score += 1
         report.append("Password contains numbers.")
    else:
         report.append("Password does not contain numbers.")
    if any(char.islower() for char in password):
         score += 1
         report.append("Password contains lowercase letters.")
    else:
         report.append("Password does not contain lowercase letters.")
    if any(char.isupper() for char in password):
         score += 1
         report.append("Password contains uppercase letters.")
    else:
         report.append("Password does not contain uppercase letters.")
    if any(char in "!@#$%^&*()-+" for char in password):
         score += 1
         report.append("Password contains special characters.")
    else:
         report.append("Password does not contain special characters.")

#~~~~~~~Pattern check~~~~~~~~~~~#
    if re.match(r"(.)\1{3,}", password) or password in ["123456", "qwerty", "abcdef"]:
        report.append("Password contains common patterns.")
        score -= 2

#~~~~~~~Entropy check~~~~~~~~~~~#
    if entropy < 3.5:
        report.append(f"Password has low entropy.")
        score -= 1
    elif 3.5 <= entropy <= 4.5:
        report.append(f"Password has medium entropy.")
        score += 1
    elif entropy > 4.5:
        report.append(f"Password has high entropy.")
        score += 2

#~~~~~~~~~Final report~~~~~~~~~~~#
    print("\n~~~ Password Strength Report ~~~")
    for r in report:
        print(r)
    print(f"Final Score: {score}")
    print(f"Estimated crack time: {crack_time(password)}")
    print(f"Shannon Entropy: {entropy:.2f}")
    if score >= 8:
        print("Password is strong.")
    elif 4 <= score < 8:
        print("Password is moderate.")
    else:
        print("Password is weak.")
strength_checker(password, entropy)
