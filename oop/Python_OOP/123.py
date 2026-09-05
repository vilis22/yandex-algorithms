x = _

for key in tuple(x.__dict__):
    if hasattr(Alphabet, key):
        delattr(x, key)
