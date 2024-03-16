year_tax = int(input())

sneakers_price = year_tax - year_tax * 0.40
basketball_outfit_price = sneakers_price - sneakers_price * 0.20
basketball_ball_price = basketball_outfit_price / 4
basketball_accessories_price = basketball_ball_price / 5

total_price = year_tax + sneakers_price + basketball_outfit_price + basketball_ball_price + basketball_accessories_price

print (total_price)