import re

ABBREV = {
    'st': 'street', 'st.': 'street', 'street.': 'street',
    'ave': 'avenue', 'av': 'avenue', 'av.': 'avenue',
    'rd': 'road', 'rd.': 'road',
    'blvd': 'boulevard', 'blvd.': 'boulevard',
    'pl': 'place', 'plz': 'plaza', 'pl.': 'place',
    'ct': 'court', 'ctr': 'center',
    'ln': 'lane', 'dr': 'drive', 'ter': 'terrace',
    'hwy': 'highway', 'pkwy': 'parkway',
    'sq': 'square', 'e': 'east', 'e.': 'east', 'w': 'west', 'w.': 'west',
    's': 'south', 's.': 'south', 'n': 'north', 'n.': 'north',
    'wash': 'washington', 'wash.': 'washington', 'ft': 'fort',
    'aly': 'alley', 'aly.': 'alley',
    'cres': 'crescent', 'cres.': 'crescent', 'cr': 'crescent', 'cr.': 'crescent',
    'cir': 'circle', 'cir.': 'circle', 'grn': 'green', 'grn.': 'green',
    'hl': 'hill', 'hl.': 'hill', 'mt': 'mount', 'mt.': 'mount'
}

ORDINAL = {
    'first': '1', '1st': '1',
    'second': '2', '2nd': '2',
    'third': '3', '3rd': '3',
    'fourth': '4', '4th': '4',
    'fifth': '5', '5th': '5',
    'sixth': '6', '6th': '6',
    'seventh': '7', '7th': '7',
    'eighth': '8', '8th': '8',
    'ninth': '9', '9th': '9',
    'tenth': '10', '10th': '10'
}

ALIASES = {
    'ave of the americas': '6 avenue',
    'avenue of the americas': '6 avenue',
    'west 110 street': '110 street',
    'andrews avenue north': 'andrews avenue',
    'andrews avenue south': 'andrews avenue',
}

def normalize(name: str) -> str:
    """Return a normalized street name used across the notebooks."""
    if not isinstance(name, str):
        return ''

    s = re.sub(r'[^a-z0-9\s]', ' ', name.lower())
    s = re.sub(r'\s+', ' ', s).strip()

    words = []
    for word in s.split():
        if word in ORDINAL:
            word = ORDINAL[word]
        elif word in ABBREV:
            word = ABBREV[word]
        words.append(word)

    s_norm = ' '.join(words)
    return ALIASES.get(s_norm, s_norm)
