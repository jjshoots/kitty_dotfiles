# Custom tab title pieces, used via {custom} in tab_title_template.
# kitty loads this once at startup, so changes need a full restart.

from kitty.fast_data_types import get_boss


def draw_title(data: dict) -> str:
    tab = get_boss().tab_for_id(data['tab_id'])
    if tab is None:
        return ''
    # name is only set when the tab was renamed with set_tab_title
    return f' {tab.name}' if tab.name else ''
