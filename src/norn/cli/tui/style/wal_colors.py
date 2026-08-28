from pathlib import Path


WAL_COLORS = Path.home() / ".cache" / "wal" / "colors"

TUI_COLORS = Path(__file__).parent / "colors.tcss"


DEFAULT_COLORS = {
    "background": "#141414",
    "scroll_background": "#262626",
    "scroll_color": "#3a3a3a",
    "accent_color": "#ffa927",
    "text_color": "#ffffff",
    "muted_color": "#a3a3a3",
}


def load_wal_colors():

    if not WAL_COLORS.exists():
        return None

    try:
        colors = []

        for line in WAL_COLORS.read_text().splitlines():
            line = line.strip()

            if line.startswith("#"):
                colors.append(line)

        if len(colors) < 16:
            return None

        return colors

    except OSError:
        return None


def generate_colors_tcss():
    colors = load_wal_colors()

    if colors is None:
        return

    values = {
        "background": colors[0],
        "scroll_background": colors[2],
        "scroll_color": colors[3],
        "accent_color": colors[4],
        "text_color": colors[1],
        "muted_color": colors[8],
    }

    content = "\n".join(
        f"${name}: {value};"
        for name, value in values.items()
    )

    TUI_COLORS.write_text(content + "\n")


def get_theme_variables():
    colors = load_wal_colors()

    if colors is None:
        return {
            "background": "#141414",
            "scroll-background": "#262626",
            "scroll-color": "#3a3a3a",
            "accent-color": "#ffa927",
            "text-color": "#ffffff",
            "muted-color": "#a3a3a3",
        }

    return {
        "background": colors[0],
        "text-color": colors[1],
        "scroll-background": colors[2],
        "scroll-color": colors[3],
        "accent-color": colors[4],
        "muted-color": colors[8],
    }