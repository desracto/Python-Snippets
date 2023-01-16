class Pokemon():
    """
        Parent class of Pokemon, containing name, moves
    """
    def __init__(self, name, moves: list, health:int):
        self.name = name
        self.moves = moves
        self.health = health
    
    def generate_move_map(name, damage, accuracy):
        return {"name" : name, 
                "damage": damage,
                "accuracy": accuracy}
    
    def add_move(self, move: map):
        self.moves.append(move)
