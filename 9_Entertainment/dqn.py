# -*- coding: utf-8 -*-
import random
import os
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K

import tensorflow as tf

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

EPISODES = 2000

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 1.0   # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.99
        self.learning_rate = 0.001
        self.model = self._build_model()
    
    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        model.add(Dense(24, input_dim=self.state_size, activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=Adam(lr=self.learning_rate))
        model.summary()
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = self.model.predict(state)
            if done:
                target[0][action] = reward
            else:
                t = self.model.predict(next_state)[0]
                target[0][action] = reward + self.gamma * np.amax(t)
            self.model.fit(state, target, epochs=1, verbose=0)
        
        # Decrease randomness
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        if not os.path.isdir('./save'):
            os.mkdir('./save')
        self.model.save_weights(name)


def validate(agent, n_episodes = 1):
    max_episode_len = 2000

    frames_Test = []
    times = []
    n_avg_scores = 100
    scores = deque(maxlen=n_avg_scores)
    avg_scores = []
    all_scores = []

    for e in range(n_episodes):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        total_rewards = 0

        for time in range(max_episode_len):
            env.render(mode = 'rgb_array')

            # Decide action
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            total_rewards += reward
            state = np.reshape(next_state, [1, state_size])

            # Position X-axis
            posX = next_state[0]
            if (posX < -3.0 or posX > 3.0):
                break
        
        times.append(time)
        scores.append(total_rewards)
        all_scores.append(total_rewards)
        avg_score = np.mean(scores)
        avg_scores.append(avg_score)

        isOk = ""
        if avg_score >= 195 and time > 100:
            isOk = ", --> Ok"

        print("episode: {}/{}, Average Score: {:.0f}, Trials: {}, e: {:.4}{}"
                    .format(e + 1, n_episodes, avg_score, time, agent.epsilon, isOk))

        env.close()
        print('Finished.')

def displayScores(trials, scores, all_scores, title = 'Test Random CartPole-v1'):
    # plot the scores
    fig = plt.figure()
    fig.set_size_inches(16, 14)
    #fig.patch.set_facecolor('xkcd:charcoal')
    fig.suptitle(title, fontsize=25)
    fig.tight_layout()

    # Plot 1
    ax = fig.add_subplot(211)
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    ep = np.arange(1, len(trials)+1)
    plt.plot(ep, trials)
    plt.plot([1, len(trials)], [100, 100], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=5)
    ax.legend(['Trials per Episode', 'over 100 consecutive'], fontsize=14)
    #ax.set_title('Episodes vs Trials', fontsize=16)
    ax.set_ylabel('Trials', fontsize=20)
    #ax.set_xlabel('Episode #', fontsize=20)
    ax.grid(linestyle='--', linewidth=1)

    # Plot 2
    ax = fig.add_subplot(212)
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.plot(ep, scores, color = 'red', linewidth=2)
    plt.plot(ep, all_scores, color = 'orange', linestyle='dashed')
    plt.plot([1, len(scores)], [195, 195], color='green', marker='o', linestyle='dashed', linewidth=2, markersize=5)
    #plt.plot([1, len(scores)], [np.mean(rewards), np.mean(rewards)], color='orange', marker='o', linestyle='dashed', linewidth=2, markersize=5)
    ax.legend(['Average Score', 'All scores', 'greater than 195.0'], fontsize=14)
    #ax.set_title('Episodes vs Scores', fontsize=16)
    ax.set_ylabel('Scores', fontsize=20)
    ax.set_xlabel('Episode #', fontsize=20)
    ax.grid(linestyle='--', linewidth=1)

    plt.show()

if __name__ == "__main__":
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n
    agent = DQNAgent(state_size, action_size)

    # Load if it exist
    #if os.path.isfile('./save/cartpole-ddqn.h5'):
        #agent.load("./save/cartpole-ddqn.h5")

    done = False
    batch_size = 32
    max_episode_len = 500
    times = []
    n_avg_scores = 100
    scores = deque(maxlen = n_avg_scores)
    avg_scores = []
    all_scores = []

    for e in range(EPISODES):
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        total_rewards = 0
        for time in range(max_episode_len):
            #env.render()
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            total_rewards += reward

            next_state = np.reshape(next_state, [1, state_size])
            # Remember the previous state, action, reward, and done
            agent.remember(state, action, reward, next_state, done)

            # make next_state the new current state for the next frame.
            state = next_state
            if done:
                times.append(time)
                scores.append(total_rewards)
                all_scores.append(total_rewards)
                avg_score = np.mean(scores)
                avg_scores.append(avg_score)

                if e%5 == 0:
                    print("episode: {}/{}, Average Score: {:.0f}, Trials: {}, e: {:.4}"
                        .format(e, EPISODES, avg_score, time, agent.epsilon))

                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)

        # Save
        #if e % 10 == 0:
            #agent.save("./save/cartpole-ddqn.h5")
    
    env.close()
    print('Finished.')
    
    # Display Scores
    displayScores(times, avg_scores, all_scores, 'Training CartPole-v1')
    
    # Validate
    #validate(agent)