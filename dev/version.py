import requests

def get_github_commit_count(owner, repo, branch='master'):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'sha': branch, 'per_page': 200}
    commits = []
    while True:
        response = requests.get(url, params=params)
        page_commits = response.json()
        if not page_commits:
            break
        commits.extend(page_commits)
        params['page'] = params.get('page', 1) + 1
    return len(commits)

def fetch_remote_version():
    github_owner = 'OrnitOnGithub'
    github_repo = 'lan-chatroom'
    github_branch = 'master'
    github_commits = get_github_commit_count(github_owner, github_repo, github_branch)
    return f'{github_commits}'

# Test
#print(fetch_remote_version())