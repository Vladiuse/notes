// подключить Jquery

$(Jquery);
$();

// сделать так чтобы наш код выполнялся только почле загрузки файла библиотлеки
$(document).ready(function () {
  // наш код
});

$(function () {
  // наш код
});

$("main li:even");
$("main li:odd"); /* Выбрать четный\нечетный элементы списка */

$("img:not(.logo img)"); /* выбрать все картинки, кроме одной */

$("li:has(a)"); /* выбрать все теги ли - который внутри имеет тэг а */

$("p:contains(word)"); /* выбрать все теги p в который есть слово word */

$("li:first");
$("li:last"); /* выбор первого и последнего элемента */

$("div:hidden");
$("div:visibility"); /* Выбор видимых\невидимых блоков */

// изменить текст в p
var tagP = $(".main p").text("new text");

tagP.show(1500); // показать блок
tagP.hide(1500); // скрыть блок (время показа)
tagP.hide(1500, function () {
  "тело функции";
}); // выполниться сразу после счетчика
tagP.hide(1500).show(1500); // можно вызывать по несколько функций подрят - быстрее js работает

$("nav").html(); // доступ к коду блока - в скобки можно вставить чем заменить
// пример
function change() {
  var show = $(".to-show").html();
  var to_change = $("nav").html(show);
}


// визуальные эффекты

$('.some_class').fadeOut(time); // плавное исчезновение блока
$('.some_class').fadeIn(time); // плавное появление
$('.some_class').fadeTo(1500, 0.5) // сокрытие до определенного opasity
$('.some_class').slideUp(time) // сворачивоние элемента
$('.some_class').slideDown(time) // развернуть элемента


$('#some_id').attr('attr_name') // получить указаный аттрибут
$('#some_id').attr('attr_name', 'new_attr') // установить новый аттрибут
$('#some_id').removeAttr('attr_name') // удалить указанный атрибут

$('.class_name').addClass('class_name') // добавить новый класс
$('class_name').removeClass('class_name') // удалить указанный класс
$('div li').css('matgin-top') // доступ к css свойствам
$('div li').css('matgin-top', '10px') // установить css свойства
$('div li').css({
  'color': 'black',
   'font-size': '10px'
  }) // либо передать туда обьект с множеством свойств
  .animate({}, time, func()) // вместо css делает изменение стилей анимироваными (только на числовые параметры)
  // 3м параметром можно указать функцию, которая выполнеться по исходу time


elem.after('<p>some text</p>') // добавить новый элемент после указаного
elem.insertAfter(to) // вставить elem в to
elem.before('<p>some text</p>') // добавить новый элемент ПЕРЕд указаного
elem.append('<img src="2.gif" alt="">') // вставить как в список
elem.prepend('<img src="2.gif" alt="">') // вставить как в список в НАЧАЛО

elem.each(function(){
  if($(this).attr('class') == 'some_class_name')
   {$(this).fadeOut}  // each позволяет пройтись по элементам, this - значит текущий
})

$('div, p').length // подсчет количества выбранных элементов

elem.clone() // скопировать элемент
elem.remove() // удаляет обьект и клонирует его как clone()
list.empty() // очищает содержимое елементов

$('img[alt]').css('width', '50px') // применить только к тем у кого задан указаный аттрибут


// СОБЫТИЯ

elem.mouseover(function(){some_code}) // выполнение функции при наведении на элемент
ele.mouseout(function(){some_code}) // когда мышку убираем
elem.mousemove() // при движении мышы по элементу
elem.mouseup() // нажали - но не отпустили

elem.hove(func_1, func_2) // Наведение/ убрали

$(window).scroll(func) // действие при скроле


// Переча параметра в йункцию при elem.click()
elem.click(function(e){
  console.log(e.screenX) // получить координаты по оси X
})
e.pageX // получить координаты страницы
e.screenX // координаты от элемента
e.altKey // true если клинкули с нажатым альт
e.target // элемент, инициировавший событие
e.timestamp // время наступления события


e.preventDefault() // сброс стандартного поведения элементов
e.isDefaultPrevented() // возвращает true, если для данного события уже ранее вызывался метод preventDefault

e.stopPropagation() // запрет всплытия ввер по иерархии DOM
e.isPropagationStopped() // проверить на метод выше

var answer = confirm('Some text');
       if (!answer){
           e.preventDefault()
       } // вызов окна с вопросом - если нет, то ничего не происходит

elem.slideToggle(TIME) // сворачивает и разворачивает элемент

list.size() // размер выборки
list.eq() // доступ по индексу + -1
list.index(elem) // получиь индекс элемента

// ФИЛЬТРЫ 

list.filter()  // Метод filter(условие) принимает в качестве параметра условие фильтрации
list.is()   //  Метод is (условие) определяет, имеются ли в данной выборке объекты, соответствующие условию.
list.not()   //  Противоположным по действию по сравнению с методом filter является метод not.
list.has()   // Метод has(вложенный элемент) проверяет объект на наличие вложенного элемента.
list.slice()   // Метод slice(begin, end) исключает из выборки те элементы, которые не попадают в диапазон, задаваемый параметрами begin и end.

// ВЫБОРКА 
elem.children() // получить дочерние элементы
elem.parent() // получить родителя 
elem.parents().parentsUntil() // получить всех родителей
elem.siblings() // получение элементов на том же уровне

// ВЫБОРКА И РАБОТА С НЕЙ
elem.closest(selector) // получить ближайшего родителя по условию(селектору)
elem.next() // получит следующий элемент на том-же уровне
elem.nexAll(selector) // все элементы после - селектор может сузить выборку
elen.nextUntil() // все до!
elem.prev().prevAll().prevUntil() // в другую сторону


elem.wrap('<div></div>') // обернуть в казаный элемент
elem.wapInner(html) // обернуть содержимое
elem.replaceWith(html) // заменить один элемент на другой
list.replaceAll(html) // заменить все элементы в выбоке

// ОБРАБОТКА СОБЫТИЙ
elem.bind(event, function(){}) // обработчик событий / применим только к существующим элементам! 
// за-append элементы обрабатываться не будут
elem.unbind() // отмена отслеживания событий
elem.one() // разовая обработка события
elem.delegate('button', event, func) // bind для будущих элементов
elem.undelegate() // отмена свойства
elem.on() // аналог делегейта
elem.off('button', 'click') // отмена
EVENTS = ['click', 'change', 'keydown', 'keyapp']

elem.trigger('mouseenter') // вызов тригера эемента (elem.click(f( trigger)))
