$(document).ready(function () {
    $("#filterForm").css("background-color","red")
    $("#filter").click(function () {
  console.log("HOLA")
  $(this).hide();
    })
  
  
  
  });
  
//BOOKSHELF

let bookshelf = document.getElementById("bookshelf");
let body = document.getElementById("body");
let currentWidthShelf = bookshelf.offsetWidth;
let currentWidthBody = body.offsetWidth;
console.log(currentWidthShelf)
console.log(currentWidthBody)
//    if (currentWidth < currentWidthBody) {
//    bookshelf.style.backgroundColor = "red";
//    console.log(body.offsetWidth)
//}




  