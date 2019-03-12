import numpy as np

# these random data generating functions will be used to init Item class attiributes
# such as self.itemState = randGen_itemState() for Item class
def randGen_itemState():
    """ RANDOMLY GENERATES ITEM.ATTIRIBUTE FOR STATE
    DEMO VERSION ONLY FOR CO CA NE """
    pass 
    demoStateList = ['California', 'Colorado', 'Nebraska']
    randomIndexState = np.random.randint(0, int(len(demoStateList)-1))
    return demoStateList[randomIndexState]

# generates another attiribute self.itemType = randGen_itemType()
def randGen_itemType():
    """ RANDOMLY GENERATES ITEM.ATTIRIBUTE FROM 
    LIST: 1BR 2BR 3BR CONDO """
    # binomial expansion to apprx normal dist aka bell curve
    # 1-2-2-1 > 1-3-4-3-1
    demoItemTypeList = [
        'OneBedroom', 'TwoBedroom', 'TwoBedroom', 'ThreeBedroom',
        'ThreeBedroom', 'Condo'
    ]
    randomIndexType = np.random.randint(0, int(len(demoItemTypeList) - 1))

    return demoItemTypeList[randomIndexType]

def randGen_itemBasePrice():
    """GENERATES RANDOM PRICES AS PER OBSERVED STATISTICAL DIST
    """
    __DEMO = np.random.randint(149000,299000)
    return int(round(__DEMO,2))

# below dictionary is required for an excel-VLOOKUP-like case-switch
def dictItemType_init():
    """RETURNS DICTIONARY TO USE AS A REF TABLE FOR ITEM TYPE"""
    keysItemType = ['OneBedroom', 'TwoBedroom', 'ThreeBedroom', 'Condo']
    valuesItemType = ['1B','2B','3B','0C']
    return dict(zip(keysItemType,valuesItemType))

def randGen_itemID(itemState, itemType):
    """ RANDOMLY GENERATES BARCODE-LIKE ITEM ID'S"""
    pass
    itemBarcode_First = itemState
    dictItemType = dictItemType_init()
    itemBarcode_Second = dictItemType[itemType]
    itemBarcode_Third = '00'
    itemBarcode_Fourth = str(np.random.randint(100000,111111))

    return str(itemBarcode_First+itemBarcode_Second+itemBarcode_Third+itemBarcode_Fourth)

def randGen_itemType():
    """ RANDOMLY GENERATES ITEM.ATTIRIBUTE FROM 
    LIST: 1BR 2BR 3BR CONDO """
# binomial expansion to apprx normal dist aka bell curve
# 1-2-2-1    
    demoItemTypeList = [
        'OneBedroom', 'TwoBedroom', 'TwoBedroom', 'ThreeBedroom',
        'ThreeBedroom', 'Condo'
    ]
    randomIndexType = np.random.randint(0, int(len(demoItemTypeList) - 1))
    randomIndexType = np.random.randint(0, int(len(demoItemTypeList) - 1))
#     print(randomIndexType)

    return demoItemTypeList[randomIndexType]


# below dictionary is required for an excel-VLOOKUP-like case-switch
def dictItemType_init():
    keysItemType = ['OneBedroom', 'TwoBedroom', 'ThreeBedroom', 'Condo']
    valuesItemType = ['1B','2B','3B','0C']
    return dict(zip(keysItemType,valuesItemType))


def dictItemState_init():
    """RETURNS DICTIONARY TO STORE STATE ABBRV 
    EX KEY: COLORADO VALUE: CO, CALIFORNIA:CA, NEBRASKA: NE"""
# these states for demo-run
    keysItemState = [
            'California',
            'Colorado',
            'Nebraska'
    ]
# convert into abrv for itemID
    valuesItemState = [
            'CA',
            'CO',
            'NE'
    ]

    return dict(zip(keysItemState,valuesItemState))

def randGen_itemID(itemState, itemType):
    """ GENERATE RANDOM ITEM ID FOR DATA STORAGE ETC. """
    
    pass
    dictItemState = dictItemState_init() 
    itemBarcode_First = dictItemState[itemState]
    dictItemType = dictItemType_init()
    itemBarcode_Second = dictItemType[itemType]
    itemBarcode_Third = '00'
    itemBarcode_Fourth = str(np.random.randint(100000,111111))

    return str(itemBarcode_First+itemBarcode_Second+itemBarcode_Third+itemBarcode_Fourth)

def labelMaker(itemState, itemType):
    pass
    """  CRE4TE LABELS TO PULL CURRENT ROUND'S PRICE FROM 
    MASTER PRICE DATABASE (LIST-OF-LISTS) EX: CO1B will be 
    used to pull data (ie. price index) for a Colorado One Bedroom etc."""
    
    
    dictItemState = dictItemState_init() 
    itemBarcode_First = dictItemState[itemState]
    dictItemType = dictItemType_init()
    itemBarcode_Second = dictItemType[itemType]

    return str(itemBarcode_First+itemBarcode_Second)



def dictItemIcon_init():
    """RETURNS A DICTIONARY THAT STORES URL DIRECTORY
    FOR PRE-LOADED IMAGES TO GITHUB"""
    
    keysItemType = [
        'OneBedroom',
        'TwoBedroom',
        'ThreeBedroom',
        'Condo'                        
    ]
# below will be appended to base URL before random no
    valuesItemIconDir = [
        '/1-',
        '/2-',
        '/3-',
        '/0-',
    ]
    return dict(zip(keysItemType,valuesItemIconDir))

# --------------------------

# add to base URL to choose a pre-loaded image randomly
def randGen_itemIcon(itemType):
    """"RANDOMLY GENERATES ITEM ICON NO THAT WILL BE
    APPENDED TO BASE-URL. TAKES ITEM TYPE AS PARAMETER"""
    pass
    baseURL = 'https://raw.githubusercontent.com/attila5287/pr3-RegroPoly-assets-herokuAPP/master'
    dictItemIcon = dictItemIcon_init()
    append2IconURL1 = dictItemIcon[itemType]
    append2IconURL1str = str(append2IconURL1)
    append2IconURL2 = np.random.randint(1,6)
    append2IconURL_2str = str(append2IconURL2)
    append_ext = '.png'
    return str(baseURL + append2IconURL1str + append2IconURL_2str + append_ext)


def dictItemDesc_init():
    """
    RETURNS A DICTIONARY THAT STORES TEXT PARTS TO BE PLACED
    IN ITEM-TITLE i.e. KEY:OneBedroom VAL:one bedroom
    """
    keysItemType = [
        'OneBedroom',
        'TwoBedroom',
        'ThreeBedroom',
        'Condo'                        
    ]
# below will be appended to base URL before random no
    values_for_ItemDesc = [
        ' one bedroom in ',
        ' two bedroom in ',
        ' three bedroom in ',
        ' condo in '
    ]
    return dict(zip(keysItemType,values_for_ItemDesc))


def randGen_itemTitle(itemType, itemState):
    pass
    dict_for_title = dictItemDesc_init()
    adjectiveTitle = ['Alluring', 'Astonishing', 'Breathtaking', 'Brilliant', 'Captivating', 'Crisp', 'Dazzling', 'Discerning', 'Divine', 'Effervescent', 'Enchanting', 'Enrapturing',
    'Enthralling', 'Enticing', 'Exceptional', 'Exquisite', 'Fabulous', 'Harmonious', 'Magnificent', 'Marvelous', 'Outstanding', 'Rare', 'Resplendent', 'Sensational',
    'Sophisticated', 'Spectacular', 'Stately', 'Striking', 'Soothing', 'Stunning', 'Sun-drenched', 'Timeless', 'Unmatched', 'Unparalleled', 'Upscale', 'Warm', 'Welcoming']
    randomIndexTitle = np.random.randint(0, int(len(adjectiveTitle) - 1))

    title_first = str(adjectiveTitle[randomIndexTitle])
    title_second = str(dict_for_title[itemType])
    title_third = str(itemState)
    title_fourth = '!..'
        
    # now lets concatanate all string objects into title
    title_final = title_first + title_second + title_third + title_fourth

    return title_final

