import json
import csv
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import vader

with open('takehome.json') as json_file:
    hotels = json.load(json_file)
    #print("\nTotal hotel count : ", len(hotels), "\n")

    for hotel in hotels:
        keys = hotel.keys()
        print("* all keys: ", keys)
        for key in keys:
            print(key + ": type  ", type(key))

        print("* hotel name: ", hotel["name"])
        print("* hotel link: ", hotel["link"])
        print("* reviewquantity:", hotel["reviewquantity"])
        print("* ranking:", hotel["ranking"])
        print("* overall_rating:", hotel["overall_rating"])
        print("* doctype:", hotel["doctype"])
        print("* ranking: ", hotel["ranking"])

        reviews = hotel["reviews"]
        length = len(reviews)
        print("* total review count: ", length)
        print("* review details:")
        for i in range(length):
            print("\treview No. " + str(i + 1) + ":")
            review = reviews[i]
            print("\t* rating: ", review["rating"])
            print("\t* reviewed on: ", review.get("date", "Unknown"))
            print("\t* date of stay:", review.get("date_of_stay", "Unknown"))

            reviewContent = review.get("review", "Unknown")
            #print("\t* review:", reviewContent)

            # TODO clean review.csv

            with open('review.csv', 'a+', newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=' ')
                writer.writerow(reviewContent.split())
                #writer.writerow("\n")

