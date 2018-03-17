import random

def end():

    chocie = input("Would you like to pick anther name? [Y/N} \n")

    if chocie == "Y" or "y" or "yes" or "Yes":
        start()
    else:
        exit(0)

def male():
    names = ["Aspen", "Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James", "Alexander", "Michael",
             "Benjamin", "Elijah", "Daniel", "Aiden", "Logan", "Matthew", "Lucas", "Jackson", "David",
             "Oliver", "Jayden", "Joseph", "Gabriel", "Sammuel", "Carter", "Anthony", "John", "Dylan",
             "Luke", "Henry", "Andrew"]

    random_num = random.randrange(1,31)
    name = names[random_num]

    print("Your little boy's name is " + name)

    end()

def female():
    names = ["Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte", "Harper,"
            "Madison", "Amelia", "Elizabeth", "Sofia", "Evelyn", "Avery", "Chloe", "Ella", "Grace", "Victoria",
             "Aubrey", "Scarlett", "Zoey", "Addison" "Lily", "Lillian", "Natalie", "Hannah", "Aria", "Layla "]

    random_num = random.randrange(1,31)
    name = names[random_num]

    print("Your little girl's name is " + name)

    end()


def start():
    print("Welcome to the Baby Name Generator")
    print("This program picks the most popular names right now.")
    gender = input("Enter the gender of your baby \n")

    if (gender == "male") or (gender == "Male") or (gender == "boy") or (gender == "Boy"):
        male()
    elif (gender == "female") or (gender =="Female") or (gender == "girl") or  (gender == "Girl"):
        female()
    else:
        exit(0)



start()




