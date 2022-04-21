"""
Author: Zane Miller
Date: 04/20/2022
Email: millzane@oregonstate.edu
Module: FilteredUploadClass
Description: Defines a class for Filtering Apple Health Data and Uploading to database
"""
import csv
import sys
import MySQLdb as mysql
import mariadb


class FilterDataUpload():
    """
    FilteredDataUpload class can filter sources out of csv, connect to a MySQL database, get row
    data from CSV, upload a csv to MySQL database, create a new table in a MySQL database, commit
    changes to MySQL database ... more???
    TODO
        1) function to create new MySQL database
        2) Function to create new user
        3) Functions for more extracted data types
        4) New class for database management??
        5) Web interface
        6) Data Analytics - New Class
    """

    def __init__(self, unfiltered_csv, filtered_csv, data_type):

        self.unfiltered_csv = unfiltered_csv
        self.filtered_csv = filtered_csv
        self.data_type = data_type

        self.default_workout_import_sources = ['Zane’s Apple\xa0Watch', 'Stryd', 'Slopes', 'ELEMNT']

        # Cursor initializer
        self.cursor = None
        self.connection = None

        self.table_name = None

    def database_connect(self, **kwargs):
        # Connect to MariaDB - fitnessTracker
        try:
            self.connection = mysql.connect(
                user=kwargs['user'],
                password=kwargs['password'],
                host=kwargs['host'],
                port=kwargs['port'],
                database=kwargs['database'],

            )
        except mariadb.Error as e:
            print(f"Error connecting to Mariadb Platform: {e}")
            sys.exit(1)

        self.cursor = self.connection.cursor()

    def filter_watch_workout_data(self, import_source=None):
        """
        Filters only workout data from Apple Watch from Workout.csv and writes to Workout_Filtered.csv
        :return: None
        """

        if not import_source:
            import_source = self.default_workout_import_sources

        with open(self.unfiltered_csv, 'r') as rf:
            csv_reader = csv.reader(rf, delimiter=",")

            with open(self.filtered_csv, 'w') as wf:
                csv_writer = csv.writer(wf, delimiter=',', quotechar='"')
                for row in csv_reader:
                    if row[0] in import_source:
                        csv_writer.writerow(row)

    def get_row_data(self):
        """ Gets the row data to import from filtered csv"""
        # Read data from filtered csv file Workout_Filtered
        with open(self.filtered_csv) as input_file:
            csv_reader = csv.reader(input_file)
            rows = list(csv_reader)

        return rows

    def upload_csv(self):
        """
        Function writes Workout_Filtered.csv to workoutDataAppleWatch table in fitnessTracker MariaDB
        """
        # Get row data
        rows = self.get_row_data()

        # Add new rows of Apple Watch Workout data
        skip_header = False  # No header row in csv
        for row in rows:

            if skip_header:
                skip_header = False
                continue

            query = f"INSERT INTO {self.table_name}(" \
                    f"sourceName, " \
                    f"sourceVersion, " \
                    f"device, " \
                    f"creationDate, " \
                    f"startDate, " \
                    f"endDate, " \
                    f"workoutActivityType, " \
                    f"duration, " \
                    f"durationUnit, " \
                    f"totalDistance, " \
                    f"totalDistanceUnit, " \
                    f"totalEnergyBurned, " \
                    f"totalEnergyBurnedUnit) " \
                    f"VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', " \
                    f"'{row[6]}','{row[7]}', '{row[8]}', '{row[9]}', '{row[10]}', '{row[11]}', " \
                    f"'{row[12]}')"

            self.cursor.execute(query)

    def create_new_table(self, table_name):
        """ Create new workoutDataAppleWatch table if one does not already exist """
        self.table_name = table_name
        print(f"Creating new {self.data_type} table")

        # create workout table
        if self.data_type == 'workout':
            query = f"CREATE TABLE IF NOT EXISTS {self.table_name}(" \
                    f"id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
                    f"sourceName varchar(255), " \
                    f"sourceVersion varchar(255), " \
                    f"device varchar(255), " \
                    f"creationDate varchar(255), " \
                    f"startDate varchar(255), " \
                    f"endDate varchar(255), " \
                    f"workoutActivityType varchar(255), " \
                    f"duration varchar(255), " \
                    f"durationUnit varchar(255), " \
                    f"totalDistance varchar(255), " \
                    f"totalDistanceUnit varchar(255), " \
                    f"totalEnergyBurned varchar(255), " \
                    f"totalEnergyBurnedUnit varchar(255))"

            self.cursor.execute(query)

        elif self.data_type == 'sleep':
            # TODO
            print("Sleep not set up yet")
            pass

        elif self.data_type == 'resting_hr':
            # TODO
            print("Resting HR not set up yet")
            pass

        # TODO error checking for created new table

    def commit_changes(self):
        """ Commit changes to database """
        self.connection.commit()

    def close_connection(self):
        """ Close connection to database """
        self.connection.close()
