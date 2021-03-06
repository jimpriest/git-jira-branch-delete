#!/usr/bin/env python
import sys, regex, datetime
from git import Repo
import requests
from jira import JIRA
import credentials  # password storage

# Get Jira connection info
jirausername = credentials.login['username']
jirapassword = credentials.login['password']
jiraurl = credentials.login['url']
jirakey = credentials.login['key']

# Connect to JIRA
jira_options = {"server": jiraurl }
jira = JIRA(options=jira_options, basic_auth=(jirausername, jirapassword))

# Connect to Git
repo = Repo('~/www/apps/navycrms/.git')
git = repo.git

# Get local Git Branches
branchlist = repo.branches

# Parse 4 or 5 digit ticket numbers and check JIRA status for that ticket
# Change status to whatever status you want to delete branches 
pattern = '\\d{4,5}'
ticketstatusfordelete = ["Done", "Pending Release", "Cancelled"]

for i in branchlist:
  branchname = str(i)
  ticketnum = regex.findall(pattern, branchname)
  if len(ticketnum):
    # get issue info from JIRA
    issue = jira.issue( jirakey + "-" + ticketnum[0])
    status = str(issue.fields.status)
    if status in ticketstatusfordelete:
      print("Issue " + str(ticketnum[0]) + " is " + status + "! Branch deleted: " + branchname)
      git.branch('-D', branchname)    
    else:
      print("Issue " + str(ticketnum[0]) + " is " + status + ". Nothing to do!")