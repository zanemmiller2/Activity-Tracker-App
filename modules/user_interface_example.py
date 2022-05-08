from FilteredWorkoutClass import FilterWorkoutDataUpload

if __name__ == '__main__':
    # --------------------------------------------------------------------------------------------#
    #   User customizable settings                                                                #
    # --------------------------------------------------------------------------------------------#

    # Select source and destination files for upload
    workout_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App-Data/apple_health_export/' \
                     'Extracted_data/Workout.csv'
    workout_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App/Workout_Filtered.csv'

    sleep_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App-Data/apple_health_export/' \
                             'Extracted_data/SleepAnalysis.csv'
    sleep_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App/Sleep_Filtered.csv'

    restinghr_unfiltered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App-Data/apple_health_export/' \
                             'Extracted_data/RestingHeartRate.csv'
    restinghr_filtered_csv = '/Users/zanemiller/Desktop/361_SWE/Activity-Tracker-App/RestingHR_Filtered.csv'


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
    workout_upload = FilterWorkoutDataUpload(workout_unfiltered_csv,
                                             workout_filtered_csv,
                                             upload_data_type)

    sleep_upload = FilterWorkoutDataUpload(sleep_unfiltered_csv,
                                           sleep_filtered_csv,
                                           upload_data_type)

    restinghr_upload = FilterWorkoutDataUpload(restinghr_unfiltered_csv,
                                               restinghr_filtered_csv,
                                               upload_data_type)

    # filters out unwanted import sources from watch workout data ** optional param
    workout_upload.filter_watch_workout_data(data_tables_types_sources[upload_data_type])
    sleep_upload.filter_watch_workout_data()

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
    workout_upload.create_new_table('sleep')
    workout_upload.create_new_table('resting_hr')

    # Uploads CSV
    workout_upload.upload_csv()

    # Commit changes to database
    workout_upload.commit_changes()

    # Close database connection
    workout_upload.close_connection()
