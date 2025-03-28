import click

from .rest import run_server
from ..utils import (
    log,
    main,
    module_main_exe,
    LISTEN_HOST,
    SERVER_PORT,
)


@main.command('run-server')
@click.option('-h', '--host', type=str, default=LISTEN_HOST)
@click.option('-p', '--port', type=int, default=SERVER_PORT)
@click.option('-r', '--redis', type=str, default=None)
def run_server_command(host, port, redis):
    log(run_server(host, port, redis))


module_main_exe(__package__)
