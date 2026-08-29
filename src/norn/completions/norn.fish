complete -c norn -f -n "__fish_use_subcommand" -a "start stop status app add delete list"

complete -c norn -f -n "__fish_seen_subcommand_from add" -a "block interval"

complete -c norn -f -n "__fish_seen_subcommand_from delete" -a "block interval"

complete -c norn -f -n "__fish_seen_subcommand_from list" -a "block interval date"