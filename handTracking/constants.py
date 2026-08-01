
hand_connections = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index Finger
    (9, 10), (10, 11), (11, 12),           # Middle Finger
    (13, 14), (14, 15), (15, 16),          # Ring Finger
    (0, 17), (17, 18), (18, 19), (19, 20),  # Pinky Finger
    (5, 9), (9, 13), (13, 17)              # Palm Knuckle Connections
]

hand_point_names = {
    # Wrist
    0: "wrist",

    # Thumb
    1: "thumb 1",
    2: "thumb 2",
    3: "thumb 3",
    4: "thumb tip",

    # Index finger
    5: "index 1",
    6: "index 2",
    7: "index 3",
    8: "index tip",

    # Middle finger
    9: "middle 1",
    10: "middle 2",
    11: "middle 3",
    12: "middle tip",

    # Ring finger
    13: "ring 1",
    14: "ring 2",
    15: "ring 3",
    16: "ring tip",

    # Pinky
    17: "pinky 1",
    18: "pinky 2",
    19: "pinky 3",
    20: "pinky tip"
}