numpages = {
    "v1": {
        "start": 4,
        "end": 11
    },
    "v2": {
        "start": 12,
        "end": 19
    },
    "q1": {
        "start": 20,
        "end": 27
    },
    "q2": {
        "start": 28,
        "end": 35
    },
    "e1": {
        "start": 36,
        "end": 43
    },
    "e2": {
        "start": 44,
        "end": 51
    },     
}

chaporder = ["v1", "v2", "q1", "q2", "e1", "e2"]

def validateLookup(code):
    for chap in chaporder:
        if code == chap:
            return True
    return False