var number = ['A','2','3','4','5','6','7','8','9','10','J','K','Q'];
var suits = ['Spades','Diamond','Clubs','Hearts'];
const cards = [];


number.forEach((num) =>{
    suits.forEach((suit) =>
    cards.push({number: num, suit: suit})
    )
});


console.log(cards.length);