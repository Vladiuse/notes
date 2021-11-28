// Подставка моб кода и цены(старой и новой)
var country = null
    
fetch('https://extreme-ip-lookup.com/json/')
.then( res => res.json())
.then(response => {
country = response.countryCode
console.log(response.countryCode + ' - код страны');
addPhoneCode(response.countryCode);
addPrice(response.countryCode);
addCountryCodeInput(response.countryCode);
})
.catch((data, status) => {
 console.log('Request failed');
})

// Если не работает первый варик

// $.getJSON("http://www.geoplugin.net/json.gp?jsoncallback=?",
// function (data) {
//     console.log(data.geoplugin_countryCode)
//     country = data.geoplugin_countryCode
//     addPhoneCode(country);
//     addPrice(country);
//     addCountryCodeInput(country);
    
//     }
// );
 
var geoPhones = {
 'PL': '+48',
 'EE': '+372',
 'LT': '+370',
 'LV': '+371',
 'BY': '+375',
 'RU': '+7',
}
var geoPrices = {
 'PL': {'ccurrency': 'ZT', 'pprice': '130', 'pprice_old': '320', },
 'EE': {'ccurrency': 'EURO', 'pprice': '29', 'pprice_old': '69', },
 'LT': {'ccurrency': 'EURO', 'pprice': '29', 'pprice_old': '69', },
 'LV': {'ccurrency': 'EURO', 'pprice': '29', 'pprice_old': '69', },
 'BY': {'ccurrency': 'BYN', 'pprice': '29', 'pprice_old': '69', },
 'RU': {'ccurrency': 'RUB', 'pprice': '29', 'pprice_old': '69', },
}
function addPhoneCode(geo){
    // Подставка кода мобильного в значение placeholder
    var phoneInput = $('input[name=phone]')
    // phoneInput.val(geoPhones[geo])
    phoneInput.attr('placeholder', geoPhones[geo])
    // console.log(phoneInput.val(), 'значение phone input')
}

function addPrice(geo){
    var priceBlock = $('.pprice');
    var priceOldBlock = $('.pprice_old');
    var currencyBlock = $('.ccurrency');
    var price = geoPrices[geo]['pprice']
    var priceOld = geoPrices[geo]['pprice_old']
    var currency = geoPrices[geo]['ccurrency']
    priceBlock.text(price)
    priceOldBlock.text(priceOld)
    currencyBlock.text(currency)
}

function addCountryCodeInput(geo){
    var allFroms = $('form')
    var newInput = $('<input type="hidden">')
    newInput.attr('name', 'country');
    newInput.val(geo.toLowerCase());
    allFroms.append(newInput)
    
}