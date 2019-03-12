import numpy as np
from classItem import (
    Item
)


def buildTenHouses():
    """" GENERATES TEN CLS 'ITEM()' OBJECT AND STORES IN A LIST 
    TAKES NO ARGUMENTS, RETURNS AN ITERABLE OBJ(LIST) 
    FOR LATER USE ON OUT WEB FRAMEWORK COMPONENTS-MONGODB-JINJA2 
    ALSO PLEASE @app.route('/test/ten') testTen() FOR FLASK """
    print(" - $ - $  - # -REGROPOLY- # - $  - $ - ")
    # = list() no mas! = [] four-five times faster for empty list
    # test above with datetime module timeit function
    tenLittleHouses = []
    for n in range(0,10):
        newlittleHouse = None
        newlittleHouse = Item()
        tenLittleHouses.append(newlittleHouse)
        print('>                 generating ' + str(n) + ' out of 10 ')
        newlittleHouse.display()
    print(" - - - - - - - - - - - - - - - - - - - ")
    # returns an iterable for web display jinja2 temp engine compatible
    return list(tenLittleHouses)
# - - - - - - - - - - -

# test_list_tenItems = buildTenHouses()
# for item in test_list_tenItems:
#     print(item.itemState)
# - - - - - - - - - - -