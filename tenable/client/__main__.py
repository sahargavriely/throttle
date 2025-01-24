import click

from .client import run_users
from ..utils import (
    log,
    main,
    module_main_exe,
    REQUEST_HOST,
    SERVER_PORT,
)


@main.command('run-users')
@click.argument('users-amount', type=int)
@click.option('-h', '--host', type=str, default=REQUEST_HOST)
@click.option('-p', '--port', type=int, default=SERVER_PORT)
def run_users_command(users_amount, host, port):
    log(run_users(users_amount, host, port))


module_main_exe(__package__)
