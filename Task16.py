# If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?

earth_weight = int(input("Your weight:"))

for i in range(1, 16):
    earth_weight = earth_weight + 1
    moon_weight = earth_weight * 0.165
    print("Moon:", moon_weight)
