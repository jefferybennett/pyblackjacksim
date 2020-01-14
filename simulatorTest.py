import json;

#from bonsai_ai import Simulator, Brain, Config, logger
import star
from blackJack import Game

config = {};
#log = logger.Logger()

#class BlackJackSimulator(Simulator):
class BlackJackSimulator():

    def __init__(self, brain, model):
        #super().__init__(brain, "BlackJackSimulator")      # string must match cartpole.ink
        self.model = model

    def episode_start(self, parameters=None):
        self.model.reset()
        return star.state(self.model.state)

    def simulate(self, brain_action):
        action = star.action(brain_action)

        self.model.step(action)

        #terminal    = star.terminal(self.model.state)
        #reward      = star.reward(self.model.state, terminal)
        #brain_state = star.state(self.model.state)

        #if terminal:
        #    log.info(f'Episode {self.episode_count}: '
        #             f'iterations={self.iteration_count:-3.0f} reward={self.episode_reward:-3.1f}')

        #return (brain_state, reward, terminal)

if __name__ == '__main__':

    #log.info(f'Process ID {os.getpid()}')

    #brainConfig     = Config(sys.argv)        # Parses ~/.bonsai and .brains
    #brain           = Brain(brainConfig)
    model           = Game
    #sim             = BlackJackSimulator(brain, model)

    with open('config.json') as config_file:
        gameConfig = json.load(config_file)

    game = Game(gameConfig);

    #log.info(f'Training {brain.name}...')

    #for card in game._shoe._cards:
    #    print(card);