first_name = "jaxon"
last_name = "reid"
message = "My beautiful boy"
message2 = ",happy birthday! daddy loves you very much"
print(message+" "+first_name.title()+" "+last_name.upper()+" "+message2)
# changes string for 2nd project example
#.title allows you to capitalise the 1st letter of your string ie go from jaxon to Jaxon
firstname = "nelson"
lastname = "mandela"
quote = """once said,"Education is the most powerful weapon which you can use to change the world." """

print(firstname.title()+" "+lastname.capitalize()+" "+quote)

famous_person = firstname.title()+" "+lastname.capitalize()+" "
#created a variable to clean code for famous person first and last name
famous_quote = famous_person+quote
#created another variable that includes the quote and first and last name variables
print(famous_quote)





strip_name = " James Reid "
strip_name1 = "\t James Reid2 "
strip_name2 = "\n James Reid3 "
strip_name3 = "\n\t James Reid4 "
print(strip_name+strip_name1+strip_name2+strip_name3)
print(strip_name.lstrip()+strip_name1.rstrip()+strip_name2.strip()+strip_name3)
