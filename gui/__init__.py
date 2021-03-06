from pathlib import Path
import numpy as np
from api.logging import logger as glogger
from util.settings import Settings


GUI_DEBUG = Settings.get('logging.gui', False)
FONT = str(Path.cwd() / 'assets' / 'FiraCode-SemiBold.ttf')


def center_sprite(pos, size):
    assert len(pos) == 2 and len(size) == 2
    r = np.array(pos) - (np.array(size) / 2)
    return [int(r[0]), int(r[1])]


def logger(m):
    if GUI_DEBUG:
        glogger(m)
