#!/usr/bin/env bash

set -e

SERVICE_NAME="norn.service"
SERVICE_FILE="$HOME/.config/systemd/user/$SERVICE_NAME"
DATA_DIR="$HOME/.local/share/norn"



systemctl --user stop "$SERVICE_NAME" 2>/dev/null || true

rm -f "$SERVICE_FILE"

systemctl --user daemon-reload



SHELL_NAME="$(basename "$SHELL")"

case "$SHELL_NAME" in
    zsh)
        rm -f "$HOME/.oh-my-zsh/custom/completions/_norn"
        ;;

    bash)
        rm -f "$HOME/.local/share/bash-completion/completions/norn"
        ;;

    fish)
        rm -f "$HOME/.config/fish/completions/norn.fish"
        ;;

    *)
        echo "Warning: unsupported shell: $SHELL_NAME"
        ;;
esac




pip uninstall -y norn



echo
echo "Norn data directory:"
echo "$DATA_DIR"
echo

read -r -p "Do you want to delete the Norn data directory? [y/N]: " DELETE_DATA

if [[ "$DELETE_DATA" =~ ^[Yy]$ ]]; then
    if [[ -d "$DATA_DIR" ]]; then
        rm -rf "$DATA_DIR"
        echo "Norn data directory deleted."
    else
        echo "Norn data directory not found."
    fi
else
    echo "Norn data directory kept."
fi

echo "Norn uninstalled successfully."
