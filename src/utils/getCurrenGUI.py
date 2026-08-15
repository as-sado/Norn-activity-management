from os import environ
from app.Hyprland import HyprlandMonitor
from app.Interface import StartApp

def get_current_GUI() -> StartApp:
    GI = environ.get('XDG_CURRENT_DESKTOP')

    if GI == 'Hyprland':
        return HyprlandMonitor()
    else:
        raise NotImplementedError(f"Unsupported graphic interface: {GI}")
