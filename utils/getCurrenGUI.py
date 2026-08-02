from os import environ
from monitor.GUIclasses.HyprlandGUI import GetCurrentActiveWin
from monitor.interfaceGetCurrentActiveWin import InterfaceGetCurrentActiveWin



def getCurrentGrafInterface() -> InterfaceGetCurrentActiveWin:
    GI = environ.get('XDG_CURRENT_DESKTOP')

    if GI == 'Hyprland':
        return GetCurrentActiveWin()
    else:
        raise NotImplementedError(f"Unsupported graphic interface: {GI}")

grafInterface = getCurrentGrafInterface()