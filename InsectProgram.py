import InsectClass as i

mosquito = i.insect(2,4,'mosquito')
housefly = i.insect(2,4,'housefly')

#calculate the flight length

mosquito.calc_flight()
housefly.calc_flight()

print(f"The {mosquito.get_name()} can fly upto {mosquito.get_flight()} miles")
print(f"The {housefly.get_name()} can fly upto {housefly.get_flight()} miles")