import subprocess
import json
from time import sleep

import hyprland_socket

class GetCurrentActiveWin:

    def get_initial_class(self) -> str:
        if hyprland_socket.is_running():
            # Get the active window
            active_window = hyprland_socket.get_active_window()
            if active_window:
                return active_window.initial_class
        return "Not found"









