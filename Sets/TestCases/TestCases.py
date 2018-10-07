input = output = None

test_cases = [
    {
        "xs": (),
        "find": [
            (13, None)
        ],
        "iter": (),
        "insert": [
            ({"k": 23, "v": "H"}, ({"k": 23, "v": "H"}))
        ],
        "delete": [
            (28, ())
        ],
        "order-iter": [],
        "find_next": [
            (19, None)
        ],
        "find_previous": [
            (15, None)
        ],
        "find_max": None,
        "find_min": None,
        "delete_max": (),
        "delete_min": ()
    },
    {
        "xs": ({"k": 26, "v": "B"}),
        "find": [
            (26, {"k": 26, "v": "B"}),
            (21, None)
        ],
        "iter": ({"k": 26, "v": "B"}),
        "insert": [
            ({"k": 17, "v": "L"}, ({"k": 17, "v": "L"}, {"k": 26, "v": "B"}))
        ],
        "delete": [
            (26, ()),
            (11, ({"k": 26, "v": "B"}))
        ],
        "order-iter": [{"k": 26, "v": "B"}],
        "find_next": [
            (16, {"k": 26, "v": "B"}),
            (26, None),
            (27, None)
        ],
        "find_previous": [
            (19, None),
            (26, None),
            (27, {"k": 26, "v": "B"})
        ],
        "find_max": {"k": 26, "v": "B"},
        "find_min": {"k": 26, "v": "B"},
        "delete_max": (),
        "delete_min": ()
    },
    {
        "xs": ({"k": 12, "v": "Z"}, {"k": 14, "v": "Y"}),
        "find": [
            (12, {"k": 12, "v": "Z"}),
            (14, {"k": 14, "v": "Y"}),
            (21, None)
        ],
        "iter": ({"k": 12, "v": "Z"}, {"k": 14, "v": "Y"}),
        "insert": [
            ({"k": 15, "v": "N"}, ({"k": 15, "v": "N"}, {"k": 12, "v": "Z"},
                                   {"k": 14, "v": "Y"}))
        ],
        "delete": [
            (12, ({"k": 14, "v": "Y"})),
            (11, ({"k": 12, "v": "Z"}, {"k": 14, "v": "Y"}))
        ],
        "order-iter": [{"k": 12, "v": "Z"}, {"k": 14, "v": "Y"}],
        "find_next": [
            (9, {"k": 12, "v": "Z"}),
            (12, {"k": 14, "v": "Y"}),
            (13, {"k": 14, "v": "Y"}),
            (14, None),
            (16, None)
        ],
        "find_previous": [
            (9, None),
            (12, None),
            (13, {"k": 12, "v": "Z"}),
            (14, {"k": 12, "v": "Z"}),
            (16, {"k": 14, "v": "Y"})
        ],
        "find_max": {"k": 14, "v": "Y"},
        "find_min": {"k": 12, "v": "Z"},
        "delete_max": ({"k": 12, "v": "Z"}),
        "delete_min": ({"k": 14, "v": "Y"})
    },
]
