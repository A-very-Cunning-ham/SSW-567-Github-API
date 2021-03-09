import requests

def listRepos(githubUserID):
    """Returns a list of repositories the respective number of commits for a given Github username"""
    r = requests.get(f"https://api.github.com/users/{githubUserID}/repos").json()
    results = []
    if not isinstance(r, list):
        raise TypeError(f"{r['message']}")
    for repo in r:
        name = repo.get("name")
        commits = len(requests.get(f"https://api.github.com/repos/{githubUserID}/{name}/commits").json())
        results.append([name, commits])
        print(f"Repo: {name} Number of commits: {commits}")
    return results