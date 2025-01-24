# tenable.client

Sub-package of tenable.
The following package allows to execute multiple calls to the rest server.


## Command Line Interface

The `tenable.client` package also provides a command-line interface.
```sh
    $ python -m tenable.client [OPTIONS] COMMAND [ARGS]
```

The top-level options include:

- ``-q``, ``--quiet``

    This option suppresses the output.

- ``-t``, ``--traceback``

    This option shows the full traceback when an exception is raised (by
    default, only the error message is printed, and the program exits with a
    non-zero code).

Commands:

- `run-users`

    Receives amount of users as a number and keep sending requests to the rest server.
    It is also possible to pass host and port to specifies the rest server address.

    ```sh
    $ python -m tenable.client run-users [OPTIONS] USERS_AMOUNT
    ```

    Options:
    - ``-h``, ``--host`` TEXT     [default: 127.0.0.1]
    - ``-p``, ``--port`` INTEGER  [default: 8080]
    - ``--help``                  Show similar message and exit.

- `error`

    Raises an exception and prints it to the screen.

    ```sh
    $ python -m tenable.client error [OPTIONS]
    ```

    Options:
    - ``--help``                  Show similar message and exit.

All commands accept the `-q` or `--quiet` flag to suppress output, and the `-t`
or `--traceback` flag to show the full traceback when an exception is raised
(by default, only the error message is printed, and the program exits with a
non-zero code).

To showcase these options, consider `error` command, which raises an exception:

```sh
$ python -m tenable.client error
ERROR: something went terribly wrong :[
$ python -m tenable.client -q error  # suppress output
$ python -m tenable.client -t error  # show full traceback
ERROR: something went terribly wrong :[
Traceback (most recent call last):
    ...
RuntimeError: something went terrible wrong :[
```

Do note that each command's options should be passed to *that* command, for example the `-q` and `-t` options should be passed to `tenable.client`, not `upload-mind`.

```sh
$ python -m tenable.client upload-mind -q  # this doesn't work
ERROR: no such option: -q
$ python -m tenable.client -q upload-mind  # this does work
```


## Developers Note

Inside the client.py file there are two variables which control the time between each request call:
    `minimal_time_between_request = 0`
    `maximal_time_between_request = 1`
Well it's pretty self explanatory from here.