import CellPhoneClass as CP

iPhone = CP.CellPhone("Apple", "13 pro", 1000 )

print(f"The iPhone is manufactured by {iPhone.get_manufact()}, it's a {iPhone.get_model()} and it is priced at ${iPhone.get_retail_price()}")