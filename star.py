""" The state transform, action transform, terminal function and reward
    function. The functions in this file are called from sim.py.
"""

from bonsai_ai.logger import Logger

def state(model_state):
    """ Convert the state as represented in CartPole to a format expected.
        by the AI Engine.
    """
    return {
        'dealerCard1': model_state[0],
        'dealerCard2': model_state[1],
        'dealerCard3': model_state[2],
        'dealerCard4': model_state[3],
        'dealerCard5': model_state[4],
        'dealerCard6': model_state[5],
        'dealerCard7': model_state[6],
        'dealerCard8': model_state[7],
        'dealerCard9': model_state[8],
        'playerCard1': model_state[9],
        'playerCard2': model_state[10],
        'playerCard3': model_state[11],
        'playerCard4': model_state[12],
        'playerCard5': model_state[13],
        'playerCard6': model_state[14],
        'playerCard7': model_state[15],
        'playerCard8': model_state[16],
        'playerCard9': model_state[17],
        'dealerWins' : model_state[18], # 0 = Unknown, 1 = Dealer Won, 2 = Dealer Lost, 3 = Push
        'playerWins' : model_state[19], # 0 = Unknown, 1 = Player Won, 2 = Player Lost, 3 = Push
    }


def terminal(model_state):
    """ Return true if the state should end the episode. This includes both
        failure terminals (such as when the model isout-of-bounds) and success
        terminals (when the model is in a successful state)
    """
    dealerWins = model_state[18];

    # We use the dealerWin status to determine whether to terminate the episode
    return (dealerWins != 0)

def action(brain_action):
    """ Convert the action from the AI Engine to a format expected by the CartPole model.
    """
    return brain_action['command']

def reward(model_state, done):
    """ Return greater values to reward the AI for correct behavior.
    """
    return 1
