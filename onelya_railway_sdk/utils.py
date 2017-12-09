
def get_array(items, item_class):
    if items is not None:
        return [item_class(item) for item in items]
    return None


def get_item(item, item_class):
    if item is not None:
        return item_class(item)
    return None
