let toogleSpeed = 150;
let SITE = 'http://127.0.0.1:8000/'
let mainActive = null;
let subSpiner = $('#spin')
let subBlock = $('#sub-buttons')


// добавление данных
$('.plus').on('click', function(){
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
    
    URL = SITE + 'copy_paste';
    $.ajax({
        url: URL,
        method: 'GET'
    }).done(function(data){
        let butons = data['buttons']
        $('#main-buttons .spinner-border').remove()
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
    if ($(this).hasClass('btn-primary')){
        $(this).removeClass('btn-primary')
        $(this).addClass('btn-outline-primary')
    }
    else{
        $(this).addClass('btn-primary')
        $(this).removeClass('btn-outline-primary')
    }
    mainActive = $(this).attr('id');
    let groupId = $(this).attr('id');
    loadSubButton(groupId)
    $('#text-data textarea').text('')
})

// load sub-buttons
function loadSubButton(groupId){
    $('#sub-buttons').empty()
    let spin = subSpiner.clone()
    subBlock.append(spin)
    spin.show();
    URL  = SITE + 'copy_paste/code_examples_data?group_id='
    $.ajax({
        url: URL + groupId,
        method: 'GET'
        }).done(function(data){
        subButtonsData = data['buttons']
        // console.log(subButtonsData, 'суб-кнопки')
        addSubs(subButtonsData)
        spin.remove();
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

$('.add-main .add').click(function(){
    createButton();
})
// Создать новую кнопку
function createButton(name){
    URL = SITE + 'copy_paste/add_group';
    let newBtnName = $('#main input').val()
    console.log(newBtnName)
    data = {'group_name': newBtnName}
    let res = $.post(URL, data, function(data){
        console.log(data)
    })
    // $.ajax({
    //     url: URL,
    //     type: 'post',
    //     data: {1: 1, 2: 2}
    // }).done(function(response){
    //     console.log(response)
    // })
}


$('.add-sub .add').click(function(){
    createSubButton();
})

// создать субКнопку
function createSubButton(){
    URL = SITE + 'copy_paste/add_sub_button';
    console.log(mainActive);
    let groupID = mainActive;
    let subBtnName = $('.add-sub .sub-name').val();
    let value = $('.add-sub .sub-value').val();
    data = {
        'group_id': groupID,
        'name': subBtnName,
        'data': value,
    }
    let res = $.post(URL, data, function(data){
        console.log(data)
    })
}



$('#test').click(function(){
    console.log(123)
    $('#text').css('background-color', 'green')
    $('#text').css('align-items', 'flex-end')
})