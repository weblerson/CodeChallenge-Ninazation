import re

class Utils:
    @staticmethod
    def validate_password(value: str) -> bool:
        regex = re.compile(
            r'(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%<^&*?])(?=.*[0-9])[a-zA-Z0-9!@#$%<^&*?]{8,}'
        )
        if not regex.match(value):
            return False

        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        regex = re.compile(
            r'.+@.+\.[\.com\.br]+'
        )
        if not regex.match(email):
            return False

        return True