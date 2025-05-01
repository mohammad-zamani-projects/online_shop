
class FourDigitYear:
    regex = "[0-9]{4}"  # regex must be here and you must use it

    def to_python(self, value):
        # return int(value) + 1  # if you want change the value, do it here
        return int(value)

    def to_url(self, value):
        return value
