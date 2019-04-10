names = ['james', 'katie', 'thomas', 'jaxon', 'tommy', 'eddie', 'lillie', ]
position = ['1st', '2nd', '3rd']
first_place = "In " + position[0] + " place is: " + names[3].title()
second_place = "In " + position[1] + " place is: " + names[2].title()
third_place = "In " + position[2] + " place is: " + names[-1].title()

print(first_place + "\n\t" + second_place + "\n\t\t" + third_place)
