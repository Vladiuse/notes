// Итогавая ссылка будет https://handy-fun.com/ + URL

// получить названия кнопок
URL = copy_paste 
method: GET


// получить субкнопки и данные
URL = copy_paste/code_examples_data 
method: GET
data = {
    'group_id': id,
}

// добавить группу
URL = copy_paste/add_group 
method: POST
data = {
    'group_name': id,
}

// удалить группу
URL = copy_paste/remove_group 
method: POST
data = {
    'group_id': id,
}

// добавить субкнопку
URL = copy_paste/add_sub_button 
method: POST
data = {
    'group_id': id,
    'name': name,
    'data': data,
}

// удалить субкнопку
URL = copy_paste/remove_sub_button 
method: POST
data = {
    'sub_button_id': id,
}

// Все ответы в JSON