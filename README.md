# Gym Trader
Basic trading environment using stock prices

### Installation
`git clone https://github.com/overlapjho/gym-trader.git`

`cd gym-trader`

`pip install -e .`

### Usage

    import gym
    import gym_trader.envs.trader as make

    env = make.TraderEnv()
    env.seed(0)

    print('observation space:', env.observation_space)
    print('action space:', env.action_space)

    state = env.reset()

    done = False
    rewards = []
    states = []

    act = np.random.randit(2)

    while not done:

        action = act
        state, reward, done = env.step(action)

        rewards.append(reward)
        states.append(state)

        print("action:", action, " state: ", state , " reward:", reward, done)
    
        if done:
            break

### Examples

[Policy Search](/examples/policy_search.ipynb)

[Deep Q Network](examples/DQN.ipynb)


    
