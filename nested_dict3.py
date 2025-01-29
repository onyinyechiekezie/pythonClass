def add_country():
	countries = {
	"USA":{"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
	"Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
	}
	new_country = {
	"Nigeria":{"Lagos" : {"mainland": 4200329, "Ikorodu": 4230000}}
	}

	country = input("Enter ur country name: ")
	state = input("Enter state: ")
	for key, value in new_country.items():
		countries[key] = value
	print(countries)

add_country() 
	