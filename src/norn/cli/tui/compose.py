from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Button,
    Input,
    Label,
    ListView,
)


def compose_ui() -> ComposeResult:

    yield Vertical(
        Label(
            "CURRENT APPLICATION",
            id="current-title",
        ),
        Label(
            "-",
            id="current-app",
        ),
        id="current",
    )

    yield Vertical(

        Vertical(
            Label(
                "APPLICATIONS",
                id="apps-title",
            ),
            ListView(
                id="apps",
            ),
            Label(
                "TOTAL: 0m",
                id="apps-total",
            ),
            id="apps-container",
        ),

        Vertical(
            Label(
                "BLOCKED APPLICATIONS",
                id="blocked-title",
            ),
            ListView(
                id="blocked",
            ),
            id="blocked-container",
        ),

        Vertical(
            Label(
                "INTERVALS",
                id="intervals-title",
            ),
            ListView(
                id="intervals",
            ),
            id="intervals-container",
        ),

        Vertical(
            Label(
                "HISTORY",
                id="history-title",
            ),
            Input(
                placeholder="YYYY-MM-DD",
                id="history-date",
            ),
            ListView(
                id="history",
            ),
            id="history-container",
        ),

        id="content",
    )

    yield Input(
        placeholder="Command...",
        id="command",
    )

    yield Horizontal(
        Button(
            "(f1) Apps",
            id="nav-apps",
        ),
        Button(
            "(f2) Blocked",
            id="nav-blocked",
        ),
        Button(
            "(f3) Intervals",
            id="nav-intervals",
        ),
        Button(
            "(f4) History",
            id="nav-history",
        ),
        Button(
            "(q) Quit",
            id="nav-quit",
        ),
        id="navigation",
    )