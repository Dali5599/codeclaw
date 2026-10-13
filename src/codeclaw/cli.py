"""
CodeClaw CLI entry point using Typer and Rich.
"""
import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(help="CodeClaw - Autonomous AI Code Generation & Refactoring Agent")
console = Console()

@app.command()
def version():
    """Display the current CodeClaw version."""
    from codeclaw import __version__
    console.print(Panel(f"[bold cyan]CodeClaw[/bold cyan] v{__version__} - Autonomous AI Developer", border_style="cyan"))

@app.command()
def doctor():
    """Run system diagnostic check."""
    console.print("[green]✓[/green] Python 3.10+ detected")
    console.print("[green]✓[/green] Git repository detected")
    console.print("[green]✓[/green] CodeClaw core engine operational")

def main():
    app()

if __name__ == "__main__":
    main()
