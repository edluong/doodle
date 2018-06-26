
const MAX = 100;


//can reuse this function for both the user and computer
function getRandomInt(maxNum){
    return Math.floor(Math.random() * Math.floor(maxNum));
}

//gets the score of the user and the computer in an object
function randomResults(){
    return {userNum: getRandomInt(MAX), ComputerNum: getRandomInt(MAX)}
 }

 function showResults(){
    document.getElementById("test").innerHTML = randomResults().userNum;
 }

