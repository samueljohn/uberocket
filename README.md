uberocket
=========

So, you are hosting on astroids? But how to get your stuff up there? Make it fly with *uberrocket* and launch from your ground-control (github or bitbucket)!

This is going to be a small python deploy script for uberspace.de hosting, which will pull a git repo and trigger a pelican run.

The idea is to use github or bitbucket for the repository and user management and have a webhook that triggers the `deploy.fcgi` script (run in fcgi mode) to pull the changes and re-build the website.

For handling fast-cgi [flipflop.py](https://github.com/Kozea/flipflop) is shipped.

## Todo:

- Provide easy deamon setup for uberspace
- `virtualenv --python=/opt/python-3.3/bin/python ENV`
- This is meant to be called for each repository, so that we only need to configure one git
- However, we should provide a generic post-hook and in the config.yaml, we specify the [working-dir, command, parameters, env] that will be executed