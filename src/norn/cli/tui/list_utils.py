from textual.widgets import Label, ListView, ListItem


def update_list(list_view, cache, previous_order, values):

    new_order = [key for key, _ in values]
    value_map = dict(values)

    for key in new_order:
        if key not in cache:
            label = Label(value_map[key])
            item = ListItem(label)
            cache[key] = (item,label,value_map[key],)
            list_view.mount(item)

    for key in new_order:
        item, label, old_text = cache[key]
        new_text = value_map[key]

        if old_text != new_text:
            label.update(new_text)
            cache[key] = (item,label,new_text,)

    for key in list(cache):
        if key not in value_map:
            item, _, _ = cache.pop(key)

            if item.parent is list_view:
                item.remove()

    desired_items = [cache[key][0] for key in new_order]
    current_items = list(list_view.children)

    for index, desired_item in enumerate(desired_items):

        if index >= len(current_items):
            break

        if current_items[index] is desired_item:
            continue

        list_view.move_child(desired_item,before=current_items[index])
        current_items = list(list_view.children)

    previous_order[:] = new_order