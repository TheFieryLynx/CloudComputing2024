class User:
    def __init__(self, email="", first_name="", last_name="", user_dict=None):
        if user_dict is not None:
            for key in user_dict:
                setattr(self, key, user_dict[key])
        else:
            self.email = email
            self.firstName = first_name
            self.lastName = last_name
