import requests
import plotly.express as px
url="https://api.github.com/search/repositories"
url+="?q=language:python+sort:stars+stars>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r=requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    fig=px.bar(x=repo_names,y=stars)
    fig.show()
    
