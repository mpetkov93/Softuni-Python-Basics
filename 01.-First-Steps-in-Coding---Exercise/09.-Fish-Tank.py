length = int(input())
width = int(input())
height = int(input())
percentage_full = float(input()) / 100

volume = length * width * height

volume_in_liters = volume / 1000

needed_liters = volume_in_liters * (1 - percentage_full)

print (needed_liters)