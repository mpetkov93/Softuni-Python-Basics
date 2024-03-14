package_of_pens = 5.80
package_of_markers = 7.20
abstergent = 1.20

count_of_pens = int(input())
count_of_markers = int(input())
liters_of_abstergent = int(input())
percent_discount = int(input()) / 100

pens_total_price = count_of_pens * package_of_pens
markers_total_price = count_of_markers * package_of_markers
abstergent_total_price = liters_of_abstergent * abstergent

total_price = pens_total_price + markers_total_price + abstergent_total_price

print(total_price - total_price * percent_discount)