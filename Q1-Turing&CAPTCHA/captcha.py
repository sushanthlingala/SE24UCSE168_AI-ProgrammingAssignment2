import random
import string


class CaptchaGenerator:
    def generate(self):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=5))

    def distort(self, code):
        noise = [".", "~", "*", "|", "!"]
        return "[ " + " ".join(ch + random.choice(noise) for ch in code) + " ]"


class CaptchaValidator:
    def check(self, code, user_input):
        return user_input.strip().upper() == code.upper()


class CaptchaSession:
    MAX_ATTEMPTS = 3

    def __init__(self):
        self.attempts = 0
        self.solved = False
        self.locked = False
        self._gen = CaptchaGenerator()
        self._val = CaptchaValidator()
        self.code = None

    def new_challenge(self):
        self.code = self._gen.generate()
        return self._gen.distort(self.code)

    def submit(self, user_input):
        if self.locked:
            return "locked"
        self.attempts += 1
        if self._val.check(self.code, user_input):
            self.solved = True
            return "correct"
        if self.attempts >= self.MAX_ATTEMPTS:
            self.locked = True
            return "locked"
        return "incorrect"


def run():
    session = CaptchaSession()
    print("--- CAPTCHA ---")

    while not session.solved and not session.locked:
        print(f"\n{session.new_challenge()}")
        result = session.submit(input("Enter the 5 characters in the CAPTCHA above (no spaces): "))

        if result == "correct":
            print("Access granted.")
        elif result == "locked":
            print("Too many attempts. Access denied.")
        else:
            print(f"Wrong. {CaptchaSession.MAX_ATTEMPTS - session.attempts} attempt(s) left.")


run()