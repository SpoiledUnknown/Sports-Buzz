import mysql.connector



# Database setup
config = {
    'host':'host_name',
    'user':'user_name',
    'password':'your_password',
    'database':'your_database_name'
}

connection = mysql.connector.connect(**config)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS your_database_name")

# Create the cricket table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cricket (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact_number BIGINT NOT NULL,
    total_matches INT NOT NULL,
    total_run INT,
    total_wickets INT,
    average_run INT,
    average_wicket INT
)
""")

# Create the football table
cursor.execute("""
CREATE TABLE IF NOT EXISTS football (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact_number BIGINT NOT NULL,
    total_matches INT NOT NULL,
    total_goals INT,
    total_tackles INT,
    total_saves INT
)
""")

# Create the basketball table
cursor.execute("""
CREATE TABLE IF NOT EXISTS basketball (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    contact_number BIGINT NOT NULL,
    total_matches INT NOT NULL,
    player_position VARCHAR(50),
    total_points INT,
    average_points INT,
    total_bbsaves INT
)
""")

#handle the process of registeration
def handle_registration():
    #name
    while True:
        user_name = input("Enter your full name: ")

        if not user_name.isalpha():
            print("The name can only contain alphabetical letters. Please enter again.")
        else:
            break

    #age
    while True:
        user_age = input("Enter your age please: ")

        if not (user_age.isnumeric()):
            print("The age should contain numbers. Please enter again.")
        else:
            break

    user_age = int(user_age)

    #gender
    while True:
        user_gender = input("Enter your gender (male or female): ")

        if not user_gender.isalpha() or not user_gender.lower() == "male" and not user_gender.lower() == "female":
            print("The gender can only contain alphabetical letters (male or female). Please enter again.")
        else:
            break

    #phone number
    while True:
        contact_number = input("Enter your contact number please: ")

        if not (contact_number.isnumeric() and len(contact_number) == 10):
            print("The contact number should be exactly 10 digits. Please enter again.")
        else:
            break

    contact_number = int(contact_number)

    #sports name
    sports_name = input("Enter the sport you want to register yourself for: ")
    if sports_name.isdigit() :
        sports_name = input("The sport name can only contains Alphabetical letter. Enter again: ")


    if sports_name.lower() == "cricket":
       
        #number of matches
        while True:
            total_matches = input("Enter your total numbers of matches please: ")

            if not (total_matches.isnumeric()):
                print("The total numbers of matches should contain numbers. Please enter again.")
            else:
                break

        total_matches = int(total_matches)
       
       
        #total runs
        while True:
            total_run = input("Enter your total numbers of runs you scored please: ")

            if not (total_run.isnumeric()):
                print("The total numbers of runs you scored should contain numbers. Please enter again.")
            else:
                break

        total_run = int(total_run)
     
        #total wickets
        while True:
            total_wickets = input("Enter your total wickets you have taken please: ")

            if not (total_wickets.isnumeric()):
                print("The total wickets you have taken should contain numbers. Please enter again.")
            else:
                break

        total_wickets = int(total_wickets)

        #average runs
        while True:
            average_run = input("Enter your average run you scored please: ")

            if not (average_run.isnumeric()):
                print("The average run you scored should contain numbers. Please enter again.")
            else:
                break

        average_run = int(average_run)
               
        #average wicket
        while True:
            average_wicket = input("Enter your average wickets you took please: ")

            if not (average_wicket.isnumeric()):
                print("The average wicket you took should contain numbers. Please enter again.")
            else:
                break

        average_wicket = int(average_wicket)

        insert_cricket_query = """
            INSERT INTO cricket (name, age, gender, contact_number, total_matches,
                                     total_run, total_wickets, average_run, average_wicket)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cricket_data = (user_name, user_age, user_gender, contact_number, total_matches,
                        total_run, total_wickets, average_run, average_wicket)

        cursor.execute(insert_cricket_query, cricket_data)

    elif sports_name.lower() == "football":
       
        #number of matches
        while True:
            total_matches = input("Enter your total numbers of matches please: ")

            if not (total_matches.isnumeric()):
                print("The total numbers of matches should contain numbers. Please enter again.")
            else:
                break

        total_matches = int(total_matches)

        #total goals
        while True:
            total_goals = input("Enter the total goals you scored please: ")

            if not (total_goals.isnumeric()):
                print("The number of goals you have entered should contain numbers. Please enter again.")
            else:
                break

        total_goals = int(total_goals)

        #total tackles
        while True:
            total_tackles = input("Enter the total successfull tackles you have performed please: ")

            if not (total_tackles.isnumeric()):
                print("The number of tackles you have entered should contain numbers. Please enter again.")
            else:
                break

        total_tackles = int(total_tackles)

       
        total_saves = None
        while True:
            continue_input = input("If you have also played as goalkeeper then write 'yes' otherwise 'no':\n")
            if continue_input.lower() == "yes":    
                #total saves
                while True:
                    total_saves = input("Enter the total goals you gave saved please: ")

                    if not (total_saves.isnumeric()):
                        print("The number of saves you have entered should contain numbers. Please enter again.")
                    else:
                        break
                total_saves = int(total_saves)
                break
            elif continue_input.lower()=='no':
                break
            else:
                print('Invalid input !!')
                continue
                           
        # Insert football-related data into MySQL
        insert_football_query = """
            INSERT INTO football (name, age, gender, contact_number, total_matches,
                                     total_goals, total_tackles, total_saves)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        football_data = (user_name, user_age, user_gender, contact_number, total_matches,
                        total_goals, total_tackles, total_saves if 'total_saves' in locals() else None)

        cursor.execute(insert_football_query, football_data)

    elif sports_name.lower() == "basketball":
       
        #number of matches
        while True:
            total_matches = input("Enter your total numbers of matches please: ")

            if not (total_matches.isnumeric()):
                print("The total numbers of matches should contain numbers. Please enter again.")
            else:
                break

        total_matches = int(total_matches)

        #player position
        while True:
            player_position = input("What were your position in the match: ")

            if not player_position.isalpha():
                print("Player position cannot be a number. Try again:\n")
            else:
                break
           
        #total points
        while True:
            total_points = input("Enter the total points you gained in baskets: ")

            if not (total_points.isnumeric()):
                print("The number of points you have entered should contain numbers. Please enter again.")
            else:
                break

        total_points = int(total_points)

        #average points
        while True:
            average_points = input("Enter the average points you have gained: ")

            if not (average_points.isnumeric()):
                print("The number of points you have entered should contain numbers. Please enter again.")
            else:
                break

        average_points = int(average_points)

        #total bbsaves
        while True:
            total_bbsaves = input("Enter the totals points you have saved: ")

            if not (total_bbsaves.isnumeric()):
                print("The number of saves you have entered should contain numbers. Please enter again.")
            else:
                break

        total_bbsaves = int(total_bbsaves)

        # Insert basketball-related data into MySQL
        insert_basketball_query = """
            INSERT INTO basketball (name, age, gender, contact_number, total_matches,
                                     player_position, total_points, average_points, total_bbsaves)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        basketball_data = (user_name, user_age, user_gender, contact_number, total_matches,
                           player_position, total_points, average_points, total_bbsaves)

        cursor.execute(insert_basketball_query, basketball_data)
   
    else :
        print("Sorry, we currently don't support this game. Press any key to continue ! ")
        return

    confirmation = input('Wanna save changes?(write y for yes or n for no):\n')
    if confirmation.lower() == "y" or confirmation.lower() == "yes":
        connection.commit()
        print(f"Database updated successfully!\n")
    else:
        print("Changes not saved.")

def get_player_info():
    name_of_sport = input('Enter the name sport: ')
   
    # Define a dictionary to map sports to their corresponding columns
    sport_columns = {
        'cricket': ['name', 'age', 'total_matches', 'total_run', 'total_wickets', 'average_run', 'average_wicket'],
        'football': ['name', 'age', 'total_matches', 'total_goals', 'total_tackles', 'total_saves'],
        'basketball': ['name', 'age', 'total_matches', 'player_position', 'total_points', 'average_points', 'total_bbsaves']
    }

    # Check if the specified sport is supported
    if name_of_sport.lower() not in sport_columns:
        print("Sorry, we currently don't support this game.")
        return

    columns = sport_columns[name_of_sport.lower()]
    column_names = ', '.join(columns)

    # Construct the query with the WHERE clause
    query = f"SELECT {column_names} FROM {name_of_sport.lower()}"

    cursor.execute(query)

    results = cursor.fetchall()

    if results:
        # Display the player information
        print("\nPlayer Information:")
        for result in results:
            for name, value in zip(columns, result):
                print(f"{name.capitalize()}: {value}")
            print("---")
    else:
        print(f"No players found for the sport: {name_of_sport}")

               
#handling the inputs for starting the session
while True:
    user_session = input("\nDo you want to get player info, register as a player, or quit?\n>>(write getinfo, register, or quit/exit): \n")

    if user_session.lower() == "register":
        handle_registration()
    elif user_session.lower() == "getinfo":
        get_player_info()
    elif user_session.lower() == "quit" or user_session.lower() == "exit":
        break
    else:
        print("Invalid option. Please choose 'getinfo', 'register', or 'quit'/'exit'.")

#***************end of program ***************#