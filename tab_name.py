# Kitten: pin the tab's automatic name (its directory) as the tab title, with
# no prompt. Bound to alt+shift+r. alt+r opens the normal rename prompt.

import sys

from kitty.constants import config_dir

if config_dir not in sys.path:
    sys.path.insert(0, config_dir)

from tabinfo import auto_name


def main(args: list[str]) -> str:
    pass


def handle_result(args: list[str], answer: str, target_window_id: int, boss) -> None:
    w = boss.window_id_map.get(target_window_id)
    tab = w.tabref() if w is not None else boss.active_tab
    if tab is not None:
        tab.set_title(auto_name(tab))


handle_result.no_ui = True
