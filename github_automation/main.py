from github import Github

g = Github("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")

# user info
print("----------------------------------------")
print("         User Info")
print("----------------------------------------")
user = g.get_user()
print("id: ", user.id)
print("name: ", user.name)
print("email: ", user.email)
print("type: ", user.type)
print("bio: ", user.bio)
print("avatar url: ", user.avatar_url)
print("company: ", user.company)
print("blog: ", user.blog)
print("collaborators: ", user.collaborators)
print("created_at: ", user.created_at)
print("disk_usage: ", user.disk_usage)
print("url: ", user.url, user.etag, user.updated_at, user.total_private_repos, user.events_url, user.subscriptions_url,
      user.repos_url, user.followers, user.followers_url, user.following, user.following_url, user.html_url,
      user.location, user.gists_url, user.gravatar_id, user.public_repos, user.hireable, user.last_modified,
      user.received_events_url, user.raw_headers, user.login, user.node_id, user.organizations_url,
      user.starred_url, user.owned_private_repos, user.site_admin, user.raw_data, user.plan, user.private_gists,
      user.public_gists)
print("----------------------------------------")

# step 1 (get all repos)
print("         available repos")
print("----------------------------------------")
repos = user.get_repos()
for repo in repos:
    print("****************")
    print("repo details of: ", repo.name)
    print("****************")
    print("repo id: ", repo.id)
    print("repo url: ", repo.url)
    print("repo html_url: ", repo.html_url)
    print("clone url: ", repo.clone_url)
    print("branches url: ", repo.branches_url)
    print("contents url: ", repo.contents_url)
    # files holding by a repo
    print("files: ")
    contents = repo.get_contents("")
    for file in contents:
        print("     ", file.name)
    print("branches: ")
    for branch in repo.get_branches():
        print("     ", branch.name)
    print("language: ", repo.get_languages())
    print("****************")

# view traffic
# repo = g.get_repo("tapupadhi/Building-an-English-Theasaurus")
# print(repo.stargazers_count)
# traff = repo.get_views_traffic()
# print(traff)



# create a repo
# repo = user.create_repo("test")

# create file inside the repo
# repo.create_file("test.txt", "commit", "this is a test file")

# delete a file
# repo = user.get_repo('test')
# cont = repo.get_contents('test.txt')
# print(cont)
# res = repo.delete_file(cont.path, "remove test", cont.sha, branch='main')
# print(res)
