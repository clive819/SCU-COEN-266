def clean(states):
    actions = []

    # current index
    idx = states[2]

    while "Dirty" in states:
        if states[idx] == "Dirty":
            # if the spot is dirty, we clean it.
            states[idx] = "Clean"
            actions.append("Suck")
        else:
            # move to dirty spot

            # since we only have two spots to clean, xor operation is enough.
            # i.e. 0 ^ 1 -> 1; 1 ^ 1 -> 0
            nextIdx = idx ^ 1

            # check which direction are we moving
            if nextIdx > idx:
                actions.append("Right")
            else:
                actions.append("Left")

            idx = nextIdx

    return actions, len(actions)


# MARK: - test case
testCases = [
    ["Clean", "Clean", 0],
    ["Clean", "Dirty", 0],
    ["Dirty", "Clean", 0],
    ["Dirty", "Dirty", 0],
    ["Clean", "Clean", 1],
    ["Clean", "Dirty", 1],
    ["Dirty", "Clean", 1],
    ["Dirty", "Dirty", 1],
]

for test in testCases:
    actions, cost = clean(test.copy())
    print("Initial State: {} | Cost {} action(s) to clean the place | Actions: {}".format(test, cost, actions))
