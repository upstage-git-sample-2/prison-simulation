# 조성운
def select_prisoner(prisoners, selected_prisoners):
    # 죄수 선택 및 기록
    selected_prisoner = random.choice(prisoners)
    selected_prisoners.add(selected_prisoner)
    return selected_prisoner