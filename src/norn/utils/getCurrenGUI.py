from os import environ
from norn.app.Hyprland import HyprlandMonitor
from norn.app.Interface import StartApp

def get_current_GUI() -> StartApp:
    GI = environ.get('XDG_CURRENT_DESKTOP')

    if GI == 'Hyprland':
        return HyprlandMonitor()
    else:
        raise NotImplementedError(f"Unsupported graphic interface: {GI}")
