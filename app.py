""" 할 일 추가/삭제/수정 기능:
• 리스트와 딕셔너리등을 활용하여 구현
• 할 일 조회 기능:
• 날짜별, 우선순위별, 카테고리별로 할 일 조회
• 데이터 저장 및 로드:
• 파일 입출력과 예외 처리를 통해 데이터의 지속성 확보
• 사용자 입력 검증:
• 잘못된 입력에 대한 예외 처리
• GUI 인터페이스 구현:
• Tkinter를 활용한 사용자 친화적 인터페이스 """

todo_list = []

def view_tasks():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    print('=== 할 일 목록 ===')
    for idx, task in enumerate(todo_list):
        # 딕셔너리의 값을 튜플로 변환하여 출력
        task_info = (task['title'], task['due_date'], task['priority'])
        print("{}. 제목: {}, 기한: {}, 우선순위: {}".format(idx+1, task_info[0], task_info[1], task_info[2]))
    print("================")

# 날짜별 할일 조회
def view_tasks_by_date():
    pass 

# 우선 순위별 할일 조회
def view_tasks_by_priority():
    pass

def add_task():
    title = input('할 일 제목을 입력하세요: ')
    due_date = input('기한을 입력하세요 (예 2023-11-30): ')
    priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')

    # 할 일 정보를 딕셔너리로 저장
    task = {
        'title': title,
        'due_date': due_date,
        'priority': priority
    }
    todo_list.append(task)
    print('할 일이 추가되었습니다.')

# 할일 삭제 기능
def delete_task():
    pass

# 할일 수정 기능
def update_task():
    pass
    
def main():
    while True:
        print("===== 할 일 목록 관리 =====")
        print("1. 할 일 추가")
        print("2. 할 일 조회")
        print("3. 종료")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력하세요")
    # 프로그램의 맨 아래에서 main() 함수를 직접 호출합니다.

if __name__ == '__main__':
    main()