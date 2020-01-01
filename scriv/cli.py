"""Scriv command-line interface."""

import logging

import click
import click_log

from scriv.collect import collect
from scriv.create import create

logger = logging.getLogger()
click_log.basic_config(logger)


@click.group()
def cli() -> None:
    """Manage changelogs."""


cli.add_command(create)
cli.add_command(collect)
