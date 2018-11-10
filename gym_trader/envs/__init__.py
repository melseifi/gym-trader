from gym.envs.registration import registry, register, make, spec

# Custom
# ----------------------------------------

register(
    id='Trader-v0',
    entry_point='gym.envs.gym_trader.envs:TraderEnv'
)