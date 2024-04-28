import requests
from bs4 import BeautifulSoup


def list_available_packages():
    """
    This function gets the package names
    from the specified package repository URL
    :return: list of package names
    """
    url = "https://test.pypi.org/simple/"
    response = requests.get(url)
    if response.ok:
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        packages = [link.get_text() for link in links]
        return packages
    else:
        return "Failed to retrieve packages. Status code: " + str(response.status_code)


packages = list_available_packages()
print(packages)
