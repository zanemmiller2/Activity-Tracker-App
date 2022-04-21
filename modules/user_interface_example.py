from FilteredUploadClass import FilterDataUpload

if __name__ == '__main__':
    # --------------------------------------------------------------------------------------------#
    #   User customizable settings                                                                #
    # --------------------------------------------------------------------------------------------#

    # Select source and destination files for upload
    unfiltered_csv = '/Users/zanemiller/Desktop/Activity-Tracker-App-Data/apple_health_export/' \
                     'Extracted_data/Workout.csv'
    filtered_csv = '/Users/zanemiller/Desktop/Activity-Tracker-App/Workout_Filtered.csv'

    # What sources do you want to include in your upload?
    data_tables_types_sources = {
        'workout': ['Zane’s Apple\xa0Watch', 'Stryd', 'Slopes', 'ELEMNT'],
        'sleep': ['Autosleep', 'Zane’s Apple\xa0Watch'],
        'resting_hr': ['Zane’s Apple\xa0Watch']}

    # What kind of data are you uploading?
    upload_data_type = 'workout'

    # --------------------------------------------------------------------------------------------#
    #   This section models the API for uploading workout data from Apple Health                  #
    # --------------------------------------------------------------------------------------------#

    # upload data to a specific table TODO ('sleep', 'resting_hr' - functions)
    workout_upload = FilterDataUpload(unfiltered_csv, filtered_csv, upload_data_type)

    # filters out unwanted import sources from watch workout data ** optional param
    workout_upload.filter_watch_workout_data(data_tables_types_sources[upload_data_type])

    login_config = ["zanemiller",
                    "230Leafwoodct!",
                    "10.0.0.208",
                    3306,
                    'fitnessTracker']

    workout_upload.database_connect(user=login_config[0],
                                    password=login_config[1],
                                    host=login_config[2],
                                    port=login_config[3],
                                    database=login_config[4])

    # creates new table if one does not already exist
    workout_upload.create_new_table('workout_table')

    # Uploads CSV
    workout_upload.upload_csv()

    # Commit changes to database
    workout_upload.commit_changes()

    # Close database connection
    workout_upload.close_connection()
