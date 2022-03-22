import gym
from utils.agent import Agent


def main():
    episode_num = int(input("Number of episodes to run: "))
    env = gym.make("FrozenLake-v1")
    agent = Agent(env)

    for episode in range(400):
        state = env.reset()
        done = False
        while not done:
            action = agent.get_action_learn(state)
            next_state, reward, done, info = env.step(action)
            agent.learn(state, action, next_state, reward, done)
            state = next_state

    counter = 0
    for test in range(episode_num):
        state = env.reset()
        done = False
        while not done:
            action = agent.get_action(state)
            next_state, reward, done, info = env.step(action)
            state = next_state
            counter += reward
    print(agent.q)
    print(counter)


if __name__ == "__main__":
    main()
