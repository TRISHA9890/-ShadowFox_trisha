import math 
def calculate_pond_area(radius):
    pi=3.14
    area=pi*(radius**2)
    return area

def calculate_water_in_pond(area,water_per_square_meter):
    water_in_pond=area*water_per_square_meter
    return round(water_in_pond)


radius=84
water_per_square_meter=1.4

pond_area=calculate_pond_area(radius)

total_water=calculate_water_in_pond(pond_area,water_per_square_meter)

print("The area of the pond is approximately{:.2f} square meters.".format(pond_area))
print("The total amount of water in the pond is approximately{}liters".format(total_water))