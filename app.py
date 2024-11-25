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
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    year = int(input('년도를 입력하세요: '))
    month = int(input('월을 입력하세요: '))

    print('=== {}년 {:02d}월 할 일 목록 ==='.format(year, month))
    count = 0
    for idx, task in enumerate(todo_list):
        if task['due_date'].startswith('{}-{:02d}'.format(year, month)):
            count += 1
            task_info = (task['title'], task['due_date'], task['priority'])
            print("{}. 제목: {}, 기한: {}, 우선순위: {}".format(idx+1, task_info[0], task_info[1], task_info[2]))
    
    if count == 0:
        print('해당 월에 등록된 할 일이 없습니다.')
    print("================")

# 우선 순위별 할일 조회
def view_tasks_by_priority():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')

    print('=== 우선순위가 {}인 할 일 목록 ==='.format(priority))
    count = 0
    for idx, task in enumerate(todo_list):
        if task['priority'] == priority:
            count += 1
            task_info = (task['title'], task['due_date'], task['priority'])
            print("{}. 제목: {}, 기한: {}, 우선순위: {}".format(idx+1, task_info[0], task_info[1], task_info[2]))
    
    if count == 0:
        print('해당 우선순위에 등록된 할 일이 없습니다.')
    print("================")

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
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    todo_id = int(input('삭제할 할 일의 번호를 입력하세요: '))
    
    if todo_id < 1 or todo_id > len(todo_list):
        print('올바른 할 일 번호를 입력하세요.')
        return
    
    remove_todo = todo_list.pop(todo_id - 1)
    print('할일: {} 가 삭제되었습니다.'.format(remove_todo['title']))

# 할일 수정 기능
def update_task():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return

    todo_id = int(input('수정할 할 일의 번호를 입력하세요: '))

    if todo_id < 1 or todo_id > len(todo_list):
        print('올바른 할 일 번호를 입력하세요.')
        return
    
    todo = todo_list[todo_id - 1]
    
    print('수정 전 할 일 정보')
    print('제목: {}, 기한: {}, 우선순위: {}'.format(todo['title'], todo['due_date'], todo['priority']))
    print('할 일 정보를 수정하세요.')

    title = input('할 일 제목을 입력하세요: ')
    due_date = input('기한을 입력하세요 (예 2023-11-30): ')
    priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')

    update_todo = {
        'title': title,
        'due_date': due_date,
        'priority': priority
    }

    todo_list[todo_id - 1] = update_todo
    print('할 일이 수정되었습니다.')

    
def main():
    while True:
        print("===== 할 일 목록 관리 =====")
        print("1. 할 일 추가")
        print("2. 할 일 조회")
        print("3. 종료")
        print("4. 할 일 수정")
        print("5. 할 일 삭제")
        print("6. 날짜별 할 일 조회")
        print("7. 우선순위별 할 일 조회")
        print("==========================")
        choice = input("원하는 작업을 선택하세요: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        elif choice == '4':
            update_task()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            view_tasks_by_date()
        elif choice == '7':
            view_tasks_by_priority()
        else:
            print("올바른 번호를 입력하세요")
    # 프로그램의 맨 아래에서 main() 함수를 직접 호출합니다.

if __name__ == '__main__':
    main()