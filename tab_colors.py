# Give every tab its own colour and emoji in the tab bar.
#
# Loaded as a global watcher (`watcher tab_colors.py` in kitty.conf). Whenever
# the tab bar is about to be redrawn, any tab without a colour is given the
# first palette entry not already used by another tab in that OS window. The
# colour and emoji are stored on the tab itself, so they follow the tab when it
# is moved. tab_bar.py draws the emoji next to the tab number.

# accent colours from themes/my-theme.conf (Kaolin Ocean), each with a
# matching emoji
PALETTE = (
    (0x6bd9db, '🐬'),  # cyan
    (0xe84c58, '🍒'),  # red
    (0x35bf88, '🌵'),  # green
    (0xdbac66, '🦊'),  # yellow
    (0x4ca6e8, '🐳'),  # blue
    (0xc79af4, '🔮'),  # magenta
    (0xeed891, '🍋'),  # light yellow
    (0xcea2ca, '🌸'),  # pink
    (0x7cf083, '🐸'),  # light green
)
BACKGROUND = 0x14141e
FOREGROUND = 0xe6e6e8
# like the theme's active/inactive tab pair (#52DFDF / #296f6f): the focused tab
# is brightened towards white, background tabs are dimmed to about a third
ACTIVE_LIGHTEN = 0.25  # how far the focused tab moves towards white
INACTIVE_KEEP = 0.35  # how much brightness background tabs keep


def blend(color: int, base: int, amount: float) -> int:
    out = 0
    for shift in (16, 8, 0):
        c, b = (color >> shift) & 0xff, (base >> shift) & 0xff
        out |= round(b + (c - b) * amount) << shift
    return out


def pick_entry(tabs) -> tuple[int, str]:
    used = [t.tab_color for t in tabs if getattr(t, 'tab_color', None) is not None]
    return min(PALETTE, key=lambda e: (used.count(e[0]), PALETTE.index(e)))


def on_tab_bar_dirty(boss, window, data) -> None:
    tabs = data['tab_manager'].tabs
    for tab in tabs:
        if getattr(tab, 'tab_color', None) is None:
            tab.tab_color, tab.tab_emoji = color, _ = pick_entry(tabs)
            tab.active_bg, tab.active_fg = blend(0xffffff, color, ACTIVE_LIGHTEN), BACKGROUND
            tab.inactive_bg, tab.inactive_fg = blend(color, 0x000000, INACTIVE_KEEP), FOREGROUND
