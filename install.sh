#!/usr/bin/env bash

set -e

PROJECT_DIR="$(dirname "$0")"

# Install Norn
pip install --user "$PROJECT_DIR"

# Install systemd service
SERVICE_DIR="$HOME/.config/systemd/user"
SERVICE_FILE="$SERVICE_DIR/norn.service"

mkdir -p "$SERVICE_DIR"

cp "$PROJECT_DIR/systemd/norn.service" "$SERVICE_FILE"

systemctl --user daemon-reload

# Install shell completion
SHELL_NAME="$(basename "$SHELL")"

case "$SHELL_NAME" in
    zsh)
        COMPLETION_DIR="$HOME/.oh-my-zsh/custom/completions"

        mkdir -p "$COMPLETION_DIR"

        cp "$PROJECT_DIR/src/norn/completions/_norn" \
           "$COMPLETION_DIR/_norn"

        ;;

    bash)
        COMPLETION_DIR="$HOME/.local/share/bash-completion/completions"

        mkdir -p "$COMPLETION_DIR"

        cp "$PROJECT_DIR/src/norn/completions/norn.bash" \
           "$COMPLETION_DIR/norn"

        ;;

    fish)
        COMPLETION_DIR="$HOME/.config/fish/completions"

        mkdir -p "$COMPLETION_DIR"

        cp "$PROJECT_DIR/src/norn/completions/norn.fish" \
           "$COMPLETION_DIR/norn.fish"

        ;;

    *)
        echo "Warning: unsupported shell: $SHELL_NAME"
        ;;
esac

rm -rf "$PROJECT_DIR/build"
rm -rf "$PROJECT_DIR/src/norn.egg-info"

norn start

echo "Norn installed successfully."