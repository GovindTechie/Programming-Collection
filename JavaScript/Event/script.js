let btn1 = document.querySelector("#btn1");

// btn1.onclick = () => {
//     console.log("btn1 was clicked");
//     let a = 25;
//     a++;
//     console.log(a);
// };


btn1.addEventListener("click", (evt) => {
    console.log("button was clicked");
    console.log(evt);
    console.log(evt.type);
});

let box = document.querySelector("div");
box.onmouseover = () => {
    console.log("you are inside div");
};

let btn2 = document.querySelector("#btn2");

btn2.onmouseover = (evt) => {
    console.log(evt);
    console.log(evt.type);
};