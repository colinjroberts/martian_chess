class Piece:
    piece_values = {
        "Pawn": 1,
        "Drone": 2,
        "Queen": 3,
        "Empty": 0
    }
    # valid movements are tuples of max_distance and direction
    piece_valid_movement = {
        "Pawn":  {"max_distance": 1,
                  "direction": ["d"],
                  },
        "Drone": {"max_distance": 2,
                  "direction": ["h", "v"],
                  },
        "Queen": {"max_distance": 100,
                  "direction": ["h", "v", "d"],
                  },
        "Empty": {"max_distance": 0,
                  "direction": [],
                  }
    }
    piece_reprs = {
        "Pawn": "P",
        "Drone": "D",
        "Queen": "Q",
        "Empty": "_"
    }

    def __init__(self, piece_type="Empty"):
        self.piece_type = piece_type
        self.value = self.piece_values[piece_type]
        self.max_distance = self.piece_valid_movement[piece_type]["max_distance"]
        self.direction = self.piece_valid_movement[piece_type]["direction"]

    def __repr__(self):
        return self.piece_reprs[self.piece_type]
