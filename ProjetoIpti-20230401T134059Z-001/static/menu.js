const menu = document.querySelector('#menu')
const menuToggle = document.querySelector('.navbar')

menu.addEventListener('click', () => {
   
    menu.classList.toggle('fa-times');
    menuToggle.classList.toggle('nav-toggle');
    
});
