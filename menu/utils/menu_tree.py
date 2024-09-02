def expand_parents(item, items_by_id):
    parent_id = item['parent']
    while parent_id:
        parent = items_by_id[parent_id]
        parent['is_expanded'] = True
        parent_id = parent['parent']


def build_menu_tree(menu_items, current_path):
    items_by_id = {
        item.id: {
            'id': item.id,
            'name': item.name,
            'url': item.get_absolute_url(),
            'parent': item.parent_id,
            'children': [],
            'is_expanded': False
        } for item in menu_items
    }
    tree = []

    for item in items_by_id.values():
        parent_id = item['parent']
        if parent_id is None:
            tree.append(item)
        else:
            items_by_id[parent_id]['children'].append(item)

    active_item = next((item for item in items_by_id.values() if item['url'] == current_path), None)

    if active_item:
        active_item['is_expanded'] = True
        expand_parents(active_item, items_by_id)

    return tree
