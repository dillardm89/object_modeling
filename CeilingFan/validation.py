# Function to validate user input type = int
def validate_type_is_int(user_input):
    return user_input.isnumeric()


# Function to validate user input type = str
def validate_type_is_str(user_input):
    return isinstance(user_input, str)
