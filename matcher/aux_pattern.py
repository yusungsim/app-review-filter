aux_pattern = [
    {
        "RIGHT_ID": "aux",
        "RIGHT_ATTRS": {"POS": "AUX"},
    },
    {
        "LEFT_ID": "aux",
        "REL_OP": ">",
        "RIGHT_ID": "aux_attr",
        "RIGHT_ATTRS": {"DEP": "attr"},
    },
    {
        "LEFT_ID": "aux_attr",
        "REL_OP": ">",
        "RIGHT_ID": "aux_attr_adj",
        "RIGHT_ATTRS": {"DEP": {"IN": ["acomp", "amod"]}},
    },
    {
        "LEFT_ID": "aux",
        "REL_OP": ">",
        "RIGHT_ID": "aux_nsubj",
        "RIGHT_ATTRS": {"DEP": "nsubj", "POS": "PRON"},
    },
]
