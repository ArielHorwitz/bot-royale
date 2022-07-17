from util.hexagon import Hex
from collections import namedtuple
from api.logging import logger as glogger
from api.actions import Move, Push


world_info = namedtuple('WorldInfo', [
    'positions',  # list of tiles
    'walls',  # set of tiles
    'pits',  # set of tiles
    'ring_radius',  # int
    'alive_mask',  # ndarray mask
    'turn_count',  # int
    'round_count',  # int
    'ap',  # ndarray
    'round_ap_spent',  # ndarray
    # when round_priority is empty, round is over.
    'round_remaining_turns',  # list
    ])


class BaseBot:
    NAME = "BaseBot"
    SPRITE = "circle"
    TESTING_ONLY = False
    COLOR_INDEX = 0

    def __init__(self, id: int):
        self.id = id
        self.name = self.NAME

    def setup(self, wi):
        pass

    def get_action(self, world_state):
        return Move(Hex(0, 0))

    def click_debug(self, hex, button):
        """
        Called when we are clicked on in the GUI.
        May return a list of vfx args.
        """
        glogger(f'#{self.id} {self.name} received click_debug with button: {button}')
        return [
            {'name': 'mark-green', 'hex': hex, 'neighbor': None},
        ]

    def __repr__(self):
        return f'<Bot #{self.id} {self.name}>'
