gamma = 0.8
epsilon = 1e-4
V = [[0.] for _ in range(3)]
criterion = (epsilon * (1 - gamma) / gamma)
i = 0


while True:
    print(f'iteration {i}')

    s1 = max(0 + gamma * V[0][-1],
             0.3 * (-1 + gamma * V[1][-1]) + 0.7 * (-1 + gamma * V[0][-1]))

    s2 = max(0.4 * (3 + gamma * V[0][-1]) + 0.6 * (3 + gamma * V[1][-1]),
             0.3 * (2 + gamma * V[2][-1]) + 0.7 * (2 + gamma * V[1][-1]))

    s3 = max(0.4 * (3 + gamma * V[1][-1]) + 0.6 * (3 + gamma * V[2][-1]),
             2 + gamma * V[2][-1])

    maxDiff = -float('inf')
    for j, val in enumerate((s1, s2, s3)):
        maxDiff = max(maxDiff, val - V[j][-1])
        V[j].append(val)

    if maxDiff <= criterion:
        break

    i += 1

for j in range(3):
    print(f'S{j+1}: {V[j][-1]:.2f}')
