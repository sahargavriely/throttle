[![github-workflow](https://github.com/sahargavriely/tenable/actions/workflows/github-action.yml/badge.svg)](https://github.com/sahargavriely/tenable/actions/workflows/github-action.yml)


# tenable

The `tenable` python package includes 2 packages client and rest.


## Packages

The package expose several sub-packages which can be run separately on a different machines.
The sub-packages are:

- [`client`](/tenable/client/README.md) - executing http request to the rest server.
- [`rest`](/tenable/rest/README.md) - provides REST api server - http request to get logic.


## Installation

1. Clone the repository and enter it:

    ```sh
    $ git clone git@github.com:sahargavriely/tenable.git
    ...
    $ cd tenable/
    ```

2. Run the installation script and activate the virtual environment:

    ```sh
    $ ./scripts/install.sh
    ...
    $ source .env/bin/activate
    [tenable] $  # you're good to go!
    ```

3. To check that everything is working as expected, run the tests, or skip that, I'm not your mother:

    ```sh
    $ pytest tests/
    ...
    ```


## Execution

### By Hand

1. Get REDIS instance up and running:

    ```sh
    $ ./scripts/run_docker_redis_stack.sh
    ...
    ```

2. Get our rest server up and running explanation how is here: [`rest`](/tenable/rest/README.md)

3. Get our client up and running explanation how is here: [`client`](/tenable/client/README.md)

### Docker

While it is possible to execute everything hand it is recommend to use the docker compose scripts

1. Get REDIS and our rest server up and running in a single command without any installation!

    ```sh
    $ ./scripts/run_docker_compose.sh
    ...
    ```

    To stop this use the opposite script

    ```sh
    $ ./scripts/stop_docker_compose.sh
    ...
    ```

2. Get our client up and running explanation how is here: [`client`](/tenable/client/README.md)


## Developers Note

Under utils/config.py you can find very explanatory configuration variables


## Outside Instructions:

In this task, you need to write a simple HTTP Denial-of-Service protection system.
You may use any libraries that will make your code cleaner or better in any way (we do expect you to implement the core logic yourself)
You can write in any language you prefer - we recommend using multi-threaded languages.

1. Client

  1.1 The user enters the number of HTTP Clients to simulate.
  1.2 For each HTTP client you will run a separate thread/task which will do the following in a loop:
    1.2.1 Send HTTP request to the server with the client identifier as a query parameter (e.g. http://localhost:8080/?clientId=3). Different clients can share the same identifier.
    1.2.2 Wait some random time and then send another request.
  1.3 The client will run until <enter> is pressed after which it will gracefully drain all the threads/tasks (wait for all of them to complete) and will exit.

2. Server

  2.1 Starts listening for incoming HTTP requests.
  2.2 For each incoming HTTP request you will do the following:
    2.2.1 Handle the request in a separate thread/task.
    2.2.2 Check if this specific client ID reached the max number of requests per time frame threshold (no more than 5 requests per 5 secs).
    2.2.3 If the client hasn’t reached the threshold, it will get a “200 OK” response otherwise “503 Service Unavailable”.
    2.2.4 The time frame starts on each client’s first request and ends 5 seconds later. After the time frame has ended, the client’s first request will open a new time frame, and so forth.
  2.3 The server will run until <enter> is pressed after which it will gracefully drain all the threads/tasks and will exit.
  2.4 The server should utilize all available resources (cores)

3. General notes

  3.1 Pay attention to thread safeness and graceful shutdown.
  3.2 The solution should be as simple as possible. No need for advanced input or configuration mechanisms.
  3.3 The solution should be a clean piece of code. Avoid over design/engineering.
