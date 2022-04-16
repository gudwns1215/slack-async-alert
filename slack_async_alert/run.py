import typer
from .slack import SlackClient


app = typer.Typer()


@app.command()
def success(command):
    client = SlackClient()
    client(f"[Success]process command: {command} \nwhere: {client.hardware_identifier}")


@app.command()
def fail(command):
    client = SlackClient()
    client(f"[Fail]process command: {command} \nwhere: {client.hardware_identifier}")


if __name__ == "__main__":
    app()
