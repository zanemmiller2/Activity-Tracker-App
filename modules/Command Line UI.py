# Author: Zane Miller
# Date: 05/07/2022
# Email: millzane@oregonstate.edu
# Description: Module for running the Command Line User Interface

import FilteredSleepClass as Sleep
import FilteredRestingHRClass as HR
import FilteredWorkoutClass as Workout


def get_user_input_add():
    """
    Gets the user input from command line
    """
    # What kind of table do you want to create?
    get_user_input_str_add = str(input("What data would you like to add "
                                       "(sleep, "
                                       "resting heart rate, "
                                       "activity): "))

    return get_user_input_str_add


def get_user_input_view():
    """
    Gets the user input from command line
    """
    # What kind of table do you want to create?
    get_user_input_str_view = str(input("What data would you like to view "
                                        "(sleep, "
                                        "resting heart rate, "
                                        "activity): "))

    return get_user_input_str_view


def get_user_input_add_or_view():
    """
    Gets the user input from command line
    """
    # What kind of table do you want to create?
    get_user_input_str_add_or_view = str(
        input("Would you like to view or add data? "
              "(view/add): "))

    return get_user_input_str_add_or_view


def unfiltered_file_settings(data_type):
    """
    Sets default file naming settings for unfiltered csv
    """

    set_unfiltered_csv = None
    # Select source file for upload
    if data_type == 'activity':
        set_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                             'Activity-Tracker-App-Data/' \
                             'apple_health_export/' \
                             'Extracted_data/Workout.csv'

    elif data_type == 'sleep':
        set_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                             'Activity-Tracker-App-Data/' \
                             'apple_health_export/' \
                             'Extracted_data/' \
                             'SleepAnalysis.csv'

    elif data_type == 'resting heart rate':
        set_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                             'Activity-Tracker-App-Data/' \
                             'apple_health_export/' \
                             'Extracted_data/' \
                             'RestingHeartRate.csv'

    return set_unfiltered_csv


def filtered_file_settings(data_type):
    """
    Sets default file naming settings for filtered csv
    """
    set_filtered_csv = None
    # Selects destination files for upload
    if data_type == 'activity':
        set_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                           'Activity-Tracker-App/' \
                           'Workout_Filtered.csv'

    elif data_type == 'sleep':
        set_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                           'Activity-Tracker-App/' \
                           'Sleep_Filtered.csv'

    elif data_type == 'resting heart rate':
        set_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/' \
                           'Activity-Tracker-App/' \
                           'RestingHR_Filtered.csv'

    return set_filtered_csv


def import_default_sources_settings(data_type):
    """
    Defines the default import sources for filtered data
    """

    # What sources do you want to include in your upload?
    if data_type == 'activity':
        data_tables_types_sources = ['Zane’s Apple\xa0Watch',
                                     'Stryd',
                                     'Slopes',
                                     'ELEMNT']

    elif data_type == 'sleep':
        data_tables_types_sources = ['Autosleep',
                                     'Zane’s Apple\xa0Watch']

    elif data_type == 'resting heart rate':
        data_tables_types_sources = ['Zane’s Apple\xa0Watch']


def valid_input(check_user_input):
    """ Verifies user input is in list or not exit """

    check_user_input.lower()
    user_input_options = ['sleep', 'resting heart rate', 'activity']

    if check_user_input in user_input_options:
        return True

    else:
        return False


def login_configuration():
    """ Gets the loging configuration for fitnessTracker db """
    login_config = ["zanemiller",
                    "230Leafwoodct!",
                    "10.0.0.208",
                    3306,
                    'fitnessTracker']

    return login_config


def ask_connect_db(class_upload):
    """
    Asks user if they want to connect to the db or not?
        If yes -- connects to database.
        If not -- TODO DONT KNOW YET
    """
    # Do you want to connect to the database?
    db_connect = str(input("Would you like to connect to the "
                           "fitnessTracker Database? (y or n): "))

    if db_connect.lower() == 'y':
        login_config = login_configuration()

        class_upload.database_connect(user=login_config[0],
                                      password=login_config[1],
                                      host=login_config[2],
                                      port=login_config[3],
                                      database=login_config[4])
        return True
    else:
        print("Database connection not established ...\n")
        return False


def ask_create_table(class_upload):
    """
    Asks the user if they want to create a new table.
    Creates new db table if yes, asks the user for table title.
    If no: TODO
    """

    create_table_response = input("Do you want to create a new table? "
                                  "(y or n): ")

    if create_table_response == 'y':
        table_title = input("What would you like to call this table?: ")

        class_upload.create_new_table(table_title)

        print(f"'{table_title}' created ...\n")
        return True

    else:
        return False


def ask_filter_data(class_upload, user_input):
    """
    Asks the user if they want to upload an unfiltered csv
    """
    filter_response = input(f"Do you want to filter "
                            f"{user_input} data? (y or n): ")

    if filter_response.lower() == 'y':
        class_upload.filter_watch_data()
        print(f"{user_input} data filtered ...\n")
        return True

    else:
        return False


def ask_upload_filtered(class_upload, user_input):
    """
    Asks if the user wants to upload the filtered data to the database
    """
    upload_filtered_response = input("Do you want to upload the filtered "
                                     "data? (y or n): ")

    if upload_filtered_response.lower() == 'y':
        class_upload.upload_csv()
        print(f"{user_input} filtered data uploaded to database ...\n")
        return True

    else:
        return False


def ask_commit_changes(class_upload, user_input):
    """
    Asks if the user wants to upload the filtered data to the database
    """
    ask_commit_response = input("Do you want to commit the filtered "
                                "data? (y or n): ")

    if ask_commit_response.lower() == 'y':
        class_upload.commit_changes()
        print(f"{user_input} filtered data committed to database ...\n")
        return True

    else:
        return False


def ask_1week_hr(class_upload):
    """
    Asks the user if they want to view hr data
    """
    view_hr_response = input("Would you like to see your 1 week "
                             "average? (y or n): ")

    if view_hr_response == 'y':
        average_hr = class_upload.heart_rate_averages_one_week()

        if average_hr is None:
            print("Not enough data to display\n")
        else:
            print(f"Your average resting HR over the "
                  f"last week is {average_hr}\n")

        return True

    else:
        return False


def ask_1month_hr(class_upload):
    """
    Asks the user if they want to view hr data
    """
    view_hr_response = input("Would you like to see your 1 month "
                             "average? (y or n): ")

    if view_hr_response == 'y':
        average_hr = class_upload.heart_rate_averages_one_month()

        if average_hr is None:
            print("Not enough data to display\n")
        else:
            print(f"Your average resting HR over the "
                  f"last month is {average_hr}\n")

        return True
    else:
        return False


def ask_6month_hr(class_upload):
    """
    Asks the user if they want to view hr data
    """
    view_hr_response = input("Would you like to see your 6 month "
                             "average?(y or n): ")

    if view_hr_response == 'y':
        average_hr = class_upload.heart_rate_averages_six_month()

        if average_hr is None:
            print("Not enough data to display\n")
        else:
            print(f"Your average resting HR over the last "
                  f"6 months is {average_hr}\n")
        return True

    else:
        return False


def ask_1year_hr(class_upload):
    """
    Asks the user if they want to view hr data
    """
    view_hr_response = input("Would you like to see your 1 year "
                             "average? (y or n): ")

    if view_hr_response == 'y':
        average_hr = class_upload.heart_rate_averages_one_year()
        if average_hr is None:
            print("Not enough data to display\n")
        else:
            print(f"Your average resting HR over the "
                  f"last year is {average_hr}\n")

        return True

    else:
        return False


if __name__ == '__main__':

    user_input = get_user_input_add_or_view()

    if user_input == 'add':

        while True:
            # Get user input -- What data
            user_input_add = get_user_input_add()

            if user_input_add.lower() == 'exit':
                exit()

            # Valid entry -- create src/dst files and class instances
            if valid_input(user_input_add):
                # set source and destination files for data upload
                unfiltered_csv = unfiltered_file_settings(user_input_add)
                filtered_csv = filtered_file_settings(user_input_add)

                # Create class instances for data type as "upload"
                if user_input == 'sleep':
                    upload = Sleep.FilterDataUpload(unfiltered_csv,
                                                    filtered_csv,
                                                    user_input_add)
                elif user_input == 'resting heart rate':
                    upload = HR.FilterDataUpload(unfiltered_csv,
                                                 filtered_csv,
                                                 user_input_add)
                else:
                    upload = Workout.FilterDataUpload(unfiltered_csv,
                                                      filtered_csv,
                                                      user_input_add)

                # Ask if user wants to connect to db
                if not ask_connect_db(upload):
                    print("Please try again!\n")
                    continue

                # Ask if user wants to create new table
                if not ask_create_table(upload):
                    print("Please try again!\n")
                    continue

                # Ask if user wants to filter data
                if not ask_filter_data(upload, user_input_add):
                    print("Please try again!\n")
                    continue

                # Ask if the user wants to upload filtered data to database
                if not ask_upload_filtered(upload, user_input_add):
                    print("Please try again!")
                    continue

                # Ask the user if they want to commit changes to the database
                if not ask_commit_changes(upload, user_input_add):
                    print("Please try again!")
                    continue

                upload.close_connection()

            # Invalid entry -- try again
            else:
                print(f"{user_input_add} not an option! Try again ... ")
                continue

    elif user_input == 'view':
        while True:
            # Get user input -- What data
            user_input_view = get_user_input_view()

            if user_input_view.lower() == 'exit':
                exit()

            # Valid entry -- create src/dst files and class instances
            if valid_input(user_input_view):

                # set source and destination files for data upload
                unfiltered_csv = unfiltered_file_settings(user_input_view)
                filtered_csv = filtered_file_settings(user_input_view)

                # Create class instances for data type as "upload"
                if user_input_view == 'sleep':
                    upload = Sleep.FilterDataUpload(unfiltered_csv,
                                                    filtered_csv,
                                                    user_input_view)
                elif user_input_view == 'resting heart rate':
                    upload = HR.FilterDataUpload(unfiltered_csv,
                                                 filtered_csv,
                                                 user_input_view)
                else:
                    upload = Workout.FilterDataUpload(unfiltered_csv,
                                                      filtered_csv,
                                                      user_input_view)

                # Ask if user wants to connect to db
                if not ask_connect_db(upload):
                    print("Please try again!\n")

                if not ask_1week_hr(upload):
                    print("Ok ... skipping 1 week resting average")

                if not ask_1month_hr(upload):
                    print("Ok ... skipping 1 month resting average")

                if not ask_6month_hr(upload):
                    print("Ok ... skipping 6 month resting average")

                if not ask_1year_hr(upload):
                    print("Ok ... skipping 1 year resting average")

            # Invalid entry -- try again
            else:
                print(f"{user_input_view} not an option! Try again ... ")
                continue

        # Average week
        # Average Month
        # Average 6 months
        # Average year
