

def get_population():
	countries = {
	"USA":{"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
	"Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
	}

	country = input("Enter ur country name")
	state = input("Enter state")
	for city in countries["USA"]["California"].items():
		print(city)
		
get_population()

def add_country():
	countries = {
	"USA":{"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
	"Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
	}
	new_country = {
	Nigeria = {Lagos : {"mainland": 4_200_329, "Ikorodu": 4_230_000}}
	}

	country = input("Enter ur country name")
	state = input("Enter state")
	for key, value in new_country.items():
		countries[key] = value
	print(countries)

add_country() 
	