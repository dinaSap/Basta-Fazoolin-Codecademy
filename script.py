class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return (f"{self.name} Menu is available from {self.start_time} to {self.end_time}")
  def calculate_bill(self, purchased_items):
    total_price = 0
    for i in purchased_items.values():
      total_price += i
    return total_price
    
    
brunch = Menu("Brunch",{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 1100, 1600)
early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800 )
dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300 )
kids = Menu("Kid's Menu", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1100, 2100)

#print(brunch)
#print(brunch.calculate_bill({'pancakes': 7.50, 'home fries': 4.50, 'coffee': 1.50}))
#print(early_bird.calculate_bill({'salumeria plate': 8.00, 'mushroom ravioli (vegan)': 13.50 }))

class Franchise:
  def __init__(self,address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return self.address
  def available_menus(self, time):
    menu_list = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        menu_list.append(menu)
    return menu_list
        
    
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

#print(flagship_store.available_menus(1700))
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Arepa's Menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepa = Business("Take a' Arepa", arepas_place)




    
