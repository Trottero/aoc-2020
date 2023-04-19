from tqdm import tqdm

with open('./15/input.txt', 'r') as f:
    lines = [int(x) for x in f.readlines()[0].strip().split(',')]

spoken = {k: i + 1 for i, k in enumerate(lines)}

max_rounds = 30000000
spoken_number = lines[-1]
for current_turn in tqdm(range(len(lines) + 1, max_rounds + 1)):
    if spoken_number not in spoken:
        spoken[spoken_number] = current_turn - 1
        spoken_number = 0
        continue

    last_spoken = spoken[spoken_number]
    spoken[spoken_number] = current_turn - 1
    spoken_number = current_turn - 1 - last_spoken


print(spoken_number)
