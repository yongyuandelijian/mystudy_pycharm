import re

IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'

# area_codes 有三千多行，知乎编辑器保存不了，已放到github仓库中
AREA_CODES = {}

def is_valid_idcard(idcard):
    """Validate id card is valid."""
    if isinstance(idcard, int):
        idcard = str(idcard)

    if not re.match(IDCARD_REGEX, idcard):
        return False

    if idcard[:6] not in AREA_CODES:
        return False

    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    items = [int(item) for item in idcard[:-1]]

    copulas = sum([a * b for a, b in zip(factors, items)])

    ckcodes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    return ckcodes[copulas % 11].upper() == idcard[-1].upper()