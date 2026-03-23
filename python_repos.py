import requests
import plotly.express as px
import plotly.io as pio

pio.renderers.default='browser'

# make an API call and check the response

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r =requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# convert the response object to dictionary
response_dict= r.json()

# process results
print(response_dict.keys())
# Explore information about the repositories
repo_dicts = response_dict["items"]
repo_names, stars= [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nkeys{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(f"{key}")

fig = px.bar(x=repo_names, y=stars )
fig.show()