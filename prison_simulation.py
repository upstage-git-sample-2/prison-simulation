import random

# 조성운
def select_prisoner(prisoners, selected_prisoners):
    # 죄수 선택 및 기록
    selected_prisoner = random.choice(prisoners)
    selected_prisoners.add(selected_prisoner)
    return selected_prisoner

if __name__ == "__main__":
    num_simulations = 1000
    num_prisoners = 100
    run_simulations(num_simulations, num_prisoners)

