uberocket
=========

This is going to be a small python deploy script for <uberspace.de> hosting, which will pull a git repo and trigger a pelican run.

Not yet ready for anything. Beware.

The idea is to use github or bitbucket for the repository and user management and have a webhook that 
triggers the deploy.py script (run in cgi mode) to pull the changes and re-build the website.
