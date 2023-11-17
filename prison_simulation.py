def run_simulations(num_simulations, num_prisoners):
    success_count = 0

    for _ in range(num_simulations):
        if simulate_prisoners_problem(num_prisoners):
            success_count += 1

    success_percentage = success_count / num_simulations * 100
    print(f"{num_prisoners}명의 죄수 중 모든 죄수가 최소한 한 번 선택된 확률: {success_percentage}%")


