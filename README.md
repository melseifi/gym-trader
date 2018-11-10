# Gym Trader
Basic trading environment using stock prices

### How to install
`git clone https://github.com/overlapjho/gym-trader.git`

`cd gym-trader`

`pip install -e`

### How to use

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

    
