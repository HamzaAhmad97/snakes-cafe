def get_orders():
    intro = {
        "part1": """
      **************************************
      **    Welcome to the Snakes Cafe!   **
      **     Please see our menu below.   **
      **                                  **
      ** To quit at any time, type "quit" **
      **************************************
      """,
        "part2": """
      **************************************
      **   What would you like to order?  **
      **************************************
      """
    }
    menu = {
        "Appetizers": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
        "Entrees": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden"
        ],
        "Desserts": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],
        "Drinks": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ]
    }
    allItems = []
    for _, itms in menu.items():
        allItems.extend(itms)

    print(intro['part1'])
    for cat in menu.keys():
        print(cat, '\n----------')
        for itm in menu[cat]:
            print(itm)
        print()
    print(intro['part2'])
    print(allItems)
    choices = {}
    choice = input('>')
    


get_orders()
