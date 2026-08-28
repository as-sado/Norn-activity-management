import asyncio
from textual.widgets import Input
from norn.cli.command_runner import execute_command
from norn.cli.tui.views.history import load_history

async def handle_input_submitted(app, event: Input.Submitted):

    if event.input.id == "history-date":
        date = event.value.strip()

        if not date:
            return

        await load_history(app, date )
        return

    command = event.value.strip()
    if not command:
        return

    event.input.value = ""

    if app.current_view == "blocked":
        parts = command.split(maxsplit=1)
        if parts:
            command = (f"{parts[0]} block"+ (f" {parts[1]}"
                                                    if len(parts) > 1
                                                    else ""
                                                )
                                            )
    elif app.current_view == "intervals":
        parts = command.split(maxsplit=1)
        if parts:
            command = (f"{parts[0]} interval"+ (f" {parts[1]}"
                                                    if len(parts) > 1
                                                    else ""
                                                )
                                            )

    try:
        result = await asyncio.to_thread(execute_command,command)
        if result is None:
            result = ("Command executed successfully.")

    except Exception as e:
        result = f"Error: {e}"

    app.update_tui()
    event.input.focus()