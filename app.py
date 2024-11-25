from todo import add_todo, delete_todo, update_todo, get_all_todos, get_todos_by_date, get_todos_by_priority

def main():
    while True:
        print("===== 할 일 목록 관리 =====")
        print("0. 종료")
        print("1. 할 일 추가")
        print("2. 할 일 수정")
        print("3. 할 일 삭제")
        print("4. 할 일 목록 조회")
        print("5. 날짜별 할 일 목록 조회")
        print("6. 우선순위별 할 일 목록 조회")
        print("==========================")
        choice = int(input("원하는 작업을 선택하세요 (예 1): "))

        if choice == 0:
            print("프로그램을 종료합니다.")
            break
        elif choice == 1:
            add_todo()
        elif choice == 2:
            update_todo()
        elif choice == 3:
            delete_todo()
        elif choice == 4:
            get_all_todos()
        elif choice == 5:
            get_todos_by_date()
        elif choice == 6:
            get_todos_by_priority()
        else:
            print("올바른 번호를 입력하세요")


if __name__ == '__main__':
    main()