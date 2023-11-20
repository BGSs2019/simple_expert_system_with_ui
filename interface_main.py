#импорт элементов библиотеки tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter.messagebox import showinfo
from tkinter import ttk
from datetime import datetime

#плохое объявление структур для заполнения таблицы
bool_parameters = []
num_parameters = []
str_parameters = []
strnum_parameters = []
#плохое задание для значения целевой функции
ava_sum = 0.0
ava_mul = 1.0

#функция для выравнивания таблиц
def column_width(num_of_columns):
    return int(640/(num_of_columns-2))

#функция для обработки действий кнопки открытия файла
def open_file_click():

    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    filename = fd.askopenfilename(title='Open a file', filetypes=filetypes)

    if filename:
        path_line.delete("0.0", END)
        path_line.insert(END, filename)

        try:
            with open(filename, 'r') as ft:
                #обнуляем списки и таблицы
                bool_parameters = []
                num_parameters = []
                str_parameters = []
                strnum_parameters = []

                bool_tree.delete(*bool_tree.get_children())
                num_tree.delete(*num_tree.get_children())
                str_tree.delete(*str_tree.get_children())
                strnum_tree.delete(*strnum_tree.get_children())

                params = 0

                for line in ft:
                    if line.split(' ')[0] == 'Type:':
                        params = params + 1
                        print('Found '+ str(params) + ' parameters')
                        param_type = line.split(' ')[1][:-1]
                        print('Param type: ' + param_type)

                        if param_type == 'Bool':
                            param_name = next(ft).split(' ')[1][:-1]
                            print('Name of found parameter: ' + param_name)

                            param_num = int(next(ft).split(' ')[1][:-1])
                            print('Num of param: ' + str(param_num))

                            bool_value = bool(next(ft).split(' ')[1][:-1])
                            print('Bool value: ' + str(bool_value))

                            bool_weight = float(next(ft).split(' ')[1][:-1])
                            print('Bool weight: ' + str(bool_weight))

                            bool_parameters.append(tuple((param_num, param_name, bool_value, bool_weight)))
                            print(bool_parameters)

                        if param_type == 'Num':
                            param_name = next(ft).split(' ')[1][:-1]
                            print('Name of found parameter: ' + param_name)
                            
                            param_num = int(next(ft).split(' ')[1][:-1])
                            print('Num of param: ' + str(param_num))

                            num_value = float(next(ft).split(' ')[1][:-1])
                            print('Num value: ' + str(num_value))

                            num_min_value = float(next(ft).split(' ')[1][:-1])
                            print('Num min value: ' + str(num_min_value))

                            num_max_value = float(next(ft).split(' ')[1][:-1])
                            print('Num max value: ' + str(num_max_value))

                            num_weight = float(next(ft).split(' ')[1][:-1])
                            print('Num weight: ' + str(num_weight))

                            num_parameters.append(tuple((param_num, param_name, num_value, num_min_value, num_max_value, num_weight)))
                            print(num_parameters)

                        if param_type == 'Str':
                            param_name = next(ft).split(' ')[1][:-1]
                            print('Name of found parameter: ' + param_name)
                            
                            param_num = int(next(ft).split(' ')[1][:-1])
                            print('Num of param: ' + str(param_num))

                            str_value = next(ft).split(' ')[1][:-1]
                            print('Str value: ' + str_value)

                            str_arr_values = next(ft).split(' ')[1:]
                            str_arr_values = [word.rstrip() for word in str_arr_values]
                            str_arr_values = '\n'.join(str_arr_values)
                            print('Str arr values: ' + str(str_arr_values))

                            str_weight = float(next(ft).split(' ')[1][:-1])
                            print('Str weight: ' + str(str_weight))

                            str_parameters.append(tuple((param_num, param_name, str_value, str_arr_values, str_weight)))
                            print(str_parameters)

                        if param_type == 'StrNum':
                            param_name = next(ft).split(' ')[1][:-1]
                            print('Name of found parameter: ' + param_name)
                            
                            param_num = int(next(ft).split(' ')[1][:-1])
                            print('Num of param: ' + str(param_num))

                            strnum_feature = next(ft).split(' ')[1][:-1]
                            print('Strnum feature: ' + str(strnum_feature))

                            strnum_value = float(next(ft).split(' ')[1][:-1])
                            print('Strnum value: ' + str(strnum_value))

                            strnum_features = next(ft).split(' ')[1:]
                            strnum_features = [word.rstrip() for word in strnum_features]
                            strnum_features = '\n'.join(strnum_features)
                            print('Strnum features: ' + str(strnum_features))

                            strnum_min_values = next(ft).split(' ')[1:]
                            strnum_min_values = [word.rstrip() for word in strnum_min_values]
                            #strnum_min_values = [float(i) for i in strnum_min_values]
                            strnum_min_values = '\n'.join(strnum_min_values)
                            print('Strnum min arr values: ' + str(strnum_min_values))

                            strnum_max_values = next(ft).split(' ')[1:]
                            strnum_max_values = [word.rstrip() for word in strnum_max_values]
                            #strnum_max_values = [float(i) for i in strnum_max_values]
                            strnum_max_values = '\n'.join(strnum_max_values)
                            print('Strnum max arr values: ' + str(strnum_max_values))

                            strnum_weights = next(ft).split(' ')[1:]
                            strnum_weights = [word.rstrip() for word in strnum_weights]
                            #strnum_max_values = [float(i) for i in strnum_weights]
                            strnum_weights = '\n'.join(strnum_weights)
                            print('Strnum weights: ' + str(strnum_weights))

                            strnum_parameters.append(tuple((param_num, param_name, strnum_feature, strnum_value, strnum_features, strnum_min_values, strnum_max_values, strnum_weights)))
                            print(strnum_parameters)

                            #добавление считанных данных в таблицу
                            for bool_param in bool_parameters:
                                bool_tree.insert('', END, values=bool_param)
                            for num_param in num_parameters:
                                num_tree.insert('', END, values=num_param)
                            for str_param in str_parameters:
                                str_tree.insert('', END, values=str_param)
                            for strnum_param in strnum_parameters:
                                strnum_tree.insert('', END, values=strnum_param)

            msg = 'Data sussessfully imported from:\n' + filename
            mb.showinfo("Completed", msg)
        except:
            raise Exception

#функция сохранения параметров (как на экране)
def save_click():
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    filename = fd.asksaveasfilename(title='Save file', filetypes=filetypes)

    if filename:
        try:    
            with open(filename, 'w') as ft:
                #списки для записи в файл
                bools_to_save = []
                nums_to_save = []
                strs_to_save = []
                strnums_to_save = []
                #присвоение элементов с экрана списки
                for k in bool_tree.get_children(""): 
                    bools_to_save.append(bool_tree.item(k, option='values'))
                for k in num_tree.get_children(""): 
                    nums_to_save.append(num_tree.item(k, option='values'))
                for k in str_tree.get_children(""): 
                    strs_to_save.append(str_tree.item(k, option='values'))
                for k in strnum_tree.get_children(""): 
                    strnums_to_save.append(strnum_tree.item(k, option='values'))

                # print('bools: ' + str(bools_to_save))
                # print('nums: ' + str(nums_to_save))
                # print('strs: ' + str(strs_to_save))
                # print('strnums' + str(strnums_to_save))

                #построчная запись файлов
                for bool in bools_to_save:
                    ft.write('Type: Bool\n')
                    ft.write('Name: ' + bool[1] + '\n')
                    ft.write('Num: ' + bool[0] + '\n')
                    ft.write('Value: ' + bool[2] + '\n')
                    ft.write('Weight: ' + bool[3] + '\n')
                    ft.write('\n')

                for num in nums_to_save:
                    ft.write('Type: Num\n')
                    ft.write('Name: ' + num[1] + '\n')
                    ft.write('Num: ' + num[0] + '\n')
                    ft.write('Value: ' + num[2] + '\n')
                    ft.write('MinValue: ' + num[3] + '\n')
                    ft.write('MaxValue: ' + num[4] + '\n')
                    ft.write('Weight: ' + num[5] + '\n')
                    ft.write('\n')

                for str in strs_to_save:
                    ft.write('Type: Str\n')
                    ft.write('Name: ' + str[1] + '\n')
                    ft.write('Num: ' + str[0] + '\n')
                    ft.write('Value: ' + str[2] + '\n')
                    ft.write('ArrValues: ' + str[3].replace('\n', ' ') + '\n')
                    ft.write('Weight: ' + str[4] + '\n')
                    ft.write('\n')

                for strnum in strnums_to_save:
                    ft.write('Type: StrNum\n')
                    ft.write('Name: ' + strnum[1] + '\n')
                    ft.write('Num: ' + strnum[0] + '\n')
                    ft.write('Feature: ' + strnum[2] + '\n')
                    ft.write('Value: ' + strnum[3] + '\n')
                    ft.write('ArrValues: ' + strnum[4].replace('\n', ' ') + '\n')
                    ft.write('MinValues: ' + strnum[5].replace('\n', ' ') + '\n')
                    ft.write('MaxValues: ' + strnum[6].replace('\n', ' ') + '\n')
                    ft.write('Weights: ' + strnum[7].replace('\n', ' ') + '\n')
                    ft.write('\n')

            #сообщение об успешной записи файла
            msg = 'Data sussessfully saved to:\n' + filename
            mb.showinfo("Completed", msg)

        except:
            raise Exception

#обработка клика по кнопке ввода параметра
def enter_click():
    #метод для передачи значения булевого параметра в таблицу
    def bool_confirm_click():
        try:
            #проверка правильности ввода
            if (bool_value_entry.get() == '0' or bool_value_entry.get() == '1'):
                #собираем значения в переменные
                current_bool_tree = []
                for k in bool_tree.get_children(""): 
                    current_bool_tree.append(bool_tree.item(k, option='values'))

                new_bool_name = bool_name_entry.get()
                new_bool_value = bool(bool_value_entry.get())
                new_bool_weight = float(bool_weight_entry.get())
                new_bool_num = int(current_bool_tree[-1][0]) + 1
                new_bool = tuple([new_bool_num, new_bool_name, new_bool_value, new_bool_weight])
                #передаем значения в таблицу
                bool_tree.insert('', END, values=new_bool)

                mb.showinfo("Completed", 'New BOOL added successfully!')
            else:
                mb.showinfo("Completed", 'BOOL can only be "0" or "1"!')
        except:
            raise Exception

    #описание формы ручного ввода булевых значений
    if radio_value.get() == 1:
        print('enter new bool')
        bool_enter = Toplevel(root)
        bool_enter.geometry('200x95')
        #bool_enter.resizable(False, False)
        bool_enter.iconbitmap('favicon.ico')
        bool_enter.title("BOOL")

        bool_name_label = Label(bool_enter, text='Name:')
        bool_name_entry = Entry(bool_enter)
        bool_value_label = Label(bool_enter, text='Value:')
        bool_value_entry = Entry(bool_enter, )
        bool_weight_label = Label(bool_enter, text='Weight:')
        bool_weight_entry = Entry(bool_enter)
        bool_confirm = ttk.Button(bool_enter, text='Confirm', command=bool_confirm_click)
        #сетка
        bool_name_label.grid(row=1, column=1, sticky='e')
        bool_name_entry.grid(row=1, column=2, sticky='e')
        bool_value_label.grid(row=2, column=1, sticky='e')
        bool_value_entry.grid(row=2, column=2, sticky='e')
        bool_weight_label.grid(row=3, column=1, sticky='e')
        bool_weight_entry.grid(row=3, column=2, sticky='e')
        bool_confirm.grid(row=4, column=2)

    #метод для передачи значения числового параметра в таблицу
    def num_confirm_click():
        try:
            #собираем значения в переменные
            current_num_tree = []
            for k in num_tree.get_children(""): 
                current_num_tree.append(num_tree.item(k, option='values'))

            new_num_name = num_name_entry.get()
            new_num_min_value = float(num_min_value_entry.get())
            new_num_max_value = float(num_max_value_entry.get())
            new_num_value = float(num_value_entry.get())
            new_num_weight = float(num_weight_entry.get())
            new_num_num = int(current_num_tree[-1][0]) + 1
            new_num = tuple([new_num_num, new_num_name, new_num_min_value, new_num_max_value, new_num_value, new_num_weight])
            #передаем значения в таблицу
            num_tree.insert('', END, values=new_num)

            mb.showinfo("Completed", 'New NUM added successfully!')
        except:
            raise Exception

    #описание формы ручного ввода числовых значений
    if radio_value.get() == 2:
        print('enter new NUM')
        num_enter = Toplevel(root)
        num_enter.geometry('200x140')
        #num_enter.resizable(False, False)
        num_enter.iconbitmap('favicon.ico')
        num_enter.title("NUM")

        num_name_label = Label(num_enter, text='Name:')
        num_name_entry = Entry(num_enter)
        num_min_value_label = Label(num_enter, text='Min Value:')
        num_min_value_entry = Entry(num_enter)
        num_max_value_label = Label(num_enter, text='Max Value:')
        num_max_value_entry = Entry(num_enter)
        num_value_label = Label(num_enter, text='Value:')
        num_value_entry = Entry(num_enter, )
        num_weight_label = Label(num_enter, text='Weight:')
        num_weight_entry = Entry(num_enter)
        num_confirm = ttk.Button(num_enter, text='Confirm', command=num_confirm_click)
        #сетка
        num_name_label.grid(row=1, column=1)
        num_name_entry.grid(row=1, column=2)
        num_min_value_label.grid(row=2, column=1)
        num_min_value_entry.grid(row=2, column=2)
        num_max_value_label.grid(row=3, column=1)
        num_max_value_entry.grid(row=3, column=2)
        num_value_label.grid(row=4, column=1)
        num_value_entry.grid(row=4, column=2)
        num_weight_label.grid(row=5, column=1)
        num_weight_entry.grid(row=5, column=2)
        num_confirm.grid(row=6, column=2)

    #метод для передачи значения строкового параметра в таблицу
    def str_confirm_click():
        try:
            #собираем значения в переменные
            current_str_tree = []
            for k in str_tree.get_children(""): 
                current_str_tree.append(str_tree.item(k, option='values'))

            new_str_name = str_name_entry.get()
            new_str_value = str_value_entry.get()
            new_str_values = str_values_text.get(0.0, END)
            new_str_weight = float(str_weight_entry.get())
            new_str_num = int(current_str_tree[-1][0]) + 1
            new_str = tuple([new_str_num, new_str_name, new_str_value, new_str_values, new_str_weight])
            #передаем значения в таблицу
            str_tree.insert('', END, values=new_str)

            mb.showinfo("Completed", 'New STR added successfully!')
        except:
            raise Exception

    #описание формы ручного ввода строковых значений
    if radio_value.get() == 3:
        print('enter new str')
        str_enter = Toplevel(root)
        str_enter.geometry('470x180')
        #str_enter.resizable(False, False)
        str_enter.iconbitmap('favicon.ico')
        str_enter.title("STR")

        str_name_label = Label(str_enter, text='Name:')
        str_name_entry = Entry(str_enter, width=67)
        str_value_label = Label(str_enter, text='Value:')
        str_value_entry = Entry(str_enter, width=67)
        str_values_label = Label(str_enter, text='Values:')
        str_values_text = Text(str_enter, width=50, height=5)
        str_weight_label = Label(str_enter, text='Weight:')
        str_weight_entry = Entry(str_enter, width=67)
        str_confirm = ttk.Button(str_enter, text='Confirm', command=str_confirm_click)
        #сетка
        str_name_label.grid(row=1, column=1)
        str_name_entry.grid(row=1, column=2)
        str_value_label.grid(row=2, column=1)
        str_value_entry.grid(row=2, column=2)
        str_values_label.grid(row=3, column=1)
        str_values_text.grid(row=3, column=2)
        str_weight_label.grid(row=4, column=1)
        str_weight_entry.grid(row=4, column=2)
        str_confirm.grid(row=5, column=2)

    #метод для передачи значения строково-числового параметра в таблицу
    def strnum_confirm_click():
            try:
                new_strnum_features = strnum_features_text.get(0.0, END)
                new_strnum_min_values = strnum_min_values_text.get(0.0, END)
                new_strnum_max_values = strnum_max_values_text.get(0.0, END)
                new_strnum_weights = strnum_weights_text.get(0.0, END)
                if len(new_strnum_features.split('\n')) == len(new_strnum_min_values.split('\n')) == len(new_strnum_max_values.split('\n')) == len(new_strnum_weights.split('\n')):
                    #собираем значения в переменные
                    current_strnum_tree = []
                    for k in strnum_tree.get_children(""): 
                        current_strnum_tree.append(strnum_tree.item(k, option='values'))

                    new_strnum_name = strnum_name_entry.get()
                    new_strnum_features = strnum_features_text.get(0.0, END)
                    new_strnum_min_values = strnum_min_values_text.get(0.0, END)
                    new_strnum_max_values = strnum_max_values_text.get(0.0, END)
                    new_strnum_feature = strnum_feature_entry.get()
                    new_strnum_value = strnum_value_entry.get()
                    new_strnum_weights = strnum_weights_text.get(0.0, END)

                    new_strnum_num = int(current_strnum_tree[-1][0]) + 1
                    new_strnum = tuple([new_strnum_num, new_strnum_name, new_strnum_features, new_strnum_min_values, new_strnum_max_values, new_strnum_feature, new_strnum_value, new_strnum_weights])
                    #передаем значения в таблицу
                    strnum_tree.insert('', END, values=new_strnum)

                    mb.showinfo("Completed", 'New STRNUM added successfully!')
                else:
                    mb.showinfo("Error", 'Features, min, max values and weights must have equal shapes!')
            except:
                raise Exception

    if radio_value.get() == 4:
        print('enter new strnum')
        strnum_enter = Toplevel(root)
        strnum_enter.geometry('560x380')
        #str_enter.resizable(False, False)
        strnum_enter.iconbitmap('favicon.ico')
        strnum_enter.title("STRNUM")

        strnum_name_label = Label(strnum_enter, text='Name:')
        strnum_name_entry = Entry(strnum_enter, width=80)
        strnum_features_label = Label(strnum_enter, text='Features:')
        strnum_features_text = Text(strnum_enter, width=15, height=10)
        strnum_min_values_label = Label(strnum_enter, text='Min Values:')
        strnum_min_values_text = Text(strnum_enter, width=15, height=10)
        strnum_max_values_label = Label(strnum_enter, text='Max Values:')
        strnum_max_values_text = Text(strnum_enter, width=15, height=10)
        strnum_feature_label = Label(strnum_enter, text='Feature')
        strnum_feature_entry = Entry(strnum_enter)
        strnum_value_label = Label(strnum_enter, text='Value:')
        strnum_value_entry = Entry(strnum_enter)
        strnum_weights_label = Label(strnum_enter, text='Weights:')
        strnum_weights_text = Text(strnum_enter, width=15, height=10)
        strnum_confirm = ttk.Button(strnum_enter, text='Confirm', command=strnum_confirm_click)
        #сетка
        strnum_name_label.grid(row=1, column=1)
        strnum_name_entry.grid(row=1, column=2, columnspan=6)
        strnum_features_label.grid(row=2, column=1)
        strnum_features_text.grid(row=2, column=2)
        strnum_min_values_label.grid(row=3, column=1)
        strnum_min_values_text.grid(row=3, column=2)
        strnum_max_values_label.grid(row=3, column=3)
        strnum_max_values_text.grid(row=3, column=4)
        strnum_feature_label.grid(row=2, column=5)
        strnum_feature_entry.grid(row=2, column=6)
        strnum_value_label.grid(row=3, column=5)
        strnum_value_entry.grid(row=3, column=6)
        strnum_weights_label.grid(row=2, column=3)
        strnum_weights_text.grid(row=2, column=4)
        strnum_confirm.grid(row=6, column=6)

#функция проверка, является ли строка числом на число
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

#функция сортировки значений для таблиц
def sort(tree, col, reverse):
    # получаем все значения столбцов в виде отдельного списка
    l = [(tree.set(k, col), k) for k in tree.get_children("")]
    #print(l[0][0])
    #print('Is number: ' + str(is_number(l[0][0])))
    # сортируем список
    if(is_number(l[0][0])):
        l.sort(key=lambda tup: float(tup[0]), reverse=reverse)
    else:
        l.sort(reverse=reverse)
    # переупорядочиваем значения в отсортированном порядке
    for index,  (_, k) in enumerate(l):
        tree.move(k, "", index)
    # в следующий раз выполняем сортировку в обратном порядке
    tree.heading(col, command=lambda: sort(tree, col, not reverse))

#расчет результатов
def execute_click():
    #обнуляем предыдущее значение глобальных переменных
    global ava_sum
    global ava_mul
    ava_sum = 0.0
    ava_mul = 1.0
    #списки для записи в файл
    bools_from_table = []
    nums_from_table = []
    strs_from_table = []
    strnums_from_table = []
    #присвоение элементов с экрана списки
    for k in bool_tree.get_children(""): 
        bools_from_table.append(bool_tree.item(k, option='values'))
    for k in num_tree.get_children(""): 
        nums_from_table.append(num_tree.item(k, option='values'))
    for k in str_tree.get_children(""): 
        strs_from_table.append(str_tree.item(k, option='values'))
    for k in strnum_tree.get_children(""): 
        strnums_from_table.append(strnum_tree.item(k, option='values'))
    #расчеты для каждого типа параметров
    for booly in bools_from_table:
        if booly[2] == '1':
            bool_compnt = float(booly[3])
            count_target_func(bool_compnt)

    for numy in nums_from_table:
        if float(numy[4])<float(numy[2]) or float(numy[4])>float(numy[3]):
            num_compnt = float(numy[5])
            count_target_func(num_compnt)

    for stry in strs_from_table:
        str_check = stry[3].split('\n')
        for chk in str_check:
            if stry[2] == chk:
                str_compnt = float(stry[4])
                count_target_func(str_compnt)

    for strnumy in strnums_from_table:
        features_check = strnumy[2].split('\n')
        min_values_check = strnumy[3].split('\n')
        max_values_check = strnumy[4].split('\n')
        weights_check = strnumy[7].split('\n')
        for i, chk in enumerate(features_check):
            if chk == strnumy[5]:
                if strnumy[6]<min_values_check[i]  or strnumy[6]>max_values_check[i]:
                    strnum_compnt = float(weights_check[i])
                    count_target_func(strnum_compnt)

    time = datetime.now()
    results = 'Count in ' + str(time) + '\n' + 'Avalanche risk sum: ' + str(round(ava_sum, 4)) + '\n' + 'Avalanche risk multiply: ' + str(round(ava_mul, 4)) + '\n\n'
    result_text.insert(END, results)

#для расчета целевой функции
def count_target_func(component):
    global ava_sum
    global ava_mul
    if schemes_combobox.get() == 'Sum':
        ava_sum = ava_sum + component
    if schemes_combobox.get() == 'Multiply':
        ava_mul = ava_mul*component

#описание корневого объекта
root = Tk()
root.iconbitmap('favicon.ico')
root.title("Expert system")
root.geometry('1150x855')
root.resizable(False, False)

#создание Canvas для прокрутки интерфейса, в случае, если он не влезает
form = Canvas()
Canvas.grid(form, row=1, column=1, sticky='nswe')
main_scroll = ttk.Scrollbar(form, orient = 'vertical', command = form.yview)
main_scroll.grid(row=1, column=3, rowspan=4, sticky='ns')

#инициализация элементов
#блок открытия файла
open_file_frame = ttk.Frame(form, borderwidth=1, relief=SOLID, padding=[8, 10])
path_label = ttk.Label(open_file_frame, text = 'Path to param file:')
path_line = Text(open_file_frame,height=4, width=32)
path_line.insert("0.0", 'Click "Open file" button.')
start_button = ttk.Button(open_file_frame, text = 'Open file', width=42, command=open_file_click)
#блок ввода параметров
enter_param_frame = ttk.Frame(form, borderwidth=1, relief=SOLID, padding=[8, 10])
type_label = Label(enter_param_frame, text = 'Choose type of param:')
radio_value = IntVar()
radio_value.set(1)
bool_radio_btn = ttk.Radiobutton(enter_param_frame, text='BOOL', variable=radio_value, value=1)
num_radio_btn = ttk.Radiobutton(enter_param_frame, text = 'NUM', variable=radio_value, value=2)
str_radio_btn = ttk.Radiobutton(enter_param_frame, text = 'STR', variable=radio_value, value=3)
strnum_radio_btn = ttk.Radiobutton(enter_param_frame, text = 'STRNUM', variable=radio_value, value=4)
enter_button = ttk.Button(enter_param_frame, text = 'Enter new param', width=42, command=enter_click)
#блок выбора схемы расчета целевой функции
schemes_frame = ttk.Frame(form, borderwidth=1, relief=SOLID, padding=[8, 10])
schemes_label = ttk.Label(schemes_frame, text = 'Count schemes:')
schemes = ['Sum', 'Multiply']
schemes_var = StringVar(value=schemes[0])
schemes_combobox = ttk.Combobox(schemes_frame, textvariable=schemes_var, values=schemes, width=38)
execute_btn = ttk.Button(schemes_frame, text = 'Execute', width=18, command=execute_click)
save_btn = ttk.Button(schemes_frame, text = 'Save', command=save_click, width=18)
result_label = ttk.Label(schemes_frame, text = 'Results:')
result_text = Text(schemes_frame, height=5, width=30)
result_text_scrollbar = Scrollbar(schemes_frame, orient = 'vertical', command = result_text.yview)

#описание сетки
#блок открытия файла
open_file_frame.grid(row = 2, column = 1, padx=2, pady=2, sticky='nswe')
path_label.grid(row = 1, column = 1, sticky='w')
path_line.grid(row = 2, column = 1, columnspan = 2)
start_button.grid(row = 3, column = 1, padx=2, pady=2)
#блок ввода параметров
enter_param_frame.grid(row = 3, column = 1, padx=2, pady=2, sticky='nswe')
type_label.grid(row = 1, column = 1, sticky='nw')
bool_radio_btn.grid(row = 2, column = 1, sticky='nw')
num_radio_btn.grid(row = 3, column = 1, sticky='nw')
str_radio_btn.grid(row = 4, column = 1, sticky='nw')
strnum_radio_btn.grid(row = 5, column = 1, sticky='nw')
enter_button.grid(row = 6, column = 1, sticky='n')
#блок выбора схемы расчета целевой функции
schemes_frame.grid(row = 4, column = 1,padx=2, pady=2, sticky='nswe')
schemes_label.grid(row = 1, column = 1, sticky='w')
schemes_combobox.grid(row = 2, column = 1, columnspan = 4)
execute_btn.grid(row = 3, column = 1, columnspan=2, padx=2, pady=2, sticky='w')
save_btn.grid(row = 3, column = 3, columnspan=2, padx=2, pady=2)
result_label.grid(row = 4, column = 1, sticky='w')
result_text.grid(row = 5, column =1, columnspan=3)
result_text_scrollbar.grid(row = 5, column = 4, sticky='nsw')

#блок изображения
image_frame = ttk.Frame(form, borderwidth=1, relief=SOLID)
image = Canvas(image_frame, height = 70, width=1115)
image.grid(row = 1, column = 1, columnspan = 2, padx=2, pady=2, sticky='w')
python_image = PhotoImage(file='mountains.png')
image.create_image(1, 1, anchor=NW, image=python_image)
image_frame.grid(row=1, column=1, columnspan=2, padx=2, pady=2, sticky='we')

#ТАБЛИЦЫ
table_frame = ttk.Frame(form, borderwidth=1, relief=SOLID, padding=[8, 10])
table_frame.grid(row = 2, column = 2, rowspan = 3, padx=2, pady=2)

#блок таблицы БУЛЕВЫХ параметров
bool_table_label = Label(table_frame, text = 'BOOL parameters:')
#расположение таблицы булевых параметров
bool_table_label.grid(row = 1, column = 1)
# определяем данные для отображения
bool_parameters_default = [(1, 'Param1', True, 0.01),
(2, 'Param2', False, 0.01),
(3, 'Param3', True, 0.03),
(4, 'Param4', True, 0.07),
(5, 'Param5', False, 0.05),
(6, 'Param6', False, 0.02),
(7, 'Param7', True, 0.01)]
# определяем столбцы
bool_columns = ('No', 'Name', 'Value', 'Weight')
bool_num_of_columns = 4
bool_tree = ttk.Treeview(table_frame, columns=bool_columns, show='headings', height = 4, selectmode="extended")
bool_tree.grid(row = 2, column = 1)
#вертикальная прокрутка
bool_y_scroll = Scrollbar(table_frame, orient = 'vertical', command = bool_tree.yview)
bool_tree.configure(yscroll=bool_y_scroll.set)
bool_y_scroll.grid(row=2, column=3, sticky='ns')
#горизонтальная прокрутка
bool_x_scroll = Scrollbar(table_frame, orient = 'horizontal', command = bool_tree.xview)
bool_tree.configure(xscroll=bool_x_scroll.set)
bool_x_scroll.grid(row = 3, column = 1, sticky = 'we')
# определяем заголовки
bool_tree.heading('No', text='No', command=lambda: sort(bool_tree, 0, False))
bool_tree.heading('Name', text='Name', command=lambda: sort(bool_tree, 1, False))
bool_tree.heading('Value', text='Value', command=lambda: sort(bool_tree, 2, False))
bool_tree.heading('Weight', text='Weight', command=lambda: sort(bool_tree, 3, False))
# настраиваем столбцы
bool_tree.column("No", width=40)
bool_tree.column("Name", width=120)
bool_tree.column("Value", width=column_width(bool_num_of_columns))
bool_tree.column("Weight", width=column_width(bool_num_of_columns))
# добавляем данные
for bool_param in bool_parameters_default:
    bool_tree.insert('', END, values=bool_param)

#блок таблицы ЧИСЛОВЫХ параметров
num_table_label = Label(table_frame, text = 'NUM parameters:')
#расположение таблицы числовых параметров
num_table_label.grid(row = 4, column = 1)
# определяем данные для отображения
num_parameters_default = [(1, 'Param1', 10, 20, 15, 0.01),
(2, 'Param2', 10, 20, 15, 0.01),
(3, 'Param3', 40, 80, 55, 0.01),
(4, 'Param4', 10, 30, 17, 0.01),
(5, 'Param5', 10, 40, 15, 0.01),
(6, 'Param6', 27, 20, 43, 0.01),
(7, 'Param7', 10, 80, 18, 0.01),
(8, 'Param8', 45, 67, 25, 0.01),
(9, 'Param9', 10, 20, 37, 0.01),
(10, 'Param10', 10, 20, 15, 0.01)]
# определяем столбцы
num_columns = ('No', 'Name', 'Min value', 'Max value', 'Value', 'Weight')
num_num_of_columns = 6
num_tree = ttk.Treeview(table_frame, columns=num_columns, show='headings', height = 4, selectmode="extended")
num_tree.grid(row = 5, column = 1)
#вертикальная прокрутка
num_y_scroll = Scrollbar(table_frame, orient = 'vertical', command = num_tree.yview)
num_tree.configure(yscroll=num_y_scroll.set)
num_y_scroll.grid(row=5, column=3, sticky='ns')
#горизонтальная прокрутка
num_x_scroll = Scrollbar(table_frame, orient = 'horizontal', command = num_tree.xview)
num_tree.configure(xscroll=num_x_scroll.set)
num_x_scroll.grid(row = 6, column = 1, sticky = 'we')
# определяем заголовки
num_tree.heading('No', text='No', command=lambda: sort(num_tree, 0, False))
num_tree.heading('Name', text='Name', command=lambda: sort(num_tree, 1, False))
num_tree.heading('Min value', text = 'Min value', command=lambda: sort(num_tree, 2, False))
num_tree.heading('Max value', text = 'Max value', command=lambda: sort(num_tree, 3, False))
num_tree.heading('Value', text='Value', command=lambda: sort(num_tree, 4, False))
num_tree.heading('Weight', text='Weight', command=lambda: sort(num_tree, 5, False))
# настраиваем столбцы
num_tree.column("No", width=40)
num_tree.column("Name", width=120)
num_tree.column("Min value", width=column_width(num_num_of_columns))
num_tree.column("Max value", width=column_width(num_num_of_columns))
num_tree.column("Value", width=column_width(num_num_of_columns))
num_tree.column("Weight", width=column_width(num_num_of_columns))
# добавляем данные
for num_param in num_parameters_default:
    num_tree.insert('', END, values=num_param)

#блок таблицы СТРОКОВЫХ параметров
str_table_label = Label(table_frame, text = 'STR parameters:')
#стиль
str_table_style = ttk.Style()
str_table_style.configure('W.Treeview', rowheight = '60')
#расположение таблицы строковых параметров
str_table_label.grid(row = 7, column = 1)
# определяем данные для отображения
str_parameters_default = [(1, 'Param1', 'grass', 'grass\nrock\ncobblestone\ndirt', 0.01),
(2, 'Param2', 'dirt', 'sand\ndirt', 0.07),
(3, 'Param3', 'gravel', 'silicon\ngravel', 0.11),
(3, 'Param4', 'gravel', 'silicon\ngravel', 0.11)]
# определяем столбцы
str_columns = ('No', 'Name', 'Value', 'Values', 'Weight')
str_num_of_columns = 5
str_tree = ttk.Treeview(table_frame, columns=str_columns, show='headings', height = 3, selectmode="extended", style='W.Treeview')
str_tree.grid(row = 8, column = 1)
#вертикальная прокрутка
str_y_scroll = Scrollbar(table_frame, orient = 'vertical', command = str_tree.yview)
str_tree.configure(yscroll=str_y_scroll.set)
str_y_scroll.grid(row=8, column=3, sticky='ns')
#горизонтальная прокрутка
str_x_scroll = Scrollbar(table_frame, orient = 'horizontal', command = str_tree.xview)
str_tree.configure(xscroll=str_x_scroll.set)
str_x_scroll.grid(row = 9, column = 1, sticky = 'we')
# определяем заголовки
str_tree.heading('No', text='No', command=lambda: sort(str_tree, 0, False))
str_tree.heading('Name', text='Name', command=lambda: sort(str_tree, 1, False))
str_tree.heading('Value', text='Value', command=lambda: sort(str_tree, 2, False))
str_tree.heading('Values', text='Values', command=lambda: sort(str_tree, 3, False))
str_tree.heading('Weight', text='Weight', command=lambda: sort(str_tree, 4, False))
# настраиваем столбцы
str_tree.column("No", width=40)
str_tree.column("Name", width=120)
str_tree.column("Value", width=column_width(str_num_of_columns))
str_tree.column("Values", width=column_width(str_num_of_columns))
str_tree.column("Weight", width=column_width(str_num_of_columns))
# добавляем данные
for str_param in str_parameters_default:
    str_tree.insert('', END, values=str_param)

#блок таблицы СТРОКОВО-ЧИСЛОВЫХ параметров
strnum_table_label = Label(table_frame, text = 'STRNUM parameters:')
#стиль
strnum_table_style = ttk.Style()
strnum_table_style.configure('My.Treeview', rowheight = '30')
#расположение таблицы строково-числовых параметров
strnum_table_label.grid(row = 10, column = 1)
# определяем данные для отображения
strnum_parameters_default = [(1, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 10, '0.01\n0.02'),
(2, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 20, '0.01\n0.02'),
(3, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 30, '0.01\n0.02'),
(4, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 40, '0.01\n0.02'),
(5, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 60, '0.01\n0.02'),
(6, 'Param1', 'surface\ncover', '15\n10', '30\n40', 'surface', 50, '0.01\n0.02')]
# определяем столбцы
strnum_columns = ('No', 'Name', 'Features', 'Min values', 'Max values', 'Feature', 'Value', 'Weights')
strnum_num_of_columns = 8
strnum_tree = ttk.Treeview(table_frame, columns=strnum_columns, show='headings', height = 5, selectmode="extended", style='My.Treeview')
strnum_tree.grid(row = 11, column = 1)
#вертикальная прокрутка
strnum_y_scroll = Scrollbar(table_frame, orient = 'vertical', command = strnum_tree.yview)
strnum_tree.configure(yscroll=strnum_y_scroll.set)
strnum_y_scroll.grid(row=11, column=3, sticky='ns')
#горизонтальная прокрутка
strnum_x_scroll = Scrollbar(table_frame, orient = 'horizontal', command = strnum_tree.xview)
strnum_tree.configure(xscroll=strnum_x_scroll.set)
strnum_x_scroll.grid(row = 12, column = 1, sticky = 'we')
# определяем заголовки
strnum_tree.heading('No', text='No', command=lambda: sort(strnum_tree, 0, False))
strnum_tree.heading('Name', text='Name', command=lambda: sort(strnum_tree, 1, False))
strnum_tree.heading('Features', text='Features', command=lambda: sort(strnum_tree, 2, False))
strnum_tree.heading('Min values', text = 'Min values', command=lambda: sort(strnum_tree, 3, False))
strnum_tree.heading('Max values', text = 'Max values', command=lambda: sort(strnum_tree, 4, False))
strnum_tree.heading('Feature', text='Feature', command=lambda: sort(strnum_tree, 5, False))
strnum_tree.heading('Value', text='Value', command=lambda: sort(strnum_tree, 6, False))
strnum_tree.heading('Weights', text='Weights', command=lambda: sort(strnum_tree, 7, False))
# настраиваем столбцы
strnum_tree.column("No", width=40)
strnum_tree.column("Name", width=120)
strnum_tree.column("Features", width=column_width(strnum_num_of_columns))
strnum_tree.column("Min values", width=column_width(strnum_num_of_columns))
strnum_tree.column("Max values", width=column_width(strnum_num_of_columns))
strnum_tree.column("Feature", width=column_width(strnum_num_of_columns))
strnum_tree.column("Value", width=column_width(strnum_num_of_columns))
strnum_tree.column("Weights", width=column_width(strnum_num_of_columns))
# добавляем данные
for strnum_param in strnum_parameters_default:
    strnum_tree.insert('', END, values=strnum_param)

root.eval('tk::PlaceWindow . center')
#запуск главного цикла
root.mainloop()