import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.bodybuilding.com/exercises/finder/"
page_start = 1
page_end = 210

current_page = page_start
all_exercises = []
for item in range(page_start, page_end):
    page = requests.get(URL + str(current_page))

    soup = BeautifulSoup(page.content, "html.parser")

    exercises = soup.select(".ExCategory-results > .ExResult-row > .ExResult-cell--nameEtc")

    for exercise in exercises:
        name = exercise.h3.text.strip().replace("\n", "")
        muscle = exercise.find("div", class_ = "ExResult-muscleTargeted").find("a").text.strip()
        equipment = exercise.find("div", class_="ExResult-equipmentType").find("a").text.strip()
        all_exercises.append([name, muscle, equipment])
        print(f"{name},{muscle},{equipment}")
    
    current_page += 1

with open("exercises.csv", "w") as csv_file:
    csvwriter = csv.writer(csv_file)
    csvwriter.writerows(all_exercises) 

