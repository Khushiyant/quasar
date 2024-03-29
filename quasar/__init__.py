'''This module contains the main() function, which is the entry point for the
command line interface.'''
from dotenv import load_dotenv
from quasar.cli import cli
from quasar.utils import logger
from quasar._version import __version__ as _version

__version__ = _version

load_dotenv()  # Load environment variables from .env file


def main():
    '''Entry point for the command line interface.'''
    logger.info(f"Quasar {_version} started")
    cli()
    

if __name__ == "__main__":
    main()
