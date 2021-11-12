import sys
import os
from github import Github
from datetime import datetime
from slack_sdk import WebClient

print(sys.argv)
# slack_token = os.environ['SLACK_TOKEN']
# git_token = os.environ['GIT_TOKEN']
# repo = os.environ['REPO']

# client = WebClient(slack_token)
# g = Github(git_token)
# # channel_id = "C02GMMQUQ56"  # Content Operation
# channel_id = "C02MBCYLF08" # Test Channel
# message = f'Issues in {repo} opened more than 5 days ago: \n'

# for issue in g.get_user().get_repo(repo).get_issues():
#     today = datetime.now()
#     diff = (today - issue.created_at).days
#     if diff > 5:
#         message += ' ' + issue.title + ' : \t' + str(diff) + ' days ago' + '\n'
#         message += ' ' + issue.html_url + '\n\n'

# result = client.chat_postMessage(
#                     channel=channel_id,
#                     text=message)
