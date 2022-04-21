from FilteredUploadClass import FilterDataUpload

if __name__ == '__main__':
    unfiltered_csv = '/Users/zanemiller/Desktop/Activity-Tracker-App/apple_health_export/' \
                     'Extracted_data/Workout.csv'
    filtered_csv = '/Users/zanemiller/Desktop/Activity-Tracker-App/apple_health_export/' \
                   'Filtered_Data/Workout_Filtered.csv'

    data_tables_types_sources = {
        'workout': ['Zane’s Apple\xa0Watch', 'Stryd', 'Slopes', 'ELEMNT'],
        'sleep': ['Autosleep', 'Zane’s Apple\xa0Watch'],
        'resting_hr': ['Zane’s Apple\xa0Watch']}
    upload_data_type = 'workout'

    # --------------------------------------------------------------------------------------------#
    #   This section models the API for uploading workout data from Apple Health                  #
    # --------------------------------------------------------------------------------------------#

    # upload data to a specific table TODO ('sleep', 'resting_hr' - functions)
    workout_upload = FilterDataUpload(unfiltered_csv, filtered_csv, upload_data_type)

    # filters out unwanted import sources from watch workout data ** optional param
    workout_upload.filter_watch_workout_data(data_tables_types_sources[upload_data_type])

    user = "zanemiller"
    password = "230Leafwoodct!"
    host = "10.0.0.208"
    port = 3306
    database = 'fitnessTracker'

    workout_upload.database_connect(user=user,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=database)

    # creates new table if one does not already exist
    workout_upload.create_new_table('workout_table')

    workout_upload.upload_csv()

    workout_upload.commit_changes()

    workout_upload.close_connection()

    # TODO Write class for analyzing data gggggdgd
