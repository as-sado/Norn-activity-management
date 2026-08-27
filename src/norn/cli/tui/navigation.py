from textual.containers import Vertical
from textual.widgets import Button, Input


class NavigationMixin:

    def on_key(self, event):

        if event.key == "f1":
            self.show_view("apps")

        elif event.key == "f2":
            self.show_view("blocked")

        elif event.key == "f3":
            self.show_view("intervals")

        elif event.key == "f4":
            self.show_view("history")

        elif event.key == "q":
            self.exit()

    def on_button_pressed(
        self,
        event: Button.Pressed,
    ):

        button_id = event.button.id

        if button_id == "nav-apps":
            self.show_view("apps")

        elif button_id == "nav-blocked":
            self.show_view("blocked")

        elif button_id == "nav-intervals":
            self.show_view("intervals")

        elif button_id == "nav-history":
            self.show_view("history")

        elif button_id == "nav-quit":
            self.exit()

    def show_view(self, view):

        self.current_view = view

        apps = self.query_one(
            "#apps-container",
            Vertical,
        )

        blocked = self.query_one(
            "#blocked-container",
            Vertical,
        )

        intervals = self.query_one(
            "#intervals-container",
            Vertical,
        )

        history = self.query_one(
            "#history-container",
            Vertical,
        )

        command = self.query_one(
            "#command",
            Input,
        )

        apps.display = False
        blocked.display = False
        intervals.display = False
        history.display = False
        command.display = False

        if view == "apps":

            apps.display = True

        elif view == "blocked":

            blocked.display = True

            command.placeholder = "add/delete [app InitialClass] [time in minute]"
            command.display = True
            command.focus()

        elif view == "intervals":

            intervals.display = True

            command.placeholder = (
                "add/delete [app InitialClass] [start time] [end time] (HH:MM)"
            )

            command.display = True
            command.focus()

        elif view == "history":

            history.display = True

            self.query_one(
                "#history-date",
                Input,
            ).focus()