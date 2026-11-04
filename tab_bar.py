# Custom tab title pieces, used via {custom} in tab_title_template.
# kitty loads this once at startup, so changes need a full restart.

import sys

from kitty.constants import config_dir

if config_dir not in sys.path:
    sys.path.insert(0, config_dir)

from kitty.fast_data_types import get_boss

from tabinfo import STATE_MARK, display_name, tab_state


def draw_title(data: dict) -> str:
    tab = get_boss().tab_for_id(data['tab_id'])
    if tab is None:
        return ''
    parts = []
    if emoji := getattr(tab, 'tab_emoji', None):  # set by tab_colors.py
        parts.append(emoji)
    if name := display_name(tab):
        parts.append(name)
    if mark := STATE_MARK.get(tab_state(tab)):
        parts.append(mark)
    return ' ' + ' '.join(parts) if parts else ''
