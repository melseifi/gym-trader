from gym.envs.registration import register


register(
    id="Trader-v0",
    entry_point="gym_trader.envs:TraderEnv",
    timestep_limit=50)