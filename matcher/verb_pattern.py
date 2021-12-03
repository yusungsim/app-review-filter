verb_pattern = [
    {
        "RIGHT_ID": "verb",
        "RIGHT_ATTRS": {"POS": "VERB"},
    },
    {
        "LEFT_ID": "verb",
        "REL_OP": ">",
        "RIGHT_ID": "verb_prep",
        "RIGHT_ATTRS": {"DEP": "prep"},
    },
    {
        "LEFT_ID": "verb_prep",
        "REL_OP": ">",
        "RIGHT_ID": "verb_prep_pobj",
        "RIGHT_ATTRS": {"DEP": "pobj"},
    },
]
