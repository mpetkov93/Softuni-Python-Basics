chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
desert_percentage = 0.20
delivery = 2.50

count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vegan_menus = int(input())

total_price = count_chicken_menus * chicken_menu + count_fish_menus * fish_menu + count_vegan_menus * vegan_menu
total_price = total_price + total_price * desert_percentage
total_price = total_price + delivery

print (total_price)