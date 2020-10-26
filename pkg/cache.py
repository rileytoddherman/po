cache = {}


def cached(func):
    def _cached(*args, **kwargs):
        key = str(id(func)) + str(args) + str(kwargs)
        if key in cache:
            return cache[key]
        rs = func(*args, **kwargs)
        cache[key] = rs
        return rs

    return _cached

