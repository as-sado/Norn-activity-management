import argparse
from .commands import (list, list_block, list_interval, 
                       add_block, add_interval, 
                       delete_block, delete_interval, 
                       start, stop, status, start_tui, list_date)
from .const import (status_help, stop_help, start_help, app_help,
                    delete_interval_help, delete_block_help,delete_help,
                    add_interval_help, add_block_help, add_help, 
                    list_help, list_interval_help, list_blcok_help, list_date_help)
from norn.utils.parse_time import parse_time


def get_argument():
    parser = argparse.ArgumentParser(prog="norn",formatter_class=argparse.RawTextHelpFormatter,)
    
    commands = parser.add_subparsers(
        dest='command',
        required=True
    )

    # norn start 
    start_parser = commands.add_parser(
        "start",
        help=start_help
    )
    start_parser.set_defaults(func=start)

    # norn stop
    stop_parser = commands.add_parser(
        "stop",
        help=stop_help
    )
    stop_parser.set_defaults(func=stop)

    # norn status
    status_parser = commands.add_parser(
        "status",
        help=status_help
    )
    status_parser.set_defaults(func=status)

    # norn app
    app_parser = commands.add_parser(
        "app",
        help=app_help,
    )
    app_parser.set_defaults(func=start_tui)
    

    # norn add
    add_parser = commands.add_parser(
        "add",
        help=add_help,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    add_commands = add_parser.add_subparsers(
        dest="add_command",
    )

    #norn add block
    block_parser = add_commands.add_parser(
        "block",
        help=add_block_help
    )

    block_parser.add_argument(
        "name",
        type=str,
    )

    block_parser.add_argument(
        "time",
        type=int,
    )
    block_parser.set_defaults(func=add_block)

    # norn add interval
    interval_parser = add_commands.add_parser(
        "interval",
        help=add_interval_help
    )

    interval_parser.add_argument(
        "name",
        type=str,
    )

    interval_parser.add_argument(
        "start",
        type=parse_time,
    )

    interval_parser.add_argument(
        "end",
        type=parse_time,
    )
    interval_parser.set_defaults(func=add_interval)


    # norn delete
    delete_parser = commands.add_parser(
        "delete",
        help=delete_help,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    delete_commands = delete_parser.add_subparsers(
        dest="delete_command",
    )

    # norn delete block
    delete_block_parser = delete_commands.add_parser(
        "block",
        help=delete_block_help
    )

    delete_block_parser.add_argument(
        "name",
        type=str,
    )
    delete_block_parser.set_defaults(func=delete_block)

    # norn delete interval
    delete_interval_parser = delete_commands.add_parser(
        "interval",
        help=delete_interval_help
    )

    delete_interval_parser.add_argument(
        "name",
        type=str,
    )
    delete_interval_parser.set_defaults(func=delete_interval)


    # norn list 
    list_parser = commands.add_parser(
        "list",
        help=list_help,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    list_parser.set_defaults(func=list)

    list_command = list_parser.add_subparsers(
        dest="list_command",
    )

    # norn list block
    block_list_parser = list_command.add_parser(
        "block",
        help=list_blcok_help
    )
    block_list_parser.set_defaults(func=list_block)

    # norn list interval
    interval_list_parser = list_command.add_parser(
        "interval",
        help=list_interval_help
    )
    interval_list_parser.set_defaults(func=list_interval)

    # norn list date
    date_list_pareser = list_command.add_parser(
        "date",
        help=list_date_help
    )

    date_list_pareser.add_argument(
        "date",
        type=str
    )
    date_list_pareser.set_defaults(func=list_date)


    return parser


