# GitTemplate
Contains the Git template folder to be used by the Git client.

## Install
To use the repo, clone in and set it as the template directory for git-init.

For example, you can define it as global template directory : 
```
git config --global init.templateDir C:/path/to/GitTemplate
```

## Dependencies
Some hooks are implemented using external dependencies like Python.
Some environment variable have to be defined in order to be able to run the scripts properly.

- In the hooks directory, create a directory called env
- In the env directory, create a file called var
- The template of this file is the following :
```
#!/bin/sh

PYTHON_BIN_PATH="C:/path/to/python"
```