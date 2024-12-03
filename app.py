import json

TODO_DB = []
TODO_FILE_PATH = 'todos.json'
PRIORITY_LEVELS = {
    0: '높음',
    1: '중간',
    2: '낮음'
}

# 할 일 정보를 저장할 JSON 파일 경로
def save_todo_db():
    try:
        with open(TODO_FILE_PATH, 'w') as file:
            json.dump(TODO_DB, file)
    except Exception as e:
        print("DB에 저장할수 없습니다.", e)
    else: 
        print("DB에 저장되었습니다.")

def load_todo_db():
    try:
        with open(TODO_FILE_PATH, 'r') as file:
            TODO_DB.extend(json.load(file))
    except FileNotFoundError:
        print("저장된 데이터가 없습니다.")
    except Exception as e:
        print("DB를 불러올 수 없습니다.", e)
    else:
        print("DB를 불러왔습니다.")
    finally:
        print("DB를 불러오는 작업이 완료되었습니다.")

def print_todo_details(id, todo):
    priority_value = PRIORITY_LEVELS[todo['priority']]
    print("{0}. [ ] {1} (기한: {2}, 우선순위: {3})".format(id, todo['title'], todo['due_date'], priority_value))

def validate_priority(priority):
    if priority not in PRIORITY_LEVELS:
        raise ValueError("priority 값이 올바르지 않습니다.")
    return True

def get_all_todos():
    return TODO_DB

def get_todos_by_date(target_date):
    # 결과를 저장할 리스트 초기화
    filtered_todos = []
    try:
        todo_list = get_all_todos()

        # todo_list에서 각 항목을 확인
        for todo in todo_list:
            if todo['due_date'] == target_date:  # 날짜가 일치하면
                filtered_todos.append(todo)  # 결과 리스트에 추가
    except ValueError:
        print("올바른 날짜 형식을 입력하세요. (예: YYYY-MM-DD)")
    else:
        filtered_todos.sort(key=lambda x: x['priority'])
        return filtered_todos

def get_todos_by_priority(priority):
    filtered_todos = []
    try:
        validate_priority(priority)
        
        # 결과를 저장할 리스트 초기화
        todo_list = get_all_todos()
        
        for todo in todo_list:
            if todo['priority'] == priority:
                filtered_todos.append(todo)
    except ValueError:
        print("올바른 우선순위를 입력하세요. (높음: 0, 중간: 1, 낮음: 2)")
    else:
        filtered_todos.sort(key=lambda x: x['due_date'])
        return filtered_todos

def add_todo(title, due_date, priority):
    try:
        validate_priority(priority)
        # 할 일 정보를 딕셔너리로 저장
        todo = {
            'title': title,
            'due_date': due_date,
            'priority': priority
        }
        TODO_DB.append(todo) # 할 일 정보를 TODO_DB에 추가
        save_todo_db() # DB에 저장
    except ValueError:
        print("유효한 데이터를 입력하세요")
        return False
    else:
        print('할 일이 추가되었습니다.')
        return True

def get_todo(id):
    todo_list = get_all_todos()

    if id < 0 or id >= len(todo_list):
        raise IndexError('todo id is out of range')

    return todo_list[id]
    
# 할일 삭제 기능
def delete_todo(id):
    try:
        todo_list = get_all_todos()
        if id < 0 or id >= len(todo_list):
            raise IndexError('todo id is out of range')
        TODO_DB.pop(id)
        save_todo_db()
    except IndexError:
        print("id 값이 올바르지 않습니다.")
    else:
        print('할 일 삭제 기능이 수행되었습니다.')
        return True

# 할일 수정 기능
def update_todo(id, update_data):
    try:
        validate_priority(update_data['priority'])
        todo_list = get_all_todos()
        if id < 0 or id >= len(todo_list):
            raise IndexError('todo id is out of range')
        todo = todo_list[id]
        
        for key in todo.keys():
            if key in update_data:
                todo[key] = update_data[key]
        
        save_todo_db()
    except ValueError:
        print("우선순위 값이 올바르지 않습니다.")
    except IndexError:
        print("올바른 할 일 번호를 입력하세요")
    except:
        print("DB에 수정할 수 없습니다.")
    else:
        print('할 일이 수정되었습니다.')
        return True

def view_todos():
    todo_list = get_all_todos()
    if not todo_list:
        print('등록된 할 일이 없습니다.')
        return
    
    print("=== 전체 할 일 목록 ===")
    for idx, todo in enumerate(todo_list):
        print_todo_details(idx+1, todo)
    print("===========================")

def search_todos_by_priority():
    priority = int(input("우선순위를 선택하세요. (높음: 0, 중간: 1, 낮음: 2): "))
    filtered_todos = get_todos_by_priority(priority)
    
    # gui
    if not filtered_todos:
        print("해당 우선순위에 등록된 할 일이 없습니다.")
        return
    print("=== 우선순위가 {}인 할 일 목록 ===".format(PRIORITY_LEVELS[priority]))
    for idx, todo in enumerate(filtered_todos):
        print_todo_details(idx+1, todo)
    print("===========================")

def search_todos_by_date():
    search_date = input('날짜를 입력하세요 (예 YYYY-MM-DD): ')
    filtered_todos = get_todos_by_date(search_date)

    # gui
    if not filtered_todos:
        print("해당 날짜에 등록된 할 일이 없습니다.")
        return
    print("=== 날짜가 {}인 할 일 목록 ===".format(search_date))
    for idx, todo in enumerate(filtered_todos):
        print_todo_details(idx+1, todo)
    print("===========================")

def create_todo_item():
    try:
        title = input('할 일 제목을 입력하세요: ')
        due_date = input('기한을 입력하세요 (예 YYYY-MM-DD): ')
        priority = int(input('우선순위를 선택하세요. (높음: 0, 중간: 1, 낮음: 2): '))
            
        add_todo(title, due_date, priority)
    except ValueError:
        print("올바른 데이터를 입력하세요")

def delete_todo_item():
    try:
        todo_id = int(input('삭제할 할 일 번호를 입력하세요: '))
        delete_todo(todo_id)
    except ValueError:
        print("올바른 데이터를 입력하세요")

def update_todo_item():
    try:
        todo_id = int(input('수정할 할 일 번호를 입력하세요: '))
        update_input_dto = {
            'title': input('할 일 제목을 입력하세요: '),
            'due_date': input('기한을 입력하세요 (예 YYYY-MM-DD): '),
            'priority': int(input('우선순위를 선택하세요. (높음: 0, 중간: 1, 낮음: 2): '))
        }
        update_todo(todo_id, update_input_dto)
    except ValueError:
        print("올바른 데이터를 입력하세요")


def display_menu():
    print("===== To-Do List APP =====")
    print("0. 종료")
    print("1. 할 일 추가")
    print("2. 할 일 수정")
    print("3. 할 일 삭제")
    print("4. 할 일 조회")
    print("5. 날짜별 할 일 조회")
    print("6. 우선순위별 할 일 조회")
    print("===========================")

def handle_todo_action(choice):
    if choice == '1':
        create_todo_item()
    elif choice == '2':
        update_todo_item()
    elif choice == '3':
        delete_todo_item()
    elif choice == '4':
        view_todos()
    elif choice == '5':
        search_todos_by_date()
    elif choice == '6':
        search_todos_by_priority()
    else:
        print("올바른 메뉴 번호를 입력하세요(0-6)")

def main():
    load_todo_db()
    while True:
        try:
            display_menu()
            choice = input("원하는 작업을 선택하세요: ")

            if choice == '0':
                print("프로그램을 종료합니다.")
                save_todo_db()
                break
           
            handle_todo_action(choice)
        except Exception as e:
            print("예외가 발생했습니다.", e)
        finally:
            print()

if __name__ == '__main__':
    main()