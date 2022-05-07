# Author: Zane Miller
# Date: 05/01/2022
# Email: millzane@oregonstate.edu
# Description:
#       Microservice for pulling json data from json file based on keyword.
#               - Currently takes one request at a time but can be modified to
#                 receive multiple requests.
#
#               - Currently overwrites contents in the response, but can be
#                 modified to append.
#
#               - Currently loops infinitely but can be modified to exit on
#                 command.
#
#               - On main program controller side, activity_request.txt should
#                 first be checked that the request has been received before
#                 sending new request, or previous request may be lost. Request
#                 is received when activity_request.txt is empty.
#                      - In other words, on the controller side, only write to
#                        an empty activity_request.txt file.

import json

request_file = "activity_request.txt"
pull_file = "activity_dictionary.json"
response_file = "activity_data.json"

while True:
	# Get the keyword
	with open(request_file, "r+") as request:

		# read the keyword and strip (formatting)
		keyword = request.readline()
		keyword.strip()

		# Clear request line to allow for new quest
		request.truncate(0)

	if keyword:
		# Get the related content from activity_dictionary.json
		# as python dictionary object
		with open(pull_file, "r") as pull:
			parsed_json = json.load(pull)

		# Searches the JSON data for the requested keyword
		for entry in parsed_json:

			# finds the first entry in the dictionary pertaining to the keyword
			if entry["activity"].lower() == keyword.lower():
				# Write to activity_data.json -- overwrite mode
				with open(response_file, "a") as response:
					# indentation for formatting (pretty printing)
					json.dump(entry, response, indent=4)

				# Will only find the first entry -- Can be modified to return
				# multiple entries with the same keyword, if requested later.
				continue

	# No current request
	else:
		continue
