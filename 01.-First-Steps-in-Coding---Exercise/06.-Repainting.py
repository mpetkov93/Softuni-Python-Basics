protective_nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
hours_for_work_to_be_done = int(input())

added_nylon = 2
added_paint_percentage = 0.10
added_bags = 0.40
workers_price_percentage = 0.30

total_nylon_price = (quantity_nylon + added_nylon) * protective_nylon_price
total_paint_price = (quantity_paint + (quantity_paint * added_paint_percentage)) * paint_price
total_thinner_price = quantity_thinner * paint_thinner_price

total_sum_of_materials = total_nylon_price + total_paint_price + total_thinner_price + added_bags

total_workers_price = (total_sum_of_materials * workers_price_percentage) * hours_for_work_to_be_done

total_price = total_sum_of_materials + total_workers_price

print (total_price)