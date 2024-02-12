import requests

def get_github_commit_count(owner, repo, branch='master'):
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    params = {'sha': branch, 'per_page': 100}  # Set per_page to a value that suits your repository's commit count

    commits = []
    while True:
        response = requests.get(url, params=params)
        page_commits = response.json()

        if not page_commits:
            break

        commits.extend(page_commits)
        params['page'] = params.get('page', 1) + 1

    return len(commits)


# Assuming you have a version file with a single number representing the local version
#def get_local_version():
#    with open('version.txt', 'r') as file:
#        return int(file.read())

# Your Flask route to display the information
#@app.route('/check_update')
def check_update():
    github_owner = 'OrnitOnGithub'
    github_repo = 'lan-chatroom'
    github_branch = 'master'

    github_commits = get_github_commit_count(github_owner, github_repo, github_branch)
    #local_version = get_local_version()

    #update_available = github_commits > local_version

    return f'GitHub Commits: {github_commits}'
    #, Local Version: {local_version}, Update Available: {update_available}'

print(check_update())