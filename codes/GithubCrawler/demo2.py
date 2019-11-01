from bs4 import BeautifulSoup
import requests
import json

# set a
stars_limit = 0

# output file
output_file_name = "output.txt"

# request a url and encode the getting json data to python dictionary data
def request_url(url):
    response = requests.get(url)

    # the response text is json
    text = response.text
    dict_text = json.loads(text)
    return dict_text

# visit username, get his repos name, add his follower&following name to userlist
def visit_user(username):
    user_url = 'https://api.github.com/users/'+username
    repos_url = user_url+'/repos'
    followers_url = user_url+'/followers'
    following_url = user_url+'/following'

    userinfo = request_url(user_url)
    reposinfo = request_url(repos_url)

    # get repos of current user
    repos = handle_repo(reposinfo)

    followersinfo = request_url(followers_url)
    followinginfo = request_url(following_url)

    # get other users from current's follower and following
    names = handle_follow(followersinfo, followinginfo)

    return repos, names

def handle_repo(infos):
    repos = []
    for item in infos:
        if int(item["stargazers_count"])>=stars_limit:
            # each repo info stored in a list
            repo = []
            repo.append(item["full_name"])
            repo.append(item["url"])
            repo.append(item["stargazers_count"])
            repo.append(item["forks_count"])

            repos.append(repo)

    print(len(repos))
    return repos

def handle_follow(infos1, infos2):
    names = set()
    for user1 in infos1:
        names.add(user1["login"])

    for user2 in infos2:
        names.add(user2["login"])

    return names

def visit_all_users():
    all_users = set()
    all_repos = dict()

    requested_users = set()

    all_users.add('YangShaw')

    count = 0;
    while all_users and count<1:
        username = all_users.pop()
        # avoid repeated requests
        if username not in requested_users:
            print("current user: %s" % username)
            count = count+1
            repos, names = (visit_user(username))
            requested_users.add(username)
            # using dict to store user-repos pairs. repos is a list of list.
            all_repos[username] = repos
            all_users = all_users.union(names)
        else:
            pass

    # print(type(all_repos))
    # for repo in all_repos.items():
    #     print(repo)


    return all_repos

def output_to_file(repos = dict()):

    with open(output_file_name, 'w') as f:
        for repo in repos.items():
            f.write(repo)


if __name__ == "__main__":
    all_repos = visit_all_users()
    print(type(all_repos))
    output_to_file(all_repos)