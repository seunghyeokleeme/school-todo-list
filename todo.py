todo_list = []

def print_todo_details(todo_id, todo):
    print("{}. 제목: {}, 기한: {}, 우선순위: {}".format(todo_id, todo['title'], todo['due_date'], todo['priority']))

def add_todo():
    title = input('할 일 제목을 입력하세요: ')
    due_date = input('기한을 입력하세요 (예 2023-09-03): ')
    priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')

    # 할 일 정보를 딕셔너리로 저장
    todo = {
        'title': title,
        'due_date': due_date,
        'priority': priority
    }
    todo_list.append(todo)
    print('할 일이 추가되었습니다.')

# 할일 삭제 기능
def delete_todo():
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
def update_todo():
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

    updated_todo = {
        'title': title,
        'due_date': due_date,
        'priority': priority
    }

    todo_list[todo_id - 1] = updated_todo
    print('할 일이 수정되었습니다.')

def get_all_todos():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    print('=== 할 일 목록 ===')
    for idx, todo in enumerate(todo_list):
        print_todo_details(idx+1, todo)
    print("================")

# 날짜별 할일 조회
def get_todos_by_date():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    year = int(input('년도를 입력하세요: '))
    month = int(input('월을 입력하세요: '))

    print('=== {}년 {:02d}월 할 일 목록 ==='.format(year, month))
    count = 0
    for idx, todo in enumerate(todo_list):
        if todo['due_date'].startswith('{}-{:02d}'.format(year, month)):
            count += 1
            print_todo_details(idx+1, todo)
    
    if count == 0:
        print('해당 월에 등록된 할 일이 없습니다.')
    print("================")

# 우선 순위별 할일 조회
def get_todos_by_priority():
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    priority = input('우선순위를 입력하세요 (높음, 중간, 낮음): ')

    print('=== 우선순위가 {}인 할 일 목록 ==='.format(priority))
    count = 0
    for idx, todo in enumerate(todo_list):
        if todo['priority'] == priority:
            count += 1
            print_todo_details(idx+1, todo)
    
    if count == 0:
        print('해당 우선순위에 등록된 할 일이 없습니다.')
    print("================")
