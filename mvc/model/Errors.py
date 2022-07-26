class Error(Exception):
    """Base class for other exceptions"""
    pass

class GameHasEndedError(Error):
    """Raised when the game has ended"""
    pass

class InvalidMoveError(Error):
    """Raised when the move is invalid"""
    pass

class InvalidCoordRangeStepError(Error):
    """Raised when the move is out of range"""
    pass