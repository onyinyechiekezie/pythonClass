countries = {
	"USA":{"California": {"Los Angeles": 4000000, "San Francisco": 870000}},
	"Canada": {"Ontario": {"Toronto": 2930000, "Ottawa": 994837}}
	}
for city in countries["USA"]["California"].items():
	print(city)