# Shared helpers for the tab bar (tab_bar.py), the tab watcher (tab_colors.py)
# and the auto-rename kitten (tab_name.py).

import os

# Per-window user var set by claude_attention.sh (via Claude Code hooks).
STATE_VAR = 'claude'
# Strongest state wins when a tab has several splits.
STATE_RANK = {'waiting': 3, 'done': 2, 'busy': 1}
STATE_MARK = {'waiting': '🔔', 'done': '✅', 'busy': '⏳'}
MAX_NAME = 18


def auto_name(tab) -> str:
    """Name a tab after the directory its active window is in."""
    w = tab.active_window
    if w is None:
        return ''
    cwd = w.cwd_of_child or ''
    name = os.path.basename(cwd.rstrip('/')) or cwd
    if name == os.path.basename(os.path.expanduser('~')):
        name = '~'
    return name


def display_name(tab) -> str:
    name = tab.name or auto_name(tab)
    if len(name) > MAX_NAME:
        name = name[:MAX_NAME - 1] + '…'
    return name


def tab_state(tab) -> str:
    best = ''
    for w in tab:
        s = w.user_vars.get(STATE_VAR, '')
        if STATE_RANK.get(s, 0) > STATE_RANK.get(best, 0):
            best = s
    return best
