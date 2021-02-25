import requests
from bs4 import BeautifulSoup 


# ------ Part 0: Request ------
def request_github_trending(url):
    page = requests.get(url)
    return page

# ------ Part 1: Extract ------
def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    name = soup.find_all("article", {'class': 'Box-row'})
    return name

# ------ Part 2: Transform ------
def transform(html_repose):

    developer = []
    repo_name = []
    for i in range(len(html_repose)):
        developer.append(html_repose[i].h1.a.get_text().split()[0])
        repo_name.append(html_repose[i].h1.a.get_text().split()[2])

    stars = []
    for i in range(len(html_repose)):
        stars.append(html_repose[i].find("span", {'class': 'd-inline-block float-sm-right'}).get_text().split()[0])

    transformed = [{'developer': developer[i], 'repository_name': repo_name[i], 'nbr_stars': stars[i]} for i in range(len(developer))]
    return transformed

# ------ Part 3: Format ------
def format(repositories_data):
    csv_string = "Developer,Repository Name,Number of Stars\n"
    for i in transformed:
        row = ','.join(i.values())
        row += '\n'
        csv_string += row

    return csv_string


url = "https://github.com/trending"
page = request_github_trending(url)
name_star = extract(page)
transformed = transform(name_star)
result = format(transformed)
print(result)





