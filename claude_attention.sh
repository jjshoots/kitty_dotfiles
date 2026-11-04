#!/bin/sh
# Claude Code hook: mark the kitty window this session runs in.
#   claude_attention.sh waiting|done|busy|clear
# Reads the hook JSON on stdin (ignored). Needs `listen_on` in kitty.conf so
# KITTY_LISTEN_ON is exported; falls back to the pid-based socket path.
state="$1"
[ -n "$KITTY_WINDOW_ID" ] || exit 0
to="${KITTY_LISTEN_ON:-unix:/tmp/kitty-$KITTY_PID}"
if [ "$state" = clear ]; then
    kitten @ --to "$to" set-user-vars --match "id:$KITTY_WINDOW_ID" claude >/dev/null 2>&1
else
    kitten @ --to "$to" set-user-vars --match "id:$KITTY_WINDOW_ID" "claude=$state" >/dev/null 2>&1
fi
exit 0
