def get_choice(prompt, options):
    print(f"\n{prompt}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print(f"  Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("  Invalid input - please enter a number.")

def know_star_sign():
    star_sign = get_choice(
    "Do you know your Star Sign?",
    ["Yes", "No"])
    if star_sign == "Yes":
         print("That's great could you type it in")
    elif star_sign == "No":
        print("Ok what is your date of Birth: Day, Month")
    return star_sign

def enter_star_sign():

    valid_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    chosen_sign = input("Please type your Star Sign: ").title().strip()

    while chosen_sign not in valid_signs:
        print(f"{chosen_sign} is not a valid Star Sign,please try again")
        chosen_sign = input("That is not a valid Star Sign, please try again: ").title().strip()

    print(f"Your Star Sign is {chosen_sign}")
    return chosen_sign

def zodiac_info(sign):
    dates = {
        "Aries": "March 21 - April 19",
        "Taurus": "April 20 - May 20",
        "Gemini": "May 21 - June 20",
        "Cancer": "June 21 - July 22",
        "Leo": "July 23 - August 22",
        "Virgo": "August 23 - September 22",
        "Libra": "September 23 - October 22",
        "Scorpio": "October 23 - November 21",
        "Sagittarius": "November 22 - December 21",
        "Capricorn": "December 22 - January 19",
        "Aquarius": "January 20 - February 18",
        "Pisces": "February 19 - March 20"
    }


    if sign == "Aries":
        print("Symbol: ♈ Ram")
        print("Element: Fire")
        print("Info: Bold and fearless, Aries are natural leaders who charge headfirst into any challenge.")
    elif sign == "Taurus":
        print("Symbol: ♉ Bull")
        print("Element: Earth")
        print("Info: Reliable and strong-willed, Taurus values stability, loyalty, and the comforts of life.")
    elif sign == "Gemini":
        print("Symbol: ♊ Twins")
        print("Element: Air")
        print("Info: Curious and quick-witted, Gemini thrives on communication and new experiences.")
    elif sign == "Cancer":
        print("Symbol: ♋ Crab")
        print("Element: Water")
        print("Info: Emotional and protective, Cancer deeply values home, family, and emotional security.")
    elif sign == "Leo":
        print("Symbol: ♌ Lion")
        print("Element: Fire")
        print("Info: Charismatic and confident, Leo loves being in the spotlight and inspires others.")
    elif sign == "Virgo":
        print("Symbol: ♍ Virgin")
        print("Element: Earth")
        print("Info: Analytical and precise, Virgo strives for perfection and practical solutions.")
    elif sign == "Libra":
        print("Symbol: ♎ Scales")
        print("Element: Air")
        print("Info: Diplomatic and fair-minded, Libra seeks balance and harmony in all things.")
    elif sign == "Scorpio":
        print("Symbol: ♏ Scorpion")
        print("Element: Water")
        print("Info: Intense and determined, Scorpio is passionate and unafraid of hidden truths.")
    elif sign == "Sagittarius":
        print("Symbol: ♐ Archer")
        print("Element: Fire")
        print("Info: Adventurous and optimistic, Sagittarius seeks freedom and new horizons.")
    elif sign == "Capricorn":
        print("Symbol: ♑ Goat")
        print("Element: Earth")
        print("Info: Ambitious and disciplined, Capricorn works hard to achieve long-term success.")
    elif sign == "Aquarius":
        print("Symbol: ♒ Water Bearer")
        print("Element: Air")
        print("Info: Innovative and independent, Aquarius thinks differently and values freedom.")
    elif sign == "Pisces":
        print("Symbol: ♓ Fish")
        print("Element: Water")
        print("Info: Compassionate and intuitive, Pisces is deeply imaginative and empathetic.")
    print(f"Dates: {sign} is from {dates[sign]}")
def find_month():
    month= get_choice(
    "What  Month were you born in? ",
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"]
    )
    print(f" You were born in {month}")
    return month

def find_day(month):
    if month in ["January", "March", "May", "July", "August", "October", "December"]:
        max_day = 31
    elif month in ["April", "June", "September", "November"]:
        max_day = 30
    elif month == "February":
        max_day = 29

    while True:
        try:
            day = int(input(f"Please enter what date in {month} you were born on: "))
            if 1 <= day <= max_day:
              print(f"This looks correct, you were born on the {day}, {month}")
              return day
            else :
              print("this doesn't look like a valid date. Please try again.")

        except ValueError:(
            print("Please enter a valid number."))



def sign_birthday(month, day):
    month_num = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    month = month_num[month]

    if month == 3 and day >=21:
        sign = "Aries"
    elif month == 4 and day <=19:
        sign = "Aries"
    elif month == 4 and day >= 20:
        sign = "Taurus"
    elif month == 5 and day <=20:
        sign = "Taurus"
    elif month == 5 and day >=21:
        sign = "Gemini"
    elif month == 6 and day <=21:
        sign = "Gemini"
    elif month == 6 and day >=22:
        sign = "Cancer"
    elif month == 7 and day <=22:
        sign = "Cancer"
    elif month == 7 and day >=23:
        sign = "Leo"
    elif month == 8 and day <=22:
        sign = "Leo"
    elif month == 8 and day >=23:
        sign = "Virgo"
    elif month == 9 and day <=22:
        sign = "Virgo"
    elif month == 9 and day >=23:
        sign = "Libra"
    elif month == 10 and day <=23:
        sign = "Libra"
    elif month == 10 and day >= 24:
        sign = "Scorpio"
    elif month == 11 and day <=21:
        sign = "Scorpio"
    elif month == 11 and day >=22:
        sign = "Sagittarius"
    elif month == 12 and day <=21:
        sign = "Sagittarius"
    elif month == 12 and day >=22:
        sign = "Capricorn"
    elif month == 1 and day <=19:
        sign = "Capricorn"
    elif month == 1 and day >=20:
        sign = "Aquarius"
    elif month == 2 and day <=18:
        sign = "Aquarius"
    elif month == 2 and day >=19:
        sign = "Pisces"
    elif month == 3 and day <=20:
        sign = "Pisces"
    return sign





def main():
    print("Star Sign Programme")

    known_sign= know_star_sign()

    if known_sign == "Yes":
        sign = enter_star_sign()

    else:
        month = find_month()
        day = find_day(month)
        sign = sign_birthday(month, day)
        print(f"\nYour star sign is {sign}")

    input("\nPress Enter to continue...")
    print("\n" * 20)
    zodiac_info(sign)
    input("\nPress Enter to continue...")

    while True:
        retry = get_choice("Would you like to try again?", ["Yes", "No"])
        if retry == "No":
            print("\nThanks for using the Star Sign Programme!")
            break

        else:
            # ask again if they know their sign
            known_sign = know_star_sign()

            if known_sign == "Yes":
                sign = enter_star_sign()
            else:
                month = find_month()
                day = find_day(month)
                sign = sign_birthday(month, day)
                print(f"\nYour star sign is {sign}")

            input("\nPress Enter to see your Zodiac info...")
            zodiac_info(sign)
            input("\nPress Enter to continue...")


main()