from operator import itemgetter

import requests

# make API call and che
url= "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f" Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts =[]
for submission_id in submission_ids[:30]:
    # Make API calls
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"{submission_id} Status code: {r.status_code}")
    response_dict = r.json()
    submission_dict ={
        'title': response_dict["title"],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key= itemgetter('comments'),
                          reverse = False)

for submission_dict in submission_dicts:
    print(f"{submission_dict['title']}")
    print(f"{submission_dict['hn_link']}")
    print(f"{submission_dict['comments']}")