_norn_completions() {
    local cur prev

    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    case "${COMP_WORDS[1]}" in
        add)
            COMPREPLY=($(compgen -W "block interval" -- "$cur"))
            ;;
        delete)
            COMPREPLY=($(compgen -W "block interval" -- "$cur"))
            ;;
        list)
            COMPREPLY=($(compgen -W "block interval date" -- "$cur"))
            ;;
        *)
            COMPREPLY=($(compgen -W "start stop status app add delete list" -- "$cur"))
            ;;
    esac
}

complete -F _norn_completions norn