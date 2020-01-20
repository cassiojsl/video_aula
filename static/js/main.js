// window.onscroll = scroll;

// function scroll() {
//   var scrollTop = window.pageYOffset;
//   if (scrollTop > 30) {
//     try {
//       document.getElementById('antes').id = 'depois'
//     } catch (e) { 
//       false 
//     }
//   } else {
//     try {
//       document.getElementById('depois').id = 'antes'
//     } catch (e) { 
//       false
//     }
//   }
// }

window.onload = function() {
    let doc = window.innerHeight;
    let win = screen.height;
    let footer = document.querySelector('.page-footer');
    if (doc < win) {
        footer.classList.remove("fixed-bottom");
    } else if (doc == win) {
        footer.classList("fixed-bottom");
    }
};