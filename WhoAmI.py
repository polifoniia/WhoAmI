import tkinter as tk
from tkinter import messagebox, font
import os

def setup_font():
    available_fonts = font.families()
    
    preferred_fonts = [
        "Comic Sans MS",
        "Arial Rounded MT Bold", 
        "Segoe UI",
        "Helvetica",
        "DejaVu Sans",
        "Tahoma",
        "Arial"
    ]
    
    for font_name in preferred_fonts:
        if font_name in available_fonts:
            return font.Font(family=font_name, size=12)
    
    return font.Font(family="Arial", size=12)

def set_icon(window):
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
      
        icon_file = 'icon.ico'

        icon_path = os.path.join(base_path, icon_file)
        if os.path.exists(icon_path):
            window.iconbitmap(icon_path)
            # print(f"Иконка загружена: {icon_file}")
            return True
        print("Іконки файлу не знайдено. Перевірте наявність icon.ico в папці з програмою")
        return False
    
    except Exception as e:
        print(f"Ошибка завантаження іконок: {e}")
        return False

colors = {
    'primary': '#FF6B8B',
    'secondary': '#4ECDC4',
    'accent1': '#45B7D1',
    'accent2': '#FFBE0B',
    'accent3': '#FB5607',
    'accent4': '#8338EC',
    'success': '#06D6A0',
    'danger': '#FF6B6B',
}

current_test = None
current_question = 0
scores = {"A": 0, "B": 0, "C": 0, "D": 0}
selected_answer = ""
answer_buttons = []

window = tk.Tk()
window.title("Хто я?")
window.geometry("900x700")
window.configure(bg='white')
window.resizable(False, False)

set_icon(window)

app_font = setup_font()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (900 // 2)
y = (screen_height // 2) - (700 // 2)
window.geometry(f'900x700+{x}+{y}')

def show_custom_confirm():
    confirm_window = tk.Toplevel(window)
    confirm_window.title("Підтвердження виходу")
    confirm_window.geometry("400x200")
    confirm_window.configure(bg='white')
    confirm_window.resizable(False, False)
    
    set_icon(confirm_window)
    
    confirm_window.transient(window)
    confirm_window.grab_set()
    
    cw_x = window.winfo_x() + (window.winfo_width() // 2) - (400 // 2)
    cw_y = window.winfo_y() + (window.winfo_height() // 2) - (200 // 2)
    confirm_window.geometry(f'400x200+{cw_x}+{cw_y}')
    
    title_font = (app_font.actual("family"), 16, "bold")
    text_font = (app_font.actual("family"), 12)
    button_font = (app_font.actual("family"), 11, "bold")
    
    tk.Label(confirm_window, text="Вихід з програми", 
             font=title_font,
             bg='white', fg=colors['primary']).pack(pady=15)
    
    tk.Label(confirm_window, text="Ти впевнений, що хочеш вийти з програми?",
             font=text_font,
             bg='white', fg='#666', wraplength=350).pack(pady=10)
    
    button_frame = tk.Frame(confirm_window, bg='white')
    button_frame.pack(pady=20)
    
    def confirm_exit():
        confirm_window.destroy()
        window.destroy()
    
    tk.Button(button_frame, text="Так, вийти", 
              font=button_font,
              bg=colors['danger'], fg='white',
              width=10, command=confirm_exit).pack(side=tk.LEFT, padx=10)
    
    tk.Button(button_frame, text="Ні, залишитись", 
              font=button_font,
              bg=colors['secondary'], fg='white',
              width=12, command=confirm_window.destroy).pack(side=tk.LEFT, padx=10)

def clear_window():
    for w in window.winfo_children():
        w.destroy()

def exit_app():
    show_custom_confirm()

def create_main_menu():
    clear_window()
    frame = tk.Frame(window, bg='white')
    frame.pack(expand=True, fill='both', padx=20, pady=20)

    title_font = (app_font.actual("family"), 26, "bold")
    subtitle_font = (app_font.actual("family"), 16)
    button_font = (app_font.actual("family"), 14, "bold")
    info_font = (app_font.actual("family"), 12)
    exit_font = (app_font.actual("family"), 12, "bold")

    tk.Label(frame, text=" ВЕСЕЛІ ТЕСТИ ДЛЯ ДІТЕЙ ",
             font=title_font,
             bg='white', fg=colors['primary']).pack(pady=10)

    tk.Label(frame, text="Обери тест, який хочеш пройти:",
             font=subtitle_font,
             bg='white', fg='#666').pack(pady=20)

    tk.Button(frame, text="Ким я стану, коли виросту?",
              font=button_font,
              bg=colors['secondary'], fg='white',
              height=3, command=start_profession_test).pack(fill='x', pady=15, padx=100)

    tk.Button(frame, text="Який у мене характер?",
              font=button_font,
              bg=colors['accent1'], fg='white',
              height=3, command=start_character_test).pack(fill='x', pady=15, padx=100)

    tk.Label(frame, text=" Навчальний додаток, який допоможе дізнатися про професії та свій характер!",
             font=info_font,
             bg='white', fg='#888').pack(pady=10)

    tk.Button(frame, text="Вийти з програми",
              font=exit_font,
              bg=colors['danger'], fg='white',
              height=2, command=exit_app).pack(fill='x', pady=20, padx=150)

def start_profession_test():
    global current_test, current_question, scores
    current_test = "profession"
    current_question = 0
    scores = {"A": 0, "B": 0, "C": 0, "D": 0}
    show_question()

def start_character_test():
    global current_test, current_question, scores
    current_test = "character"
    current_question = 0
    scores = {"A": 0, "B": 0, "C": 0, "D": 0}
    show_question()

def get_questions():
    if current_test == "profession":
        return [
            {
                "text": " Що тобі більше подобається робити?",
                "options": [
                    "A. Малювати, співати, танцювати ",
                    "B. Грати з друзями, допомагати іншим ",
                    "C. Збирати конструктор, розбирати іграшки ",
                    "D. Спостерігати за природою, доглядати за тваринами "
                ]
            },
            {
                "text": " Яку книжку ти обереш?",
                "options": [
                    "A. Казки або комікси ",
                    "B. Історії про дружбу ",
                    "C. Енциклопедію про техніку ",
                    "D. Книжку про тварин або рослини "
                ]
            },
            {
                "text": " Ким ти уявляєш себе в грі?",
                "options": [
                    "A. Артистом або чарівником ",
                    "B. Лікарем або вчителем ",
                    "C. Винахідником або будівельником ",
                    "D. Дослідником або фермером "
                ]
            }
        ]
    else:
        return [
            {
                "text": " Як ти зазвичай граєш?",
                "options": [
                    "A. Швидко перемикаюся між іграми ",
                    "B. Спокійно та акуратно ",
                    "C. Дуже активно, люблю бігати ",
                    "D. Довго граю в одну гру "
                ]
            },
            {
                "text": " Що ти робиш, коли засмучений?",
                "options": [
                    "A. Швидко забуваю та починаю нову справу ",
                    "B. Тихо сиджу в куточку ",
                    "C. Голосно виражаю емоції ",
                    "D. Довго не можу заспокоїтися "
                ]
            },
            {
                "text": " Як ти знайомишся з новими дітьми?",
                "options": [
                    "A. Легко та швидко ",
                    "B. Чекаю, коли підійдуть до мене ",
                    "C. Відразу пропоную пограти ",
                    "D. Довго придивляюся "
                ]
            }
        ]

def update_button_styles():
    for i, btn in enumerate(answer_buttons):
        option_letter = btn["text"][0]
        if option_letter == selected_answer:
            btn.config(font=(app_font.actual("family"), 12, "bold"),
                      bg=colors['accent2'],
                      fg='black',
                      relief=tk.RAISED,
                      bd=4,
                      padx=10,
                      pady=8)
        else:
            original_colors = [colors['primary'], colors['secondary'], colors['accent1'], colors['accent4']]
            btn.config(font=(app_font.actual("family"), 11, "bold"),
                      bg=original_colors[i],
                      fg='white',
                      relief=tk.RAISED,
                      bd=2,
                      padx=5,
                      pady=5)

def show_question():
    global selected_answer, next_button, answer_buttons
    clear_window()
    questions = get_questions()
    q = questions[current_question]

    frame = tk.Frame(window, bg='white')
    frame.pack(expand=True, fill='both', padx=20, pady=20)

    question_num_font = (app_font.actual("family"), 14, "bold")
    question_text_font = (app_font.actual("family"), 16, "bold")
    option_font = (app_font.actual("family"), 11, "bold")
    button_font = (app_font.actual("family"), 13, "bold")
    hint_font = (app_font.actual("family"), 10)

    tk.Label(frame, text=f"Питання {current_question + 1} з {len(questions)}",
             font=question_num_font,
             fg=colors['primary'], bg='white').pack(pady=10)

    tk.Label(frame, text=q["text"],
             font=question_text_font,
             bg='white', fg='#333', wraplength=600, justify='center').pack(pady=20)

    selected_answer = ""
    answer_buttons = []

    color_list = [colors['primary'], colors['secondary'], colors['accent1'], colors['accent4']]
    for i, opt in enumerate(q["options"]):
        btn = tk.Button(frame, text=opt,
                        bg=color_list[i], fg='white',
                        font=option_font,
                        height=2, 
                        wraplength=500,
                        padx=5,
                        pady=5,
                        command=lambda o=opt[0]: select_answer(o))
        btn.pack(fill='x', padx=100, pady=8)
        answer_buttons.append(btn)

    next_button = tk.Button(frame, text="ДАЛІ",
                            font=button_font,
                            state='disabled', bg='#CCCCCC', fg='white',
                            height=2, command=next_question)
    next_button.pack(pady=20)

    tk.Label(frame, text=" Обери один варіант відповіді та натисни 'ДАЛІ'",
             font=hint_font,
             bg='white', fg='#888').pack()

def select_answer(a):
    global selected_answer
    selected_answer = a
    next_button.config(state='normal', bg=colors['success'])
    update_button_styles()

def next_question():
    global current_question, scores
    if selected_answer:
        scores[selected_answer] += 1
    questions = get_questions()
    if current_question < len(questions) - 1:
        current_question += 1
        show_question()
    else:
        show_result()

def show_result():
    clear_window()
    max_score = max(scores.values())
    result_type = [k for k, v in scores.items() if v == max_score][0]

    if current_test == "profession":
        results = {
            "A": ("🎨 ТИ - ТВОРЕЦЬ! 🎨",
                  "У тебе багата фантазія та творчі здібності!\n\n"
                  "Тобі підходять:\n• Художник\n• Дизайнер\n• Актор\n• Музикант\n• Письменник\n\n"
                  "Твої суперсили: уява, креативність, емоційність!",
                  colors['primary']),
            "B": ("👥 ТИ - ПОМІЧНИК! 👥",
                  "Ти добрий, чуйний та любиш допомагати іншим!\n\n"
                  "Тобі підходять:\n• Вчитель\n• Лікар\n• Психолог\n• Вихователь\n• Тренер\n\n"
                  "Твої суперсили: доброта, товариськість, турбота!",
                  colors['secondary']),
            "C": ("🔧 ТИ - ВИНАХІДНИК! 🔧",
                  "Ти розумний, допитливий та любиш створювати нове!\n\n"
                  "Тобі підходять:\n• Інженер\n• Програміст\n• Вчений\n• Архітектор\n• Механік\n\n"
                  "Твої суперсили: логіка, уважність, винахідливість!",
                  colors['accent1']),
            "D": ("🌿 ТИ - ДОСЛІДНИК! 🌿",
                  "Ти любиш природу та цікаві відкриття!\n\n"
                  "Тобі підходять:\n• Ветеринар\n• Еколог\n• Біолог\n• Геолог\n• Фермер\n\n"
                  "Твої суперсили: спостережливість, терпіння, любов до природи!",
                  colors['success'])
        }
        special = "Пам'ятай: обирай професію, яка приносить радість і щастя!"
    else:
        results = {
            "A": ("😊 ТИ - САНГВІНІК! 😊",
                  "Ти - сонечко в будь-якій компанії!\n\n"
                  "• Легко знаходиш друзів\n• Завжди в гарному настрої\n• Любиш веселі ігри\n• Швидко перемикаєш увагу\n\n"
                  "Твоя суперсила: вміння радувати оточуючих!",
                  colors['accent2']),
            "B": ("😌 ТИ - ФЛЕГМАТИК! 😌",
                  "Ти - надійний друг та спокійний товариш!\n\n"
                  "• Завжди доводиш справи до кінця\n• Любиш порядок\n• Терплячий та уважний\n• На тебе можна покластися\n\n"
                  "Твоя суперсила: спокій у будь-яких ситуаціях!",
                  colors['accent1']),
            "C": ("🤩 ТИ - ХОЛЕРИК! 🤩",
                  "Ти - джерело енергії та ідей!\n\n"
                  "• Повний ентузіазму\n• Любиш бути лідером\n• Швидко приймаєш рішення\n• Завжди в русі\n\n"
                  "Твоя суперсила: вміння вести за собою!",
                  colors['accent3']),
            "D": ("🤔 ТИ - МЕЛАНХОЛІК! 🤔",
                  "Ти - чуйна та уважна людина!\n\n"
                  "• Помічаєш те, чого інші не бачать\n• Маєш багатий внутрішній світ\n• Творча та мрійлива\n• Вірна та віддана людина\n\n"
                  "Твоя суперсила: глибина почуттів та думок!",
                  colors['accent4'])
        }
        special = "Приймай себе таким, який ти є, і розвивай свої сильні сторони!"

    title, text, color = results[result_type]

    frame = tk.Frame(window, bg='white')
    frame.pack(expand=True, fill='both', padx=20, pady=20)

    title_font = (app_font.actual("family"), 22, "bold")
    text_font = (app_font.actual("family"), 12)
    button_font = (app_font.actual("family"), 12, "bold")

    tk.Label(frame, text=title, font=title_font,
             fg=color, bg='white').pack(pady=20)

    text_box = tk.Text(frame, font=text_font,
                       bg='#F8F9FA', fg='#333', wrap=tk.WORD, height=15, width=80, bd=0)
    text_box.insert(tk.END, text + "\n\n" + special)
    text_box.tag_add("special", "end-%dc" % (len(special) + 1), "end")
    text_box.tag_config("special", foreground=colors['primary'])
    text_box.config(state='disabled')
    text_box.pack(pady=10)

    tk.Button(frame, text=" Головне меню", bg=colors['success'], fg='white',
              font=button_font, command=create_main_menu).pack(fill='x', padx=100, pady=10)
    tk.Button(frame, text="Вийти", bg=colors['danger'], fg='white',
              font=button_font, command=exit_app).pack(fill='x', padx=100, pady=10)

create_main_menu()
window.mainloop()
