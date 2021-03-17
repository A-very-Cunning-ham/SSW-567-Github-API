import requests

# def listRepos(githubUserID):
#     """Returns a list of repositories the respective number of commits for a given Github username"""
#     r = requests.get(f"https://api.github.com/users/{githubUserID}/repos").json()
#     results = []
#     if not isinstance(r, list):
#         raise TypeError(f"{r['message']}")
#     for repo in r:
#         name = repo.get("name")
#         commits = len(requests.get(f"https://api.github.com/repos/{githubUserID}/{name}/commits").json())
#         results.append([name, commits])
#         print(f"Repo: {name} Number of commits: {commits}")
#     return results

def listRepos(githubUserID):
    """Returns a list of repositories the respective number of commits for a given Github username"""
    repos = getRepos(githubUserID)
    results = []

    for repo in repos:
        commits = getCommits(githubUserID, repo)
        results.append([repo, commits])
        print(f"Repo: {repo} Number of commits: {commits}")
    return results

def getRepos(ID):
    r = requests.get(f"https://api.github.com/users/{ID}/repos").json()
    names = []
    if not isinstance(r, list):
        raise TypeError(f"{r['message']}")
    for repo in r:
        names.append(repo.get("name"))
    return names

def getCommits(ID, repoName):
    return len(requests.get(f"https://api.github.com/repos/{ID}/{repoName}/commits").json())
