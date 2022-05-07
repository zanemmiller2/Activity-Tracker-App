import time

keywords = ["SwimMinng", "BikInG", "YoGa"]

for keyword in keywords:
    with open("activity_request.txt", "a") as request:
        request.write(keyword)
    time.sleep(5)
