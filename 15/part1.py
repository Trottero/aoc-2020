

with open('./15/input.txt', 'r') as f:
    lines = [int(x) for x in f.readlines()[0].strip().split(',')]

spoken = {k: i + 1 for i, k in enumerate(lines)}

max_rounds = 2020
spoken_number = lines[-1]
for current_turn in range(len(lines) + 1, max_rounds + 1):
    if spoken_number not in spoken:
        spoken[spoken_number] = current_turn - 1
        spoken_number = 0
        print(f'turn: {current_turn}, spoken number: {spoken_number}')
        continue

    last_spoken = spoken[spoken_number]
    spoken[spoken_number] = current_turn - 1
    spoken_number = current_turn - 1 - last_spoken
    print(f'turn: {current_turn}, spoken number: {spoken_number}')
