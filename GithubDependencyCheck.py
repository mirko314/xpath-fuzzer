import requests
import re
import sys

# TODO: Enter your GH API TOKEN
# see https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
# Set Permission to 'public_repo'
API_TOKEN = ""

API_ENDPOINT = "https://api.github.com/graphql"

headers = {
  "Accept": "application/vnd.github.hawkgirl-preview+json",
  "Content-Type":"application/json",
  "Authorization":"bearer " + API_TOKEN
}

def generateQuery(repo_name, repo_owner):
  return '{"query": "query {repository(owner:\\"'+repo_owner+'\\", name:\\"'+repo_name+'\\") {dependencyGraphManifests{nodes {parseable filename dependencies{nodes{packageName}}}totalCount}}}"}'

def extractDataFromGithubUrl(url):
  x = re.search("\github\.com\/(.*)\/(.*)/?", url)
  owner = x.group(1)
  name = x.group(2)
  return {"owner": owner, "name": name}

print("Check any public github repo for dependencies")
print("Enter the following arguments: $csv-of-search-strings $github-url")
print("Example: saxon,jaxen https://github.com/wso2/carbon-data")

url = sys.argv[2]
repo_data = extractDataFromGithubUrl(url)
owner = repo_data["owner"]
name = repo_data["name"]

search_strings = sys.argv[1].split(',')

print("Searching the Repo ", name, " from ", owner, " for "," and ".join(search_strings))
print("------")
print("Results:")
print("------")


GraphQLQuery = generateQuery(name, owner)

r = requests.post(API_ENDPOINT, GraphQLQuery, headers=headers)
postQueryResult = r.text
for search_string in search_strings:
  searchIndex = postQueryResult.find(search_string)
  if searchIndex != -1:
    print(search_string, "found")



