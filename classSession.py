#%%

from classItem import (
    Item
)
# this will be used in a method later as item generator
from buildHousesForSale import (
    buildTenHouses
)

# import data structures-functions etc for SessionGame()
from functions_Session import(
    dict_summary_init
)

#%%


class SessionGame():
    """
    GENERATES ITEMS EACH ROUND TO BUY-SELL, ALSO CONTAINS
    PLAYER ASSETS AND KEEPS TRACK OF PLAYER FUNDS-PROFIT
    """
    def __init__(self,
     roundNo = int(), 
     roundStart = int(), 
     roundFinish = int(), 
     playerAssets = [], 
     playerFunds = int(), 
     playerScore = int(), 
     **kwargs):
        super().__init__(**kwargs)
        self.roundNo = int(1)
        self.roundStart = int(0)
        self.roundFinish = int(16)
        self.playerAssets = []
        self.playerFunds = int(1500000)
        self.playerScore = int(50)

    def generate_items(self):
        """
        GENERATES TEN ITEMS WITH buildTenHouses()
        FUNCTION RANDOMLY. RETURNS A LIST OF TEN
        """
        pass
        return list(buildTenHouses())

    def summary_round(self):
        """
        RETURNS A DICTIONARY WITH PRE-SET KEYS 
        AND INSTANCE-SPECIFIC DYNAMIC VALUES. EX:
        ROUND-INFO, CURR-ASSETS, AVLB-FUNDS or
        SCORE(RATE-OF-RETURN) (at any given time during play)
        """
        pass
        _dict = dict_summary_init()
        _dict['title'] = 'R-0-U-N-D'
        _dict['value_current'] = int(self.roundNo)
        _dict['value_min'] = int(self.roundStart)
        _dict['value_max'] = int(self.roundFinish)
        return _dict

    def summary_funds(self):
        """
        RETURNS A DICTIONARY WITH PRE-SET KEYS 
        AND INSTANCE-SPECIFIC DYNAMIC VALUES. EX:
        AVLB-FUNDS (at any given time during play)
        """
        pass
        _dict = dict_summary_init()
        _dict['title'] = 'F-U-N-D-S'
        _dict['value_current'] = int(self.playerFunds)
        _dict['value_min'] = int(0)
        _dict['value_max'] = int(self.playerFunds*1.50)
        return _dict

    def summary_assets(self):
        """
        RETURNS A DICTIONARY WITH PRE-SET KEYS 
        AND INSTANCE-SPECIFIC DYNAMIC VALUES. EX:
        CURRENTLY-OWNED-ASSETS-INVESTMENTS
         (at any given time during play)
        """
        pass
        _dict = dict_summary_init()
        _dict['title'] = 'A-S-S-E-T-S'
        _dict['value_current'] = int(len(self.playerAssets))
        _dict['value_min'] = int(0)
        _dict['value_max'] = int(len(self.playerAssets)+5)
        return _dict        

        
    def summary_score(self):
        """
        RETURNS A DICTIONARY WITH PRE-SET KEYS 
        AND INSTANCE-SPECIFIC DYNAMIC VALUES. EX:
        SCORE (RATE-OF-RETURN) ON INVESTMENTS
         (at any given time during play)
        """
        pass
        _dict = dict_summary_init()
        _dict['title'] = 'S-C-O-R-E'
        _dict['value_current'] = int(self.playerScore)
        _dict['value_min'] = int(0)
        _dict['value_max'] = int(100)
        return _dict        

#%%

# ================= SESSION-END =================
# testSesh = SessionGame()
# ------------------------
# list_summaryRound = testSesh.summary_round()
# print(list_summaryRound)
# ------------------------
# list_summaryFunds = testSesh.summary_funds()
# print(list_summaryFunds)
# ------------------------
# list_summaryAssets = testSesh.summary_assets()
# print(list_summaryAssets)
# ------------------------
# list_summaryScore = testSesh.summary_score()
# print(list_summaryScore)
# ------------------------


#%%


#%%
 