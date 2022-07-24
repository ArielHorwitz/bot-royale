from api.bots import BaseBot
from abc import ABC, abstractclassmethod

BotID = int

class EvolvingBot(BaseBot, ABC):
    
    PARAMETER_SHAPE: tuple
    
    def __init__(self, parameters):
        assert parameters.shape == self.__class__.PARAMETER_SHAPE
        self.parameters = parameters

    @abstractclassmethod
    def _get_action(cls, state, parameters):
        raise NotImplementedError

    @abstractclassmethod
    def _get_mutation(cls, parameters):
        """ Get a new set of parameters which are a random mutation of the input parameters """
        raise NotImplementedError

    @abstractclassmethod
    def _get_mating_result(cls, parameters1, parameters2):
        """ Get a new set of parameters which are the offspring of two other sets of parameters """

    def poll_action(self, state):
        return self.__class__._get_action(state, self.parameters)

    def mutate(self):
        mutated = self.__class__._get_mutation(self.parameters)
        return self.__class__(mutated)

