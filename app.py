import json
import random
from datetime import datetime
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import ttk

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
        msgbox.showerror("에러", "DB에 저장할수 없습니다.")
        print("DB에 저장할 수 없습니다.", e)
        

def load_todo_db():
    try:
        with open(TODO_FILE_PATH, 'r', encoding='UTF-8') as file:
            TODO_DB.clear()
            TODO_DB.extend(json.load(file))
    except FileNotFoundError:
        msgbox.showinfo("알림", "저장된 할 일이 없습니다.")
    except Exception as e:
        msgbox.showerror("에러", "DB를 불러올 수 없습니다.")
        print("DB를 불러올 수 없습니다.", e)
    else:
        msgbox.showinfo("알림", "DB를 성공적으로 불러왔습니다.")


def validate_priority(priority):
    if priority not in PRIORITY_LEVELS:
        raise ValueError("priority 값이 올바르지 않습니다.")
    return True

def validate_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("날짜 형식이 올바르지 않습니다. 올바른 형식: YYYY-MM-DD (예: 2023-10-01)")
    return True

def get_all_todos():
    return TODO_DB

def get_todos_by_date(target_date):
    """
    주어진 날짜에 해당하는 할 일 목록을 반환합니다.

    매개변수:
    target_date (str): 조회할 날짜 (형식: YYYY-MM-DD)

    반환값:
    list: 주어진 날짜에 해당하는 할 일 목록
    """
    # 결과를 저장할 리스트 초기화
    filtered_todos = []
    try:
        validate_date(target_date)  # 날짜 형식 검증
        todo_list = get_all_todos()  # 모든 할 일 목록 가져오기

        # todo_list에서 각 항목을 확인
        for todo in todo_list:
            if todo['due_date'] == target_date:  # 날짜가 일치하면
                filtered_todos.append(todo)  # 결과 리스트에 추가
    except ValueError as e:
        print(e)
    else:
        # 우선순위와 생성일을 기준으로 정렬
        filtered_todos.sort(key=lambda x: (x['priority'], x['created_at']))
        return filtered_todos

def get_todos_by_priority(priority):
    """
    주어진 우선순위에 해당하는 할 일 목록을 반환합니다.

    매개변수:
    priority (int): 조회할 우선순위 (높음: 0, 중간: 1, 낮음: 2)

    반환값:
    list: 주어진 우선순위에 해당하는 할 일 목록
    """
    try:
        validate_priority(priority)
        
        # 결과를 저장할 리스트 초기화
        todo_list = get_all_todos()
        filtered_todos = []
        
        for todo in todo_list:
            if todo['priority'] == priority:
                filtered_todos.append(todo)
    except ValueError:
        return []
    else:
        filtered_todos.sort(key=lambda x: (x['due_date'], x['created_at']))
        return filtered_todos

def add_todo(title, due_date, priority):
    """
    할 일을 추가합니다.

    매개변수:
    title (str): 할 일 제목
    due_date (str): 마감 날짜 (형식: YYYY-MM-DD)
    priority (int): 우선순위 (높음: 0, 중간: 1, 낮음: 2)

    반환값:
    bool: 할 일 추가 성공 여부 (성공: True, 실패: False)
    """
    try:
        validate_priority(priority)
        validate_date(due_date)
        # 할 일 정보를 딕셔너리로 저장
        todo = {
            'id': int(datetime.now().timestamp()),
            'title': title,
            'created_at': datetime.now().isoformat(),
            'due_date': due_date,
            'priority': priority
        }
        TODO_DB.append(todo) # 할 일 정보를 TODO_DB에 추가
        save_todo_db() # DB에 저장
    except ValueError as e:
        raise ValueError(e)
    else:
        return True

def get_todo(idx):
    todo_list = get_all_todos()

    if idx < 0 or idx >= len(todo_list):
        raise IndexError('todo id is out of range')

    return todo_list[idx]

def get_todo_index(id):
    todo_list = get_all_todos()

    for idx, todo in enumerate(todo_list):
        if todo['id'] == id:
            return idx
    return -1

    
# 할일 삭제 기능
def delete_todo(idx):
    todo_list = get_all_todos()
    if idx < 0 or idx >= len(todo_list):
        raise IndexError('todo id is out of range')
    TODO_DB.pop(idx)
    save_todo_db()
    return True

# 할일 수정 기능
def update_todo(idx, update_data):
    try:
        validate_priority(update_data['priority'])
        validate_date(update_data['due_date'])
        todo_list = get_all_todos()
        if idx < 0 or idx >= len(todo_list):
            raise IndexError('todo id is out of range')
        todo = todo_list[idx]
        
        for key in todo.keys():
            if key in update_data:
                todo[key] = update_data[key]
        
        save_todo_db()
    except ValueError as e:
        raise ValueError(e)
    else:
        return True


def sorting_todos_by_priority(priority=None, order='asc'):
    sorted_todos = []

    if priority is not None:
        todos = get_todos_by_priority(priority)
        sorted_todos.extend(todos)
    else:
        for todo in get_all_todos():
            sorted_todos.append(todo)
        if order == 'desc':
            sorted_todos.sort(key=lambda x: (-x['priority'], x['due_date'], x['created_at']))
        else:
            sorted_todos.sort(key=lambda x: (x['priority'], x['due_date'], x['created_at']))
        

    todo_treeview.delete(*todo_treeview.get_children())
    for _, todo in enumerate(sorted_todos):
        priority_value = PRIORITY_LEVELS[todo['priority']]
        todo_treeview.insert('', 'end', values=(todo['id'], todo['title'], todo['due_date'], priority_value))


def sorting_todos_by_date(order='asc'):
    sorted_todos = []
    for todo in get_all_todos():
        sorted_todos.append(todo)
    if order == 'desc':
        sorted_todos.sort(key=lambda x: (datetime.strptime(x['due_date'], '%Y-%m-%d'), -x['priority'], x['created_at']), reverse=True)
    else:
        sorted_todos.sort(key=lambda x: (x['due_date'], x['priority'], x['created_at']))

    todo_treeview.delete(*todo_treeview.get_children())
    for _, todo in enumerate(sorted_todos):
        priority_value = PRIORITY_LEVELS[todo['priority']]
        todo_treeview.insert('', 'end', values=(todo['id'], todo['title'], todo['due_date'], priority_value))

def create_todo_handler():
    try:
        title = todo_name_entry.get()
        due_date = todo_due_date_entry.get()
        priority = todo_priority_combobox.current()
            
        add_todo(title, due_date, priority)
    except ValueError as e:
        msgbox.showwarning("경고", e)
    else:
        msgbox.showinfo("알림", "할 일이 추가되었습니다.")
        populate_todo_treeview(todo_treeview)


def delete_todo_handler():
    try:
        # treeview에서 선택된 아이템의 정보를 가져옴
        selected_item = todo_treeview.selection()
        if not selected_item:
            msgbox.showwarning("경고", "삭제할 할 일을 선택하세요.")
            return
        todo_id = int(todo_treeview.item(selected_item, "values")[0])
        idx = get_todo_index(todo_id)
        delete_todo(idx)
    except IndexError:
        msgbox.showwarning("경고", "올바른 할 일 번호를 입력하세요")
    except:
        msgbox.showerror("에러", "할 일 삭제에 실패했습니다.")
    else:
        msgbox.showinfo("알림", "할 일이 삭제되었습니다.")
        populate_todo_treeview(todo_treeview)

def update_todo_handler():
    try:
        selected_item = todo_treeview.selection()
        if not selected_item:
            msgbox.showwarning("경고", "수정할 할 일을 선택하세요.")
            return
        todo_id = int(todo_treeview.item(selected_item, "values")[0])
        update_input_dto = {
            'title': todo_name_entry.get(),
            'due_date': todo_due_date_entry.get(),
            'priority': todo_priority_combobox.current()
        }
        idx = get_todo_index(todo_id)
        update_todo(idx, update_input_dto)
    except ValueError as e:
        msgbox.showwarning("경고", e)
    except Exception:
        msgbox.showerror("에러", "할 일 수정에 실패했습니다.")
    else:
        msgbox.showinfo("알림", "할 일이 수정되었습니다.")
        populate_todo_treeview(todo_treeview)

def clear_todo_handler():
    try:
        TODO_DB.clear()
        save_todo_db()
    except:
        msgbox.showerror("에러", "모든 할 일 삭제에 실패했습니다.")
    else:
        msgbox.showinfo("알림", "모든 할 일이 삭제되었습니다.")
        populate_todo_treeview(todo_treeview)

#랜덤모듈 활용 - 랜덤으로 할 일 추천받기
def recommend_todo():
    todo_list = get_all_todos()
    if not todo_list:
        msgbox.showinfo("알림", "오늘은 휴식을 취하세요.")
        return
    random_todo = random.choice(todo_list)
    msgbox.showinfo("오늘의 할 일 추천", "오늘 할일 추천: {}".format(random_todo['title']))

def populate_todo_treeview(treeview):
    treeview.delete(*treeview.get_children())
    for _, todo in enumerate(TODO_DB):
        priority_value = PRIORITY_LEVELS[todo['priority']]
        treeview.insert('', 'end', values=(todo['id'], todo['title'], todo['due_date'], priority_value))


def on_treeview_click(event):
    try:
        item = todo_treeview.selection()[0]
        item_id = int(todo_treeview.item(item, "values")[0])
        idx = get_todo_index(item_id)
        todo = get_todo(idx)
    except IndexError:
        pass
    else:
        todo_name_entry.delete(0, END)
        todo_name_entry.insert(0, todo['title'])
        todo_due_date_entry.delete(0, END)
        todo_due_date_entry.insert(0, todo['due_date'])
        priority_value = PRIORITY_LEVELS[todo['priority']]
        todo_priority_combobox.set(priority_value)

def backup_handler():
    try:
        with open('backup.json', 'w') as file:
            json.dump(TODO_DB, file)
    except:
        msgbox.showerror("에러", "백업에 실패했습니다.")
    else:
        msgbox.showinfo("알림", "백업이 완료되었습니다.")

# GUI 코드
window = Tk()
window.title("To-Do List App")
window.geometry("1024x768")

header_frame = Frame(window, height=50)
header_frame.grid(row=0, column=0, columnspan=2, sticky=E+W)

form_frame = Frame(window, bg="lightgreen", width=200)
form_frame.grid(row=1, column=0, rowspan=2, sticky=N+S)

content_frame = Frame(window, bg="lightblue")
content_frame.grid(row=1, column=1, rowspan=2, sticky=N+S+E+W)

nav_frame = Frame(window, height=50)
nav_frame.grid(row=3, column=0, columnspan=2, sticky=E+W)

window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(1, weight=1)

title_label = Label(header_frame, text="To-Do List App", font=("Helvetica", 24))
title_label.pack()

todo_name_label = Label(form_frame, text="할 일 제목", bg="lightgreen",fg="black")
todo_name_label.grid(row=0, column=0, pady=10)

todo_name_entry = Entry(form_frame)
todo_name_entry.grid(row=0, column=1, pady=10)

todo_due_date_label = Label(form_frame, text="기한", bg="lightgreen",fg="black")
todo_due_date_label.grid(row=1, column=0, pady=10)

todo_due_date_entry = Entry(form_frame)
todo_due_date_entry.grid(row=1, column=1, pady=10)

todo_priority_label = Label(form_frame, text="우선순위", bg="lightgreen",fg="black")
todo_priority_label.grid(row=2, column=0, pady=10)

todo_priority_combobox = ttk.Combobox(form_frame, values=list(PRIORITY_LEVELS.values()))
todo_priority_combobox.grid(row=2, column=1, pady=10, padx=10)

add_todo_btn = Button(nav_frame, text="할 일 추가", command=create_todo_handler)
add_todo_btn.grid(row=0, column=0)

update_todo_btn = Button(nav_frame, text="할 일 수정", command=update_todo_handler)
update_todo_btn.grid(row=0, column=1)

delete_todo_btn = Button(nav_frame, text="할 일 삭제", command=delete_todo_handler)
delete_todo_btn.grid(row=0, column=2)

recommend_todo_btn = Button(nav_frame, text="할 일 추천", command=recommend_todo, fg="darkgreen")
recommend_todo_btn.grid(row=0, column=3)

delete_all_todo_btn = Button(nav_frame, text="모든 할 일 삭제", command=clear_todo_handler)
delete_all_todo_btn.grid(row=0, column=4)

exit_btn = Button(nav_frame, text="종료", command=window.quit)
exit_btn.grid(row=0, column=5)

backup_btn = Button(nav_frame, text="백업", command=backup_handler)
backup_btn.grid(row=0, column=6)

search_frame = Frame(content_frame)
search_frame.pack()

columns = ("ID", "제목", "기한", "우선순위")
todo_treeview = ttk.Treeview(content_frame, columns=columns, show="headings")
todo_treeview.heading("ID", text="ID")
todo_treeview.heading("제목", text="제목")
todo_treeview.heading("기한", text="기한")
todo_treeview.heading("우선순위", text="우선순위")

todo_treeview.pack(fill=BOTH, expand=True)

def load_todos_based_on_sorting():
    if search_option_combobox.get() == "우선순위 높은순":
        sorting_todos_by_priority()
    elif search_option_combobox.get() == "우선순위 낮은순":
        sorting_todos_by_priority(order='desc')
    elif search_option_combobox.get() == "높음":
        sorting_todos_by_priority(priority=0)
    elif search_option_combobox.get() == "중간":
        sorting_todos_by_priority(priority=1)
    elif search_option_combobox.get() == "낮음":
        sorting_todos_by_priority(priority=2)
    elif search_option_combobox.get() == "마감기한 오름차순":
        sorting_todos_by_date()
    elif search_option_combobox.get() == "마감 기한 내림차순":
        sorting_todos_by_date(order='desc')
    else:
        populate_todo_treeview(todo_treeview)

search_option_label = Label(search_frame, text="정렬 옵션", fg="black")
search_option_label.grid(row=0, column=0, padx=10)
search_option_combobox = ttk.Combobox(search_frame, values=["우선순위 높은순", "우선순위 낮은순", "높음", "중간", "낮음", "마감기한 오름차순", "마감 기한 내림차순"], width=10)
search_option_combobox.grid(row=0, column=1, padx=[0, 200])

search_option_combobox.bind("<<ComboboxSelected>>", lambda event: load_todos_based_on_sorting())

search_btn = Button(search_frame, text="검색", command=None)
search_btn.grid(row=0, column=2)

seacrh_all_btn = Button(search_frame, text="전체 할 일 조회", command=lambda: populate_todo_treeview(todo_treeview))
seacrh_all_btn.grid(row=0, column=3)

todo_treeview.bind("<ButtonRelease-1>", on_treeview_click)

load_todo_db()
populate_todo_treeview(todo_treeview)

window.mainloop()