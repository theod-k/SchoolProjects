with open("mdpinput.txt", 'r') as file:
    lines = file.readlines()
        
    nocomLines = []

    for line in lines:
        line = line.strip()
        if line.startswith('%'):
            continue
        else:
            nocomLines.append(line)

states = []
actions = []
action1Transitions = {}
action2Transitions = {}
rewards = []
gamma = None
epsilon = None

# for i in nocomLines:
#     print(i)
    
states = nocomLines[0].split(",")
for i in range(len(states)):
    states[i] = states[i].strip()
    
actions = nocomLines[1].split(",")
for i in range(len(actions)):
    actions[i] = actions[i].strip()
    
temp1 = nocomLines[2].split(",")
temp2 = nocomLines[3].split(",")
temp3 = nocomLines[4].split(",")
for i in range(len(temp1)):
    temp1[i] = float(temp1[i].strip())
    temp2[i] = float(temp2[i].strip())
    temp3[i] = float(temp3[i].strip())
action1Transitions = {
    states[0]: temp1,
    states[1]: temp2,
    states[2]: temp3
}

temp4 = nocomLines[5].split(",")
temp5 = nocomLines[6].split(",")
temp6 = nocomLines[7].split(",")
for i in range(len(temp1)):
    temp4[i] = float(temp4[i].strip())
    temp5[i] = float(temp5[i].strip())
    temp6[i] = float(temp6[i].strip())
action2Transitions = {
    states[0]: temp4,
    states[1]: temp5,
    states[2]: temp6
}

transitions = {}
for i, state in enumerate(states):
    for j, action in enumerate(actions):
        if action == actions[0]:
            transitions[(state, action)] = action1Transitions[state]
        elif action == actions[1]:
            transitions[(state, action)] = action2Transitions[state]


for i in range(6):
    rewards.append(nocomLines[8+i].split(","))
    for j in range(len(rewards[i])):
        rewards[i][j] = rewards[i][j].strip()

rewards_dict = {
    (states[0], actions[0]): float(rewards[0][2]),
    (states[0], actions[1]): float(rewards[1][2]),
    (states[1], actions[0]): float(rewards[2][2]),
    (states[1], actions[1]): float(rewards[3][2]),
    (states[2], actions[0]): float(rewards[4][2]),
    (states[2], actions[1]): float(rewards[5][2])
}

gamma = float(nocomLines[14])
epsilon = float(nocomLines[15])

# print(transitions)
# print(reward_dict)

def value_iteration(states, actions, transitions, rewards, gamma, epsilon):
    utilities = {s: 0.0 for s in states}
    policy = {s: None for s in states}
    delta = float('inf')

    while delta > epsilon * (1 - gamma) / gamma:
        new_utilities = utilities.copy()
        delta = 0

        for s in states:
            action_values = {}
            for a in actions:
                expected_utility = sum(
                    transitions[(s, a)][i] * utilities[states[i]] for i in range(len(states))
                )
                action_value = rewards[(s, a)] + gamma * expected_utility
                action_values[a] = action_value

            best_action = max(action_values, key=action_values.get)
            new_utilities[s] = action_values[best_action]
            policy[s] = best_action

            delta = max(delta, abs(new_utilities[s] - utilities[s]))

        utilities = new_utilities

    return utilities, policy

utilities, policy = value_iteration(states, actions, transitions, rewards_dict, gamma, epsilon)

# print(utilities)
# print(policy)

with open("policy.txt", "w") as file:
    file.write("% Format: State: Action (Value)\n")
    for i in range(len(utilities)):
        file.write(f"{states[i]}: {policy[states[i]]} ({round(utilities[states[i]], 2)})\n")