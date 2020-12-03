# "Action subclasses are used to describe actions and respond accordingly"
class Action:
    pass

class EscapeAction( Action ):
    pass

class MovementAction( Action ):
    def __init__( self, dx: int, dy: int ): # Assuming this is the constructor
        super().__init__() # Calls the parent constructor?

        self.dx = dx
        self.dy = dy