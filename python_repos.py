import requests
import plotly.express as px
import plotly.io as pio

pio.renderers.default='browser'

# make an API call and check the response

url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r =requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# convert the response object to dictionary
response_dict= r.json()

# process results
print(response_dict.keys())
# Explore information about the repositories
repo_dicts = response_dict["items"]
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])

    stars.append(repo_dict["stargazers_count"])

    # Build hover texts
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]

    hover_text = f"{owner} <br/> {description}"
    hover_texts.append(hover_text)
# print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"\nkeys{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(f"{key}")


# Making Visualization
title = "Most Starred Python Project on GitHub"
labels = {'x': 'Repository', 'y':'Stars'}
fig = px.bar(
    x=repo_names,
    y=stars, title=title,
    labels=labels,
    hover_name=hover_texts
)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20,
)
fig.show()