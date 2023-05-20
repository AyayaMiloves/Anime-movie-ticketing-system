# ANIME MOVIES TICKETING SYStem
from time import *
from All_list import *
from some_functions import *
animes = [latest_anime, action_anime, romance_anime, psychological_anime, slice_of_life_anime, drama_anime]
snck_drnk = [snack_dict, drink_dict]
print(
    Fore.LIGHTCYAN_EX + "----------------------WELCOME TO THE ANIME MOVIES THEATER----------------------" + Style.RESET_ALL)
sleep(0.5)
print(
    Fore.LIGHTCYAN_EX + "-----^_^----^_^HERE YOU CAN ENJOY DIFFERENT ANIME MOVIE YOU WANT^_^----^_^---\n" + Style.RESET_ALL)
import re

def get_name_input():
    while True:
        name = input("Enter your name: ")
        if re.match('^[a-zA-Z ]+$', name):
            return name
        else:
            print("Invalid name.")
name = get_name_input()
loading_dots()
sleep(0.7)
# Display choices: all anime and their genres
print(Fore.CYAN + "---------------------AVAILABLE MOVIES AND THEIR GENRE----------------------\n" + Style.RESET_ALL)
print(Fore.GREEN + """~~~[LATEST RELEASE]~~~                                     ~~~[ACTION ANIME]~~~
Juju2tsu Kaisen 0: Thedw Movie                       Kimetsu no Yaiba: Mugen Ressha-Hen
Dragon Ball Super: Super Hero                      Demon Slayer: Mugen Train
One Piece Film Red (CAMRIP)                        Sword Art Online: Alicization
Suzume no Tojimari                                 My Hero Academia: Hero Rising   
That Time I Reincarnated as a Slime: The Movie     One Piece Movie 14: Stampede
Bubble                                             The Last: Naruto The Movie
Quintessential Quintuplets: The Movie\n
~~~[ROMANCE ANIME]~~~                                   ~~~[PSYCHOLOGICAL ANIME]~~~
Your Name                                          The Promised Neverland
5 Centimeters per Second                           Death Note
Kimi no Na wa                                      Parasyte: The Maxim
Rascal Does Not Dream of Bunny Girl Senpai         Tokyo Ghoul
Violet Evergarden: The Movie                       Erased
Weathering with You                                Psycho-Pass
A Silent Voice                                     Boku dake ga Inai Machi
Hello World\n
~~~[SLICE OF LIFE ANIME]~~~                              ~~~[DRAMA ANIME]~~~
k-On!                                              Your Lie In April
Yuru Camp                                          Anohana: The Flower We Saw That Day
Non Non Biyori                                     Clannad
A Place Further Than the Universe                  Grave of the Fireflies
Barakamon                                          I Want To Eat Your Pancreas
                                                   Belle
                                                   Spirited Away""" + Style.RESET_ALL)
print("----------------------------------------------------------------------------------")


def main():
    global qtysnckdrnk, snck, qtysnck, qtydrnk, drnk, snack_list, drink_list, snck_drnk_list, num

    def anime_movie():
        match genre_choice:
            case 1:
                return latest_anime()
            case 2:
                return action_anime()
            case 3:
                return romance_anime()
            case 4:
                return psychological_anime()
            case 5:
                return sliceoflife_anime()
            case other:
                return drama_anime()
    genre_choice = genre()
    movie = anime_movie()
    movie_dict = animes[genre_choice - 1]
    key = list(movie_dict.keys())
    movie_name = key[movie - 1]
    quantity = qty()
    price = movie_dict[movie_name]
    movie_price = price * quantity
    time = choose_time()
    day = choose_day()
    seat = seats()
    def qty_snck():
        while 1:
            try:
                while 1:
                    quantity = int(input("How many of this do you want to buy? "))
                    if quantity > 0:
                        return quantity
                    else:
                        print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)

    def qty_drnk():
        while 1:
            try:
                while 1:
                    quantity = int(input("How many of this do you want to buy? "))
                    if quantity > 0:
                        return quantity
                    else:
                        print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)

    while 1:
        try:
            num = int(input("""Do you want to add snacks and drinks?
    [1] YES
    [2] NO
    Choose: """))
            if num > 2 or num < 0:
                raise ValueError(Fore.RED + "Invalid input!!" + Style.RESET_ALL)
            else:
                break
        except ValueError:
            print(Fore.RED + "Please check your input!!" + Style.RESET_ALL)
    snck_name = "NONE"
    drnk_name = "NONE"
    snck_price = 0
    drnk_price = 0
    qtysnck = 0
    qtydrnk = 0
    match num:
        case 1:
            while 1:
                snck = snacks()
                if snck == 7:
                    break
                else:
                    qtysnck += qty_snck()
                    snck_dict = snck_drnk[0]
                    snck_key = list(snck_dict.keys())
                    snck_name = snck_key[snck]
                    price_snck = snck_dict[snck_name]
                    snck_price += price_snck * qtysnck
                    break
            while 1:
                drnk = drinks()
                if drnk == 6:
                    break
                else:
                    qtydrnk += qty_drnk()
                    drnk_dict = snck_drnk[1]
                    drnk_key = list(drnk_dict.keys())
                    drnk_name = drnk_key[drnk]
                    price_drnk = drnk_dict[drnk_name]
                    drnk_price += price_drnk * qtydrnk
                    break
        case 2:
            pass
    total_price = movie_price + snck_price + drnk_price
    loading_dots()
    print(f"""THIS IS THE TOTAL PRICE
    Movie   : {movie_name}  ~~~~~~~~~ {movie_price}₱
    Snack   : {snck_name}  ~~~~~~~~~ {snck_price}₱
    Drinks  : {drnk_name}  ~~~~~~~~~ {drnk_price}₱
    Total   : {total_price}₱""")

    def payment():
        while 1:
            try:
                pay = int(input("Enter your payment: "))
                if pay >= total_price:
                    return pay
                else:
                    print(Fore.RED + "Please pay exact amount!!" + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Please enter valid input!" + Style.RESET_ALL)

    pay = payment()
    change = pay - total_price
    costumer_id = idgenerate()
    Purchase_complete()
    print(Fore.LIGHTWHITE_EX + f"\bHere is your Change: {change}₱" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + f"""\bTHANK YOU FOR PURCHASING A TICKET AND ENJOY
    \b
You can check your receipt in the Receipt.txt file. with the ID NO. {costumer_id}""")

    from datetime import datetime
    # Get the current date and time
    current_datetime = datetime.now()
    # Format the date and time as strings
    current_date_str = current_datetime.strftime("%Y-%m-%d")
    current_time_str = current_datetime.strftime("%H:%M:%S")
    # the "text" variable is for the write file for the receipt
    text = f"""------------------RECEIPT ID NO. {costumer_id}------------------
                            Date: {current_date_str} {current_time_str}
NAME          : {name.title().strip()}
MOVIE         : Ticket x{quantity} {movie_name} - total: {movie_price:,}₱
DATE and TIME : {day} {time}
SEAT          : {seat}
SNACKS        : {snck_name} x{qtysnck} - total: {snck_price:,}₱
DRINKS        : {drnk_name} x{qtydrnk} - total: {drnk_price:,}₱
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TOTAL         : {total_price:,}₱
CASH          : {pay:,}₱
CHANGE        : {change:,}₱
------------------THANK YOU AND ENJOY THE SHOW!!------------------\n"""
    # Writing the text to the file
    try:
        with open("Receipt.txt", "a") as file:
            file.write(text + "\n")
    except IOError as e:
        print(f"An error occurred while writing the receipt: {e}")
def genre():
    genres = ['latest_anime', 'action_anime', 'romance_anime', 'psychological_anime', 'slice_of_life_anime',
              'drama_anime']
    while True:
        # I use input function and triple quotes to display all the choices
        try:
            genre_choice = int(input("""------------------SELECT ANIME GENRE------------------
            [1] Latest Release
            [2] Action
            [3] Romance
            [4] Psychological
            [5] Slice of life
            [6] Drama
YOUR CHOICE: """))
            if not genre_choice <= 6 or not genre_choice > 0:
                raise ValueError("Choice Invalid!!")
            loading_dots()
            return genre_choice
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)
        # Check if the input is in the choices using if statement


def latest_anime():
    while 1:
        try:
            latest_anime = int(input("""------------------THESE ARE THE LATEST RELEASE ANIME------------------
            [1] Jujutsu Kaisen 0: The Movie                    ~ 240₱
            [2] Dragon Ball Super: Super Hero                  ~ 200₱
            [3] One Piece Film Red (CAMRIP)                    ~ 500₱
            [4] Suzume no Tojimari                             ~ 600₱
            [5] That Time I Reincarnated as a Slime: The Movie ~ 300₱
            [6] Bubble                                         ~ 200₱
            [7] Quintessential Quintuplets: The Movie          ~ 200₱
CHOOSE AN ANIME: """))
            if not latest_anime <= 7 or not latest_anime > 0:
                raise ValueError(Fore.RED + "Choice Invalid!!")
            return latest_anime

        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def action_anime():
    while 1:
        try:
            action_anime = int(input("""------------------THESE ARE THE ACTION ANIME------------------
            [1] Kimetsu no Yaiba: Mugen Ressha-Hen    ~ 290₱
            [2] Demon Slayer: Mugen Train             ~ 200₱
            [3] sword art online: Alicization         ~ 400₱
            [4] My Hero Academia: Heroes Rising       ~ 500₱
            [5] One Piece Movie 14: Stampede          ~ 300₱
            [6] The Last: Naruto the Movie            ~ 200₱
CHOOSE AN ANIME: """))
            if not action_anime <= 6 or not action_anime > 0:
                raise ValueError("Choice Invalid!!")
            return action_anime
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def romance_anime():
    while 1:
        try:
            romance_anime = int(input("""------------------THESE ARE THE ROMANCE ANIME------------------
            [1] Your Name                                    ~ 200₱
            [2] 5 Centimeters per Second                     ~ 200₱
            [3] Kimi no Na wa                                ~ 400₱
            [4] Rascal Does Not Dream of Bunny Girl Senpai   ~ 500₱
            [5] Violet Evergarden: The Movie                 ~ 300₱
            [6] Weathering with You                          ~ 200₱
            [7] A Silent Voice                               ~ 400₱
            [8] Hello World                                  ~ 300₱
CHOOSE AN ANIME: """))
            if not romance_anime <= 8 or not romance_anime > 0:
                raise ValueError("Choice Invalid!!")
            return romance_anime
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def psychological_anime():
    while 1:
        try:
            psychological_anime = int(input("""------------------THESE ARE THE PSYCHOLOGICAL ANIME------------------
            [1] The Promised Neverland   ~ 200₱
            [2] Death Note               ~ 200₱
            [3] Parasyte: The Maxim      ~ 400₱
            [4] Tokyo Ghoul              ~ 200₱
            [5] Erased                   ~ 300₱
            [6] Psycho-Pass              ~ 200₱
            [7] Boku dake ga Inai Machi  ~ 400₱
CHOOSE AN ANIME: """))
            if not psychological_anime <= 7 or not psychological_anime > 0:
                raise ValueError("Choice Invalid!!")
            return psychological_anime
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def sliceoflife_anime():
    while 1:
        try:
            sliceoflife_anime = int(input("""------------------THESE ARE THE SLICE OF LIFE ANIME------------------
            [1] K-On!                              ~ 200₱
            [2] Yuru Camp                          ~ 300₱
            [3] Non Non Biyori                     ~ 400₱
            [4] A Place Further Than the Universe  ~ 300₱
            [5] Barakamon                          ~ 300₱
CHOOSE AN ANIME: """))
            if not sliceoflife_anime <= 5 or not sliceoflife_anime > 0:
                raise ValueError("Choice Invalid!!")
            return sliceoflife_anime
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def drama_anime():
    while 1:
        try:
            drama_anime = int(input("""------------------THESE ARE THE DRAMA ANIME------------------
            [1] Your Lie in April                    ~ 300₱
            [2] Anohana: The Flower We Saw That Day  ~ 250₱
            [3] Clannad                              ~ 350₱
            [4] Grave of the Fireflies               ~ 200₱
            [5] I Want to Eat Your Pancreas          ~ 200₱
            [6] Belle                                ~ 190₱
            [7] Spirited Away                        ~ 300₱
CHOOSE AN ANIME: """))
            if not drama_anime <= 7 or not drama_anime > 0:
                raise ValueError("Choice Invalid!!")
            return drama_anime
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def qty():
    while 1:
        try:
            while 1:
                quantity = int(input("How many tickets do you want to buy? "))
                if quantity > 0:
                    return quantity
                else:
                    print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Please enter the quantity that you want to buy!!" + Style.RESET_ALL)


def choose_day():
    date_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    while 1:
        try:
            day_choice = int(input("""------------------DAYS AVAILABLE------------------
            [1] Monday     [2] Tuesday     [3] Wednesday
            [4] Thursday    [5] Friday    [6] Saturday
CHOOSE DAY: """))
            if not day_choice <= 6 or not day_choice > 0:
                raise ValueError("Choice Invalid!!")
            return date_list[day_choice - 1]
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def choose_time():
    time_list = ['8:00am - 10:30am', '10:40am - 12:00pm', '12:15pm - 1:45pm', '2:00pm - 3:40pm']
    while 1:
        try:
            time_choice = int(input(f"""------------------TIME AVAILABLE------------------
            [1] 8:00am - 10:30am
            [2] 10:40am - 12:00pm
            [3] 12:15pm - 1:45pm
            [4] 2:00pm - 3:40pm
CHOOSE TIME: """))
            if not time_choice <= 4 or not time_choice > 0:
                raise ValueError("Choice Invalid!!")
            return time_list[time_choice - 1]
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def seats():
    seat_list = [
        "A1", "A2", "A3", "A4", "A5",
        "A6", "A7", "A8", "A9", "A10", "B1", "B2", "B3", "B4", "B5",
        "B6", "B7", "B8", "B9", "B10",
    ]
    while 1:
        try:
            seat_choice = int(input("""------------------SEATS AVAILABLE------------------\n
            [1] A1, [2] A2, [3] A3, [4] A4, [5] A5,
            [6] A6, [7] A7, [8] A8, [9] A9, [10] A10,
            [11] B1, [12] B2, [13] B3, [14] B4, [15] B5,
            [16] B6, [17] B7, [18] B8, [19] B9, [20] B10
CHOOSE A SEAT: """))
            if not seat_choice <= 20 or not seat_choice > 0:
                raise ValueError("Invalid input!!")
            return seat_list[seat_choice - 1]
        except ValueError:
            print(Fore.RED + "Sorry, Please check your input!" + Style.RESET_ALL)


def snacks():
    while 1:
        try:
            while 1:
                option = abs(int(input("""------------------AVAILABLE SNACKS--------------------  
                [1]Pop-corn        50
                [2]Cookies         65
                [3]Chocolates      45
                [4]Nuts            40
                [5]Chips           35
                [6]Pretzels        55
                [7]I DONT WANT SNACKS
Select an option: """)))
                if option <= 6 and option > 0:
                    return option - 1
                elif option == 7:
                    return 7
                else:
                    print(Fore.RED + "Please choose only in the option!" + Style.RESET_ALL)
                    pass
        except ValueError:
            print(Fore.RED + "Please enter a number only" + Style.RESET_ALL)


def drinks():
    while 1:
        try:
            while 1:
                option = abs(int(input("""------------------AVAILABLE DRINKS--------------------  
                [1]Coke                35
                [2]Apple juice         45
                [3]Fanta               65
                [4]Water               20
                [5]Tea                 30
                [6]I DONT WANT DRINKS
Select an option: """)))
                if option <= 5 or not option > 0:
                    return option - 1
                elif option == 6:
                    return 6
                else:
                    print(Fore.RED + "Please choose only in the option!" + Style.RESET_ALL)
                    pass
        except ValueError:
            print(Fore.RED + "Please enter a number only" + Style.RESET_ALL)
main()
