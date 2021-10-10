def get_orders():
    intro = {
        "part1": """
      *******************************************
      **      Welcome to the Snakes Cafe!      **
      **      Please see our menu below.       **
      **                                       **
      **   To quit at any time, type "quit"    **
      ** To see all of your orders type "show" **
      *******************************************
      """,
        "part2": """
      **************************************
      **   What would you like to order?  **
      **************************************
      """
    }
    menu = {
        "Appetizers": [
            "wings",
            "cookies",
            "spring rolls",
        ],
        "Entrees": [
            "salmon",
            "steak",
            "meat tornado",
            "a literal garden"
        ],
        "Desserts": [
            "ice cream",
            "cake",
            "pie",
        ],
        "Drinks": [
            "coffee",
            "tea",
            "unicorn tears",
        ]
    }
    items = []

    print(intro['part1'])
    for cat in menu.keys():
        items.extend(menu[cat])
        print(cat, '\n----------')
        for itm in menu[cat]:
            print(itm.title())
        print()
    print(intro['part2'])

    choices = {}

    def prompt():
        choice = input('> ').lower()
        while choice != 'quit':
            choice = choice if choice in items else choice.lower(
            ) if choice.lower() in items else choice if choice == 'show' else None
            if choice and choice != 'show':
                choices[choice.lower()] = 1 if not choices.get(
                    choice.lower()) else choices[choice.lower()] + 1
                print(f'** {choices.get(choice)} {"order" if choices.get(choice) == 1 else "orders"} of {choice} {"has" if choices.get(choice) == 1 else "have"} been added to your meal **')
            elif choice == 'show':
                print('******** Order details: ')
                for itm, count in choices.items():
                    print(f'{itm}:   {count}')
                cont = input(
                    'would you like to add more to the meal? (y)es | (n)o\n>  ')
                if cont == 'yes' or cont == 'y':
                    prompt()
                elif cont == 'no' or cont == 'n':
                    return
            else:
                print(
                    '** Sorry, the item you provided is not available in the menu, please try again **')
            choice = input('> ')

    prompt()
    return choices

if __name__ == '__main__':
    get_orders()
