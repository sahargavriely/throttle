# throttle.rest

Sub-package of throttle.
The following package allows to execute running the rest server.


## Command Line Interface

The `throttle.rest` package also provides a command-line interface.
```sh
    $ python -m throttle.rest [OPTIONS] COMMAND [ARGS]
```

The top-level options include:

- ``-q``, ``--quiet``

    This option suppresses the output.

- ``-t``, ``--traceback``

    This option shows the full traceback when an exception is raised (by
    default, only the error message is printed, and the program exits with a
    non-zero code).

Commands:

- `run-server`

    It is possible to provide host and port to specifies the rest server address.
    It is also possible to provide redis url `'redis://redis:6379'` which will be used as one source of truth.
    Stop by pressing <enter>

    ```sh
    $ python -m throttle.rest run-server [OPTIONS]
    ```

    Options:
    - ``-h``, ``--host``  TEXT     [default: 127.0.0.1]
    - ``-p``, ``--port``  INTEGER  [default: 8080]
    - ``-r``, ``--redis`` TEXT     [None]
    - ``--help``                  Show similar message and exit.

- `error`

    Raises an exception and prints it to the screen.

    ```sh
    $ python -m throttle.rest error [OPTIONS]
    ```

    Options:
    - ``--help``                  Show similar message and exit.

All commands accept the `-q` or `--quiet` flag to suppress output, and the `-t`
or `--traceback` flag to show the full traceback when an exception is raised
(by default, only the error message is printed, and the program exits with a
non-zero code).

To showcase these options, consider `error` command, which raises an exception:

```sh
$ python -m throttle.rest error
ERROR: something went terribly wrong :[
$ python -m throttle.rest -q error  # suppress output
$ python -m throttle.rest -t error  # show full traceback
ERROR: something went terribly wrong :[
Traceback (most recent call last):
    ...
RuntimeError: something went terrible wrong :[
```

Do note that each command's options should be passed to *that* command, for example the `-q` and `-t` options should be passed to `throttle.rest`, not `upload-mind`.

```sh
$ python -m throttle.rest upload-mind -q  # this doesn't work
ERROR: no such option: -q
$ python -m throttle.rest -q upload-mind  # this does work
```


## Developers Note

Inside the wsgi.py file there is function which determine the amount of instances by the amount of cores
