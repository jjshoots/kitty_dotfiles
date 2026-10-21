# Custom tab title pieces, used via {custom} in tab_title_template.
# kitty loads this once at startup, so changes need a full restart.

from kitty.fast_data_types import get_boss


def draw_title(data: dict) -> str:
    tab = get_boss().tab_for_id(data['tab_id'])
    if tab is None:
        return ''
    parts = []
    if emoji := getattr(tab, 'tab_emoji', None):  # set by tab_colors.py
        parts.append(emoji)
    if tab.name:  # only set when renamed with set_tab_title
        parts.append(tab.name)
    return ' ' + ' '.join(parts) if parts else ''
