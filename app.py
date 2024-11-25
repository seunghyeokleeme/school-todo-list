from todo import add_todo, delete_todo, update_todo, get_all_todos, get_todos_by_date, get_todos_by_priority
from menu import display_menu

def handle_choice(choice):
    if choice == 0:
        print("프로그램을 종료합니다.")
        return False
    elif choice == 1:
        title = input('할 일 제목을 입력하세요: ')
        due_date = input('기한을 입력하세요 (예 2023-09-03): ')
        priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')
        add_todo(title, due_date, priority)
    elif choice == 2:
        todo_id = int(input('수정할 할 일의 번호를 입력하세요: '))
        print('할 일 정보를 수정하세요.')
        title = input('할 일 제목을 입력하세요: ')
        due_date = input('기한을 입력하세요 (예 2023-11-30): ')
        priority = input('우선순위를 입력하세요 (높음/중간/낮음): ')
        update_todo(todo_id, title, due_date, priority)
    elif choice == 3:
        todo_id = int(input('삭제할 할 일의 번호를 입력하세요: '))
        delete_todo(todo_id)
    elif choice == 4:
        get_all_todos()
    elif choice == 5:
        year = int(input('년도를 입력하세요: '))
        month = int(input('월을 입력하세요: '))
        get_todos_by_date(year, month)
    elif choice == 6:
        priority = input('우선순위를 입력하세요 (높음, 중간, 낮음): ')
        get_todos_by_priority(priority)
    else:
        print("올바른 번호를 입력하세요")
    return True

def main():
    while True:
        display_menu()
        choice = int(input("원하는 작업을 선택하세요 (예 1): "))

        if not handle_choice(choice):
            break


if __name__ == '__main__':
    main()