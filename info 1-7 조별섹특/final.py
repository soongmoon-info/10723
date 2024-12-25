import math

# 두 점 간의 유클리드 거리 계산
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# 최소 거리와 경로를 추적
min_distance = float('inf')
min_path = []

# 각 점에 대한 고유 이름을 정의한 점들
points = {
    "레드": (322, 149),
    "칼날부리": (294, 209),
    "돌거북": (351, 96),
    "블루": (167, 312),
    "두꺼비": (107, 334),
    "늑대": (166, 253)
}

# 종착점들
end_points = {
    "탑": (0, 570),
    "미드": (300, 285),
    "바텀": (600, 0)
}

# 백트래킹 함수
def backtracking(current_point, remaining_points, path, distance, end_point):
    global min_distance, min_path

    # 모든 점을 거쳤으면 종료하고 종착점까지 계산
    if not remaining_points:
        # 종착점으로 가는 거리 추가
        total_distance = distance + euclidean_distance(current_point, end_point)
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = path + [list(end_points.keys())[list(end_points.values()).index(end_point)]]  # 종착점 추가
        return

    # 남은 점들에 대해 백트래킹
    for next_point_name, next_point in remaining_points.items():
        new_remaining_points = remaining_points.copy()
        new_remaining_points.pop(next_point_name)  # 현재 점을 제외한 나머지 점들
        backtracking(next_point, new_remaining_points, path + [next_point_name], distance + euclidean_distance(current_point, next_point), end_point)

# 사용자가 지나고 싶은 점들 입력 받기
def get_user_input():
    print("가능한 점들: ")
    for name, point in points.items():
        print(f"{name}. {point}")

    selected_names = input("지나고 싶은 점들의 이름을 입력하세요 (예: 레드 칼날부리 늑대): ").split()
    selected_points = {name: points[name] for name in selected_names}

    print("\n종착점 선택: ")
    for name, point in end_points.items():
        print(f"{name}. {point}")

    end_name = input("종착점 이름을 선택하세요 (탑, 미드, 바텀): ")
    end_point = end_points[end_name]

    return selected_points, end_point

# 시작점에서 백트래킹 시작
start_point = (0, 0)
selected_points, end_point = get_user_input()

# 백트래킹 시작
backtracking(start_point, selected_points, ["Start"], 0, end_point)

# 결과 출력
print("\n최소 경로:", min_path)
print("최소 거리:", min_distance)
