# market generating items
class Agent:
    """"
    MARKET OBJECT GENERATES RANDOM HOUSE LISTINGS FOR SALE
    IMPORTANT: NEXT ROUND METHOD, PRICE GENERATOR METHODS
    """
    
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input(
                "What type of property? ",
                ("house", "apartment")).lower()
        payment_type = get_valid_input(
                "What payment type? ",
                ("purchase", "rental")).lower()

        PropertyClass = self.type_map[current_round]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))



