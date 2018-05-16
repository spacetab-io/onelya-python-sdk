from datetime import datetime


def get_array(items, item_class):
    if type(items) is list:
        return [item_class(item) for item in items]
    elif type(items) is str:
        return [item_class(item) for item in items.split(',')]
    return None


def get_item(item, item_class):
    if item is not None:
        return item_class(item)
    return None


def get_datetime(item):
    if item is not None:
        return datetime.strptime(item, '%Y-%m-%dT%X')
    return None


def get_datetime_array(items):
    if items is not None:
        return [datetime.strptime(item, '%Y-%m-%dT%X') for item in items]
    return None


def str_datetime(item):
    if item is not None:
        return item.strftime('%Y-%m-%dT%X')
    return None


def get_bool_item(item):
    if item is not None:
        return bool(item)
    return False
