gamma = 0.9
epsilon = 1e-4
V = [[0.] for _ in range(5)]
criterion = (epsilon * (1 - gamma) / gamma)
i = 0


while True:
    print(f'iteration {i}')

    s1 = gamma * max(0.5 * V[1][-1] + 0.5 * V[2][-1], 0.9 * V[1][-1] + 0.1 * V[2][-1])
    s2 = 1 + gamma * max(0.5 * V[3][-1] + 0.5 * V[4][-1], 0.9 * V[3][-1] + 0.1 * V[4][-1])
    s3 = gamma * max(0.9 * V[3][-1] + 0.1 * V[4][-1], 0.5 * V[3][-1] + 0.5 * V[4][-1])
    s4 = gamma * V[3][-1]
    s5 = 1 + gamma * V[4][-1]

    maxDiff = -float('inf')
    for j, val in enumerate((s1, s2, s3, s4, s5)):
        maxDiff = max(maxDiff, val - V[j][-1])
        V[j].append(val)

    if maxDiff <= criterion:
        break

    i += 1

for j in range(5):
    print(f'S{j+1}: {V[j][-1]}')
