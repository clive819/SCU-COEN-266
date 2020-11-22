gamma = 0.9
V = [[0.] for _ in range(4)]
criterion = 0
i = 0


while True:
    print(f'iteration {i}')

    s1 = gamma * max(V[2][-1], V[1][-1])
    s2 = 100 + gamma * max(0.1 * V[1][-1] + 0.9 * V[0][-1], V[1][-1])
    s3 = gamma * max(0.1 * V[2][-1] + 0.9 * V[3][-1], 0.1 * V[2][-1] + 0.9 * V[1][-1])
    s4 = 10 + gamma * max(V[3][-1], 0.1 * V[3][-1] + 0.9 * V[1][-1])

    maxDiff = -float('inf')
    for j, val in enumerate((s1, s2, s3, s4)):
        maxDiff = max(maxDiff, val - V[j][-1])
        V[j].append(val)

    if maxDiff <= criterion:
        break

    i += 1

for j in range(4):
    print(f'S{j+1}: {V[j][-1]: .2f}')
