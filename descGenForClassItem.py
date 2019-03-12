import numpy as np
# dictionary with keys as database values 
# and values as string objects to be placed into description

# this will generate a paragraph text as property description
def randGen_itemDesc():
    """"RANDOMLY GENERATES A PARAGRAPH AS AN ITEM DESCRIPTION
    TAKES ITEM TYPE AS SINGLE PARAMETER"""

    adjectiveKitchen = ['Awe-inspiring', 'Bright', 'Capacious', 'Complete', 'Cutting edge', 'Decked out', 'Designed for convenience', 'Dream', 'Enormous open air', 'Equipped', 'Every convenience', 'Modern', 'Open concept', 'Outdoor entertaining', 'Perfect for the inspired home chef', 'State-of-the-art appliances', 'Stocked', 'Stylish', 'Sunny',
    'Ultramodern', 'Vast', 'Workmanship']

    adjectiveView = ['Amazing', 'Astonishing', 'Bewitching', 'Breathtaking', 'Captivating', 'Cityscape', 'Delightful', 'Dramatic', 'Enchanting', 'Endless', 'Enthralling', 'Ever-changing', 'Exquisite', 'For miles', 'Iconic', 'Inviting', 'Luxuriate in', 'Magnetic', 'Mountainous', 'Natural', 'Panoramic', 'Peaceful', 'Picturesque', 'Savor', 'Soak in', 'Uninterrupted', 'Unobstructed']


    adjectiveAthmosphere = ['Alluring', 'Casual', 'Charming', 'Chic', 'Choice', 'Classic', 'Consummate', 'Contemporary', 'Cosmopolitan', 'Custom', 'Desirable', 'Elegant', 'Enticing', 'Exceptional', 'Exemplary', 'Expansive', 'Exquisite', 'Glorious', 'Graceful', 'Idyllic', 'Illuminating', 'Impeccable', 'Impressive', 'Lush', 'Luxurious', 'Majestic', 'Notable', 'Private', 'Prized', 'Quintessential', 'Refined', 'Sleek', 'Sophisticated', 'Sought-After', 'Stately', 'Superior'
    ]

    adjectiveNeighborhood = ['Affluent', 'Bucolic', 'Charming', 'Chic', 'Elegant', 'Enchanting', 'Exclusive', 'Family-friendly', 'Gated', 'Historic', 'Lavish', 'Leafy', 'Lively', 'Peaceful', 'Posh', 'Prestigious', 'Quiet', 'Serene', 'Sleek', 'Sought-after', 'Storied', 'Tranquil', 'Tree-lined', 'Trendy', 'Upscale', 'Urban', 'Verdant', 'Well-kept']

    desc_masterList = [adjectiveKitchen, adjectiveView, adjectiveAthmosphere, adjectiveNeighborhood]
    desc_pairZipList = [
        ' kitchen - ',
        ' view - ',
        ' atmosphere - ',
        ' neighborhood '
    ]

# initiliaze an empty list to store random adjective with property features
    random_paired_str = ''
# random pair generator
# concatane every pair after another with multiple-list-iteration below
    for adj_list,pair in zip(desc_masterList,desc_pairZipList):
        lenList = len(adj_list)
        randomIndexNo = np.random.randint(0,lenList)
        random_adjective = adj_list[randomIndexNo]
        paired_str = str(random_adjective + pair)
        random_paired_str+=paired_str

# returns final string object with all above in one
    return str(random_paired_str)

