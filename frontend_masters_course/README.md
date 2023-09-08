# Notes about Python

## Frontend Masters course

- Frontend Masters: Practical Guide to Python
- started class on 2023 September 8

let's say you want to create a new python project/script/whatever

1. create a new directory & `cd` inside
2. `python3 -m venv env`
    - every project gets an environment
    - guarantees:
        - python stays at the version it was when the env was created -- locked in dev environment
        - all packages within environment stay containerized within env
    - to be clear, the command is:
        - `python3 -m venv /path/to/new/virtual/environment`
    - so, the way I was doing it on KDE machines for `konsave`:
        - $HOME/.local/bin/python3 ; where python3 is the env
            - actually a decent way to do it!
3. `source env/bin/activate`
    - this will give a shell that's within the venv

three helpful REPL methods:

1. `help()`
2. `type()`
3. `dir()`

continue

## References

- [Python docs - venv - creation of virtual environments](https://docs.python.org/3/library/venv.html)
