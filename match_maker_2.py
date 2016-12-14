import csv

elligble_dict = {}

#pull all responses into a dict with email as key
with open('MatchMaker.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['Email Address']
		elligble_dict[row['Email Address']] = row

#create a tuple to store static data on the current match
def current_match(matchee):
	for person, value in elligble_dict.items():
		if matchee == value['Email Address']:
			feminist = value['Do you consider yourself a feminist?']
			banana = value['Do you peel your bananas from the top or the bottom?']
			peanutbutter = value['How do you prefer your peanutbutter']
			pokemon = value['Do you like Pokemon Go?']
			saturday_night = value['Which would you rather on a Saturday night?']
			sandwich = value['How do you cut your sandwich ']
			animal = value['Are you a dog person, or a cat person?']
			drinks = value['Approximately how many drinks do you have per week?']
			socks = value['Do you sleep with socks on?']
			fruit = value['What is your favorite fruit?']
			pickels = value['Pickles or Cucumbers']
			planning = value['Do you like to plan day-by-day or for the long term?']
			person_type = value['What would you consider yourself?']
			ski = value['Are you a skier or a snowboarder ']
			comma = value['Are you a fan of the oxford comma?']
			wish = value['What would you like to be doing?']
			age = value['Age']
			sexual_orientation = value['What Gender are you interested in ']
			gender = value['Gender']
			city = value['City of Residence']

	return(matchee, feminist, banana, peanutbutter,pokemon,saturday_night,sandwich,animal,drinks,socks,fruit,pickels,planning,person_type,ski,comma,wish,age,sexual_orientation,gender,city)

		
match_dict ={}

def match_alg(match_data):
	matchee, feminist, banana, peanutbutter,pokemon,saturday_night,sandwich,animal,drinks,socks,fruit,pickels,planning,person_type,ski,comma,wish,age,sexual_orientation,gender,city = match_data

	#iterate on each person in elligble list to get person's scores 
	for person,value in elligble_dict.items():
		personscore = 0

		if matchee != person:

			#not able to match w/anyone if not feminist
			if feminist == 'Yes':
				personscore += 1000

			#begin comparison between people (non-crucial)
			if banana == value['Do you peel your bananas from the top or the bottom?']:
				personscore += 1

			if peanutbutter == value['How do you prefer your peanutbutter']:
				personscore += 1

			if pokemon == value['Do you like Pokemon Go?']:
				personscore += 2

			if saturday_night == value['Which would you rather on a Saturday night?']:
				personscore += 3

			if sandwich == value['How do you cut your sandwich ']:
				personscore += 1

			if animal == value['Are you a dog person, or a cat person?']:
				personscore += 3

			if drinks == value['Approximately how many drinks do you have per week?']:
				personscore += 3

			if socks == value['Do you sleep with socks on?']:
				personscore += 1

			if fruit == value['What is your favorite fruit?']:
				personscore += 3

			if pickels == value['Pickles or Cucumbers']:
				personscore += 1

			if planning == value['Do you like to plan day-by-day or for the long term?']:
				personscore += 4

			if person_type == value['What would you consider yourself?']:
				personscore += 4

			if ski == value['Are you a skier or a snowboarder ']:
				personscore += 2

			if comma == value['Are you a fan of the oxford comma?']:
				personscore += 1

			if wish == value['What would you like to be doing?']:
				personscore += 5


			#filter out using high scores for crucial questions (must have at least 1301 pts to match w/someone)
			#must be within 7 years of one another, 100pts
			if abs(int(age) - int(value['Age'])) <= 7:
				personscore +=100

			#sexual orientation match 100pts
			if sexual_orientation == "Men" and value['Gender'] == 'Male' and value['What Gender are you interested in '] == "Women" and gender == 'Female':
				personscore += 100
			elif sexual_orientation == "Women" and value['Gender'] == 'Female' and value['What Gender are you interested in '] == "Men" and gender == 'Male':
				personscore += 100
			elif sexual_orientation == "Men & Women" and value['What Gender are you interested in '] == "Women" and gender == 'Female':
				personscore +=100
			elif sexual_orientation == "Men & Women" and value['What Gender are you interested in '] == "Men" and gender == 'Male':
				personscore +=100
			elif sexual_orientation == "Men & Women" and value['What Gender are you interested in '] == "Men & Women":
				personscore +=100

			#City 100pts
			if city == value['City of Residence']:
				personscore += 100


			match_dict[person] = personscore
			print person, personscore

	#print out the person with highest match score 
	print match_dict
	inverse = [(value, key) for key, value in match_dict.items()]
	print 'You have matched with ' + max(inverse)[1] + '!'
	

def user_input():
		name =raw_input('Who would you like to match?  ')	
		match_data = current_match(name)
		match_alg(match_data)	


def main():

	user_input()


if __name__ == "__main__":
    main()






