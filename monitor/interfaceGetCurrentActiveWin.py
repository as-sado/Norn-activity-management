from abc import ABC
import subprocess
import json
from typing import Protocol

class InterfaceGetCurrentActiveWin(Protocol):

    def get_initial_class(self) -> str:
        ...
    

