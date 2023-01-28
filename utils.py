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