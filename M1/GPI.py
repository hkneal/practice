"""
The script fetches all available reviews for the given Place ID.

For each review, it extracts:
name — the reviewer's name

stars — the star rating (e.g., 5)

message — the full review text (no cut-off or previews)

date — an estimated actual date, based on Googles relative time descriptions like "3 weeks ago" or "2 months ago" (randomized within the correct range is fine)

Output format:
Saves all the data into a CSV file with the following headers:
name, stars, message, date
"""


import os, config, json, csv
import requests

apikey = os.getenv("GOOG_API_KEY")
urlstr = "https://places.googleapis.com/v1/places/ChIJj61dQgK6j4AR4GeTYWZsKWw"
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': apikey,
}

# New format
# Pass all parameters as URL parameters or in headers as part of the GET request.
params = {
    'fields': 'reviews',
}
# print(apikey)
response = requests.get(url=urlstr, params=params, headers=headers)
reviews = response.json()
data = []
for review in reviews['reviews']:
    display_name = review.get('authorAttribution').get('displayName')
    message = review.get('originalText').get('text')
    data.append({
        'Name': display_name,
        'Stars': review.get('rating'),
        'Message': message,
        'Date': review.get('relativePublishTimeDescription')
    })
print(data)


with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Stars', 'Message', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(data)

        



# response = requests.get(url=urlstr, headers=headers)

test_json_response = {
  "reviews": [
    {
      "name": "places/ChIJj61dQgK6j4AR4GeTYWZsKWw/reviews/ChZDSUhNMG9nS0VJQ0FnSUNwcDdTY2N3EAE",
      "relativePublishTimeDescription": "a year ago",
      "rating": 2,
      "text": {
        "text": "So disapointed! Everywhere in the internet is marked that there is a Google Store (similar to Apple) but no, here is absolutely nothing for public - even the water in the public toilet did not work. My family just told me to sell my android phone ... sad all the way from Switzerland, just to see the (pretty nice) Googleplex from the outside",
        "languageCode": "en"
      },
      "originalText": {
        "text": "So disapointed! Everywhere in the internet is marked that there is a Google Store (similar to Apple) but no, here is absolutely nothing for public - even the water in the public toilet did not work. My family just told me to sell my android phone ... sad all the way from Switzerland, just to see the (pretty nice) Googleplex from the outside",
        "languageCode": "en"
      },
      "authorAttribution": {
        "displayName": "Manuela T.",
        "uri": "https://www.google.com/maps/contrib/108462846957530819199/reviews",
        "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjU6p8yhk7HrJRMRvN1LeUFVDidqVKflyjgf9JcETCbZDMLwaENUJQ=s128-c0x00000000-cc-rp-mo-ba5"
      },
      "publishTime": "2023-08-11T18:11:45.700605Z",
      "flagContentUri": "https://www.google.com/local/review/rap/report?postId=ChZDSUhNMG9nS0VJQ0FnSUNwcDdTY2N3EAE&d=17924085&t=1",
      "googleMapsUri": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sChZDSUhNMG9nS0VJQ0FnSUNwcDdTY2N3EAE!2m1!1s0x808fba02425dad8f:0x6c296c66619367e0"
    },
    {
      "name": "places/ChIJj61dQgK6j4AR4GeTYWZsKWw/reviews/ChdDSUhNMG9nS0VJQ0FnSURQcXR5bzVnRRAB",
      "relativePublishTimeDescription": "6 months ago",
      "rating": 5,
      "text": {
        "text": "My best experience on my trip to San Francisco. Everything was clean and beautiful.",
        "languageCode": "en"
      },
      "originalText": {
        "text": "My best experience on my trip to San Francisco. Everything was clean and beautiful.",
        "languageCode": "en"
      },
      "authorAttribution": {
        "displayName": "Samuel Schaapen",
        "uri": "https://www.google.com/maps/contrib/105993294554581133968/reviews",
        "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjXPPEAOrSwdET9vT4FU7Vzivr-go_haj5Puyk2iark7NVfQfCSY=s128-c0x00000000-cc-rp-mo-ba4"
      },
      "publishTime": "2024-12-01T03:22:30.848918Z",
      "flagContentUri": "https://www.google.com/local/review/rap/report?postId=ChdDSUhNMG9nS0VJQ0FnSURQcXR5bzVnRRAB&d=17924085&t=1",
      "googleMapsUri": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sChdDSUhNMG9nS0VJQ0FnSURQcXR5bzVnRRAB!2m1!1s0x808fba02425dad8f:0x6c296c66619367e0"
    },
    {
      "name": "places/ChIJj61dQgK6j4AR4GeTYWZsKWw/reviews/ChdDSUhNMG9nS0VJQ0FnSUNnaTUzcjBRRRAB",
      "relativePublishTimeDescription": "6 years ago",
      "rating": 5,
      "text": {
        "text": "Love this company! Even though visitors cannot enter their office, but you can enjoy the awesome and beautiful outdoor area. It's pretty cool that sometimes you also can see some employees do exercise in the area.",
        "languageCode": "en"
      },
      "originalText": {
        "text": "Love this company! Even though visitors cannot enter their office, but you can enjoy the awesome and beautiful outdoor area. It's pretty cool that sometimes you also can see some employees do exercise in the area.",
        "languageCode": "en"
      },
      "authorAttribution": {
        "displayName": "Kate Shao",
        "uri": "https://www.google.com/maps/contrib/103048140955897851689/reviews",
        "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjV5WTn4a48Nqj2g3ogrfCYTv9KSssYPBwhB_Of3tP4iep3DIzn2Dg=s128-c0x00000000-cc-rp-mo-ba7"
      },
      "publishTime": "2018-07-06T03:43:14.635Z",
      "flagContentUri": "https://www.google.com/local/review/rap/report?postId=ChdDSUhNMG9nS0VJQ0FnSUNnaTUzcjBRRRAB&d=17924085&t=1",
      "googleMapsUri": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sChdDSUhNMG9nS0VJQ0FnSUNnaTUzcjBRRRAB!2m1!1s0x808fba02425dad8f:0x6c296c66619367e0"
    },
    {
      "name": "places/ChIJj61dQgK6j4AR4GeTYWZsKWw/reviews/ChdDSUhNMG9nS0VJQ0FnSUNvOVp6UXF3RRAB",
      "relativePublishTimeDescription": "6 years ago",
      "rating": 5,
      "text": {
        "text": "A different world, completely unique experience, place where someone doesn't like to come out after entering into the campus.\nGood Headquarters, Mountain View (Silicon Valley), California, United States of America",
        "languageCode": "en"
      },
      "originalText": {
        "text": "A different world, completely unique experience, place where someone doesn't like to come out after entering into the campus.\nGood Headquarters, Mountain View (Silicon Valley), California, United States of America",
        "languageCode": "en"
      },
      "authorAttribution": {
        "displayName": "Ishwor Bhusal",
        "uri": "https://www.google.com/maps/contrib/108184535434220105394/reviews",
        "photoUri": "https://lh3.googleusercontent.com/a-/ALV-UjVNcqmLhOx7UQC3_i-VMbZjXpCxIinFrcZM2FdbMupjXpvK5vWx6A=s128-c0x00000000-cc-rp-mo-ba5"
      },
      "publishTime": "2019-02-22T04:27:41.683595Z",
      "flagContentUri": "https://www.google.com/local/review/rap/report?postId=ChdDSUhNMG9nS0VJQ0FnSUNvOVp6UXF3RRAB&d=17924085&t=1",
      "googleMapsUri": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sChdDSUhNMG9nS0VJQ0FnSUNvOVp6UXF3RRAB!2m1!1s0x808fba02425dad8f:0x6c296c66619367e0"
    },
    {
      "name": "places/ChIJj61dQgK6j4AR4GeTYWZsKWw/reviews/ChdDSUhNMG9nS0VJQ0FnSURBaTVqVHF3RRAB",
      "relativePublishTimeDescription": "8 years ago",
      "rating": 5,
      "text": {
        "text": "Amazing and welcoming google complex in Silicon Valley. It is open to public. You can take a colourful google bike for free and take a tour in the campus. You can feel the philosophy of google in the campus which encourages its employees to think freely. A must visit place in Silicon Valley. After visiting apple headquarters and experiencing that there is nothing to do there i really enjoyed my googleplex visit.",
        "languageCode": "en"
      },
      "originalText": {
        "text": "Amazing and welcoming google complex in Silicon Valley. It is open to public. You can take a colourful google bike for free and take a tour in the campus. You can feel the philosophy of google in the campus which encourages its employees to think freely. A must visit place in Silicon Valley. After visiting apple headquarters and experiencing that there is nothing to do there i really enjoyed my googleplex visit.",
        "languageCode": "en"
      },
      "authorAttribution": {
        "displayName": "Okan S",
        "uri": "https://www.google.com/maps/contrib/105190000182767225922/reviews",
        "photoUri": "https://lh3.googleusercontent.com/a/ACg8ocLk_8e_bxzQtxapb8yJeL_H6Yt28EqDOrvmXmvpkqLaDWIwAg=s128-c0x00000000-cc-rp-mo-ba6"
      },
      "publishTime": "2017-03-24T22:12:40.205Z",
      "flagContentUri": "https://www.google.com/local/review/rap/report?postId=ChdDSUhNMG9nS0VJQ0FnSURBaTVqVHF3RRAB&d=17924085&t=1",
      "googleMapsUri": "https://www.google.com/maps/reviews/data=!4m6!14m5!1m4!2m3!1sChdDSUhNMG9nS0VJQ0FnSURBaTVqVHF3RRAB!2m1!1s0x808fba02425dad8f:0x6c296c66619367e0"
    }
  ]
}