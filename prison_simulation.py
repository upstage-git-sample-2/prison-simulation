import random

#조예람
def run_simulations(num_simulations, num_prisoners):
    success_count = 0

    for _ in range(num_simulations):
        if simulate_prisoners_problem(num_prisoners):
            success_count += 1

    success_percentage = success_count / num_simulations * 100
    print(f"{num_prisoners}명의 죄수 중 모든 죄수가 최소한 한 번 선택된 확률: {success_percentage}%")


# 조성운
def select_prisoner(prisoners, selected_prisoners):
    # 죄수 선택 및 기록
    selected_prisoner = random.choice(prisoners)
    selected_prisoners.add(selected_prisoner)
    return selected_prisoner

# 김승호
def simulate_prisoners_problem(num_prisoners):
    prisoners = initialize_prisoners(num_prisoners)
    selected_prisoners = set()

    for _ in range(num_prisoners):
        selected_prisoner = select_prisoner(prisoners, selected_prisoners)

        if set(prisoners) == selected_prisoners:
            return True
    return False

if __name__ == "__main__":
    num_simulations = 1000
    num_prisoners = 100
    run_simulations(num_simulations, num_prisoners)

