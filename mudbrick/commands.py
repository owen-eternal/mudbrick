import click
from .app import BuildProject

@click.command()
@click.option('--build', type=str, 
        help='Build flask application factory.')
def main(build):
    app = BuildProject(build)
    app.start_builder