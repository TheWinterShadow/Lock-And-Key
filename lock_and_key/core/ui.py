"""UI utilities for Lock & Key."""

from rich.console import Console
from rich.panel import Panel


def print_banner() -> None:
    """Print the Lock & Key banner."""
    console = Console()
    banner = r"""
[bold cyan]
 _                _    _           _   _           _  __
| |    ___   __ _| | _(_)_ __ ___ | | | | ___  ___| |/ /___ _   _ ___
| |   / _ \ / _` | |/ / | '_ ` _ \| |_| |/ _ \/ __| ' // _ \ | | / __|
| |__| (_) | (_| |   <| | | | | | |  _  |  __/\__ \ . \  __/ |_| \__ \\
|_____\___/ \__,_|_|\_\_|_| |_| |_|_| |_|\___||___/_|\_\___|\__, |___/
                                                           |___/
[/bold cyan]
    """
    console.print(
        Panel(
            banner,
            title="Lock & Key Cloud Scanner",
            subtitle="by Your Team",
            style="bold magenta",
        )
    )
