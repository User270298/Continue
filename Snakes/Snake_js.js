const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");
let score = 0;
let box = 50;
let napravlenie;


const ground = new Image();
ground.src = "37716068933bae2f9b11ff90bc91b015.jpg";

const food = new Image();
food.src = "photo_2023-12-26_22-15-58.png"

let foodCoodr = {
    x: getFoodCord(12),
    y: getFoodCord(10)
}
let snakeCord = {
    x: 5,
    y: 5
}

function game(){
    ctx.drawImage(ground, 0, 0);
    ctx.drawImage(food, foodCoodr.x*box, foodCoodr.y*box);

    ctx.fillStyle = 'red'
    ctx.fillRect(snakeCord.x*box, snakeCord.y*box, box, box)

    if (foodCoodr.x === snakeCord.x && foodCoodr.y === snakeCord.y ){
        score++;
        foodCoodr.x = getFoodCord(12);
        foodCoodr.y = getFoodCord(10);
    }

    // if (score == 1){
    //     clearInterval(gameInterval)
    // }

    ctx.fillStyle = 'white'
    ctx.font = "50px Arial";
    ctx.fillText(score, 10, 45)

    if (napravlenie == 37){
        // left
        snakeCord.x--;
    } else if (napravlenie == 39){
        //right
        snakeCord.x++;
    } else if (napravlenie == 38){
        // up
        snakeCord.y--;
    }
    else if (napravlenie == 40){
        // down
        snakeCord.y++;
    }
}

let gameInterval = setInterval(game, 300)

function getFoodCord(num) {
   return Math.floor(Math.random() * num + 1);
}

document.body.addEventListener("keydown", () =>{
    napravlenie = event.keyCode;
});