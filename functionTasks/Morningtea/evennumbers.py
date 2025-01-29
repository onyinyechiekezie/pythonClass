def get_even_numbers(string):
	list = []
	for char in string:
		if char.isdigit():
			list.append(int(char))
	evenlist = []
	for numbers in list:
		if numbers % 2 == 0:
			evenlist.append(numbers)
	return evenlist
	
	
"""def dictionary():
	collect = int(input("Enter a number:"))
	key = []
	value = []
	dictionary = {}
	for count in range(1,4):
		key.append(count)

	for index in key:
		value.append(collect**index)
	for x,y in zip(key , value):
		dictionary[x] = y
	return dictionary 
print(dictionary())"""


def get_list(numbers):
	return[i > 20 for i in numbers if i < 51]


def get_student_grades(score):
	student_scores = {"Gloria": "88", "Divine":"78", " Esther":"65","Mercy":"75","Uzo":"71"}
for key,value in score():
	score[key]=""
		if value > 91| value <= 100:
			print("Outstanding")	
		if value > 81| value <= 90:
			print("Exceed expectation")	
		if value > 71| value <= 80:
			print("Acceptable")
		if value > 61| value <= 70:
			print("Fail")


def get_cohort_details(list1, list2):
	for key,value in zip(list1, list2):
		my_list[list1 - 1] = [list2 + 1]	
	return get_cohort_details

"""Question on nested_dictionary"""

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
	
	
	
	