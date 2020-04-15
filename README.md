# Delete Local Git Branches Based on Jira Status

This is a hacked up Python script to parse local Git branches and use the Jira API to see which tickets are complete and delete those branches.

This all works on my Mac :)  YMMV

Please be careful as this does delete things. You have been warned.

### Assumptions 
This assumes you include your Jira ticket # in your branch names. We use: feature/KEY-1234_description


### Requirements
* Python 3
* I'm using Jira v7.13
* Recent version of Git
* I'm using pipenv  (https://pipenv-fork.readthedocs.io/en/latest/basics.html)

### Configuraton
Jira URL, key, username and password are stored in credentials.py - this should typically NOT be checked into source control. 

Jira key is whatever you have prefixing your ticket numbers: FOO-1234 - "FOO" is the key. 

There is an example credentials file included in the repository. Rename to credentials.py and enter your information. 

Again make sure you do not commit credentials.py! 

Modify the status in the script to whatever you use in your Jira project. For our project when it's Pending Release or Done we can delete the branch:

ticketstatusfordelete = ["Done", "Pending Release"]


### Running 
* pipenv shell
* python branchdelete.py

```
jpriest: ~/www/git-jira-branch-delete (master=)$ pipenv shell python branchdelete.py 
Launching subshell in virtual environment…
bash-3.2$  . /Users/jpriest/.local/share/virtualenvs/git-jira-branch-delete-vVt7mrDH/bin/activate
(git-jira-branch-delete) bash-3.2$ python branchdelete.py
Issue 341 is In Review. Nothing to do!
Issue 123 is Done! Branch deleted: feature/FOOBAR-123-report_JP_v172
Issue 452 is Cancelled. Nothing to do!
Issue 345 is Pending Merge. Nothing to do!
```

