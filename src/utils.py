class Utils:
    def validate_email(self, email):
        # Add your implementation here
        if '@' in email:
            return True
        else:
            return False

    def validate_input(self, input):
        # Add your implementation here
        if input:
            return True
        else:
            return False