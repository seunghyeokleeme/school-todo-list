todo_list = []

VALID_PRIORITIES = ('높음', '중간', '낮음')

def print_todo_details(todo_id, todo):
    print("{}. 제목: {}, 기한: {}, 우선순위: {}".format(todo_id, todo['title'], todo['due_date'], todo['priority']))

def get_todo_by_id(todo_id):
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return None

    if todo_id < 1 or todo_id > len(todo_list):
        print('올바른 할 일 번호를 입력하세요.')
        return None

    return todo_list[todo_id - 1]

def add_todo(title, due_date, priority):
    if priority not in VALID_PRIORITIES:
        print('올바른 우선순위를 입력하세요.')
        return
    
    # 할 일 정보를 딕셔너리로 저장
    todo = {
        'title': title,
        'due_date': due_date,
        'priority': priority
    }
    todo_list.append(todo)
    print('할 일이 추가되었습니다.')

# 할일 삭제 기능
def delete_todo(todo_id):
    if not get_todo_by_id(todo_id):
        return
    
    remove_todo = todo_list.pop(todo_id - 1)
    print('할일: {} 가 삭제되었습니다.'.format(remove_todo['title']))

# 할일 수정 기능
def update_todo(todo_id, title, due_date, priority):
    if not get_todo_by_id(todo_id):
        return
    
    if priority not in VALID_PRIORITIES:
        print('올바른 우선순위를 입력하세요.')
        return

    todo = todo_list[todo_id - 1]
    
    print('수정 전 할 일 정보')
    print_todo_details(todo_id, todo)

    todo['title'] = title
    todo['due_date'] = due_date
    todo['priority'] = priority
    
    print('수정 후 할 일 정보')
    print_todo_details(todo_id, todo)
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
def get_todos_by_date(year, month):
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
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
def get_todos_by_priority(priority):
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return

    print('=== 우선순위가 {}인 할 일 목록 ==='.format(priority))
    count = 0
    for idx, todo in enumerate(todo_list):
        if todo['priority'] == priority:
            count += 1
            print_todo_details(idx+1, todo)
    
    if count == 0:
        print('해당 우선순위에 등록된 할 일이 없습니다.')
    print("================")
