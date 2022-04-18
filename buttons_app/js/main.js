let toogleSpeed = 150;

// добавление данных
$('.add').on('click', function(){
    let area = $(this).attr('area')
    openForm(area)
    if ($(this).hasClass('active') == true){
        $(this).removeClass('active')
        $(this).removeClass('btn-danger')
        $(this).addClass('btn-light')
        $(this).text('+')
    }
    else{
        $(this).addClass('active')
        $(this).removeClass('btn-light')
        $(this).addClass('btn-danger')
        $(this).text('x')
    }
})

// открыть-закрыть форму
function openForm(name){
    let elem  = $('#' + name)
    if (elem.hasClass('active') == true){
        elem.slideUp(toogleSpeed)
        elem.removeClass('active')
        elem.children().val('')
    }
    else {
        elem.slideDown(toogleSpeed)
        elem.addClass('active')
    }
    
}

// load main-buttons
function loadMainButton(){
    URL = 'https://handy-fun.com/copy_paste';
    $.ajax({
        url: URL,
        method: 'GET'
    }).done(function(data){
        let butons = data['buttons']
        for (buttonID in butons){
            buttonData = butons[buttonID]
            let button = $('<button class="btn btn-primary main-bnt" id=""></button>')
            button.attr('id', buttonData['id'])
            button.text(buttonData['name'])
            $('#main-buttons').append(button)
        }
        
    })
}
loadMainButton()


// при нажатие на кнопку закрузить под-кнопки
$('#main-buttons').on('click', 'button', function(){
    let groupId = $(this).attr('id');
    loadSubButton(groupId)
    $('#text-data textarea').text('')
})

// load sub-buttons
function loadSubButton(groupId){
    $('#sub-buttons').empty()
    URL  = 'https://handy-fun.com/copy_paste/code_examples_data?group_id='
    $.ajax({
        url: URL + groupId,
        method: 'GET'
        }).done(function(data){
        subButtonsData = data['buttons']
        // console.log(subButtonsData, 'суб-кнопки')
        addSubs(subButtonsData)
    })
}

// отрисовать суб-кнопки
function addSubs(data){
    
    for (id in data){
        let name = data[id]['name']
        let value = data[id]['value']
        newSubButton = $('<button class="btn btn-primary sub-bnt" value=""></button>')
        newSubButton.val(value)
        newSubButton.text(name)
        $('#sub-buttons').append(newSubButton)
    }
}

// при клике на субкнопку
$('#sub-buttons').on('click', 'button', function(){
    let subButtonText = $(this).attr('value');
    $('#text-data textarea').text(subButtonText)
})