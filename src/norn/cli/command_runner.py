import shlex

from norn.cli.parser import get_argument
from norn.utils.logger import logger


def execute_command(command: str):
    command = command.strip()
    if not command:
        return None

    try:
        argv = shlex.split(command)

    except ValueError as e:
        return f"Command parsing error: {e}"

    parser = get_argument()
    try:
        args = parser.parse_args(argv)

    except SystemExit:
        return "Invalid command. Try: --help"

    try:
        result = args.func(args)
        return result

    except Exception:
        return "Error executing command"