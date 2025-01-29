school_records={"class_1":{
	"students":[
			{"name": "Harry", "scores":{"Math":88, "English":76}},
			{"name": "Solomon", "scores":{"Math":95, "English":89}},
		]
	},
	
	"class_2":{
	"students":[
			{"name": "Daniel", "scores":{"Math":78, "English":72}},
			{"name": "Samuel", "scores":{"Math":85, "English":80}},
		]
	}
}
for keys,value in school_records.items():
		for students in value["students"]:
			if students["name"] == "Samuel":
				print(students)

total_score = 0
total_students = 0
for keys,value in school_records.items():
	for students in value["students"]:
		total_score+= students["scores"]["Math"]
		total_students += 1
average = total_score/total_students
print(f"Average is {average}")
	