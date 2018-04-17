
class Venue(object):

    def __init__(

            self,
            sk_id:       int,
            displayName: str,
            city:        str,
            state:       str):

            self.sk_id = sk_id
            self.displayName = displayName
            self.city = city
            self.state = state

    def __str__(self):

        return "      \n" \
            "ID: {}   \n" \
            "Name: {} \n" \
            "City: {} \n" \
            "State: {}\n".format(

             str(self.sk_id),
             self.displayName,
             self.city,
             self.state)
