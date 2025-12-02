from textual.app import App
from textual import events
from textual.containers import HorizontalGroup, VerticalScroll
from textual.widgets import Header, Footer

class KickOff(App):
    BINDINGS = [("s", "settings", "Open Settings")]

    def compose(self):
        yield Header()
        yield Footer()
        yield VerticalScroll()

if __name__ == "__main__":
    app = KickOff()
    app.run()
