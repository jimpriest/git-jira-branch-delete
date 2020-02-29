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
Jira URL, key, username and password are stored in credentials.py - this should typically not be checked into source control. 

Jira key is whatever you have prefixing your ticket numbers: FOO-1234 - "FOO" is the key. 

There is an example file included in the repository. Rename to credentials.py and enter your information.

### Running 

python branchdelete.py



