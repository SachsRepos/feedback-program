first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = str(first_name.capitalize() + " " + last_name.upper())
print("Hey " + first_name.capitalize() + "! Do you mind spending a minute to rate our product? (y/n)")
command = input("> ")
command = command.lower()
if command == "y" or command == "yes": # accepts both values 'y' and 'yes'
    rating = input("Rate our service on a scale of 10 ")
    special_char = """~`!@#$%^&*()_-+={[]}|'":;<,>\.?/"""
    if rating.isalpha() == True:
        print("What does that mean?")
        rating = "none"
    elif any(character in special_char for character in rating):
        print("What does that mean?")
        rating = "none"
    elif rating.isnumeric() == True:
        rating = int(rating)
        if rating <= 4:
            print(str(rating) + ". OK!")
        elif rating == 5:
            print(str(rating) + ", Thanks!")
        elif rating >= 5:
            if rating > 10:
                print("More than 10! Thanks!")
                rating = 10
            else:
                print(str(rating) + "! Thanks!")
elif command == "n" or command == "no": # accepts both values 'n' and 'no'
    print("Thanks for using our product!")
    rating ="none"
else:
    print("Please enter a valid letter!")
    rating = "none"
feedback = input("Would you like to enter feedback? (y/n) ")
feedback = feedback.lower()
if feedback == "n" or feedback == "no": # accepts both values 'n' and 'no'
    print("Thanks!")
    feedback_if_yes = "none"
elif feedback == "y" or feedback == "yes": # accepts both values 'y' and 'yes'
    feedback_if_yes = input("Please enter your experience with this product. ")
    print("Thank you! We will definitely look into it.")
else:
    print("What do you mean?")
    feedback_if_yes = "none"
output_display = open("output.txt", "w")
str_firstname = repr(first_name)
output_display.write("First Name = " + str_firstname + "\n")
str_lastname = repr(last_name)
output_display.write("Last Name = " + str_lastname + "\n")
str_rating = repr(str(rating))
output_display.write("Rating /10 = " + str_rating + "\n")
str_feedback_if_yes = repr(feedback_if_yes)
output_display.write("Feedback = " + str_feedback_if_yes + "\n")
output_display.close()
