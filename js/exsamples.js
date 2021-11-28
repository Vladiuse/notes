// Подстановка дат
function setDate() {
    let bySelector = ".by"
    let toSelector = ".to"
    let daysBack = -5;  // начальная дата(отсегодня)
    let daysTo = 0; // конечная дата(от сегодня)
    let monthA = ["Января", "Февраля", "Марта", "Апреля", "Мая", "Июня", "Июля",
        "Августа", "Сентября", "Октября", "Ноября", "Декабря"];

    let d = new Date();
    let p = new Date(d.getTime() + daysBack * 86400000);
    $(bySelector).html(p.getDate() + " ");
    p = new Date(d.getTime());
    $(toSelector).html(p.getDate() + daysTo + " " + monthA[p.getMonth()] + " ");
};
setDate();