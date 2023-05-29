const modal = document.querySelector('#login')
const modalToggle = document.querySelector('.login-form')
const closeModal = document.querySelector('.login-form form .fa-times')



// Adicionando modal 
modal.addEventListener('click', () => {
    modalToggle.classList.add('popup');
});

// Removendo modal
closeModal.addEventListener('click', () => {
    modalToggle.classList.remove('popup');
});


