#%% 
from classItem import Item
""""

"""

class Player():
    """"
    CLASS FOR PLAYER() THAT CAN BUY SELL ITEMS AND KEEP SCORE
    """
    
    def __init__(self, playerName='', playerAssets = [], availableFunds= None, **kwargs):
        super().__init__(**kwargs)
        self.playerName = 'anonymous'
        self.playerAssets = []
        self.availableFunds = 1500000
        print(str(self.playerName + ' joined the game'))
        print(" $ {:,.0} ".format(self.availableFunds))
        return None

    def set_name (self):
        """" 
        SET NEW NAME FOR PLAYER 
        """
        print('player name is currently : ' + str(self.playerName))
        print('# # # # PLEASE ENTER NAME # # # # ')
        __name = str(self.playerName)
        _user_input = input('')
        self.playerName = _user_input 
        print(__name + ' changed player name to : ' + str(self.playerName))

    def display_assets(self):
        """
        DISPLAY METHOD ON EACH ITEM IN PLAYER ASSETS
        """
        
        for property in self.playerAssets:
            property.display()
    
    def add_property (self):
        """" ADD RANDOM ITEM TO PLAYER ASSETS """
        _first_item2add = Item()
        self.playerAssets.append(_first_item2add)
        print(_first_item2add.itemID + ' added to assets')
    # second item 
        _second_item2add = Item()
        self.playerAssets.append(_second_item2add)
        print(_second_item2add.itemID + ' added to assets')
    # third item
        _third_item2add = Item()
        self.playerAssets.append(_third_item2add)
        print(_third_item2add.itemID + ' added to assets')
#  = = = = = = = = = = = = = = = = = = 
#%% 
attila = Player()

#%%
attila.add_property()

#%%
attila.display_assets()

#%%

# ---------------

#%%


#%%
