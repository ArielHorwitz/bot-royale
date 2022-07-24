import time
import multiprocessing as mp
from typing import List

from bots.botural_selection.base import EvolvingBot, BotID

def run_battle(battlemap, bots: List[EvolvingBot]) -> List[BotID]:
    pass
    # TODO run the battle, and return 
    return bots

def run_evolution(map_getter, bot_getter, n_bots, out_path, n_processes=None, max_time=None):
    if max_time is not None:
        start_time = time.time()

    if n_processes is None:
        n_processes = mp.cpu_count() - 2

    with mp.Pool(n_processes) as pool:
        # shared genetic pool?
        # maybe have a pool of n_bots, and each process takes out ~ n_bots/n_processes and runs a battle between them,
        # killing off the losers and multiplying the winners. mp.managers.SyngManager.list() looks promising.
