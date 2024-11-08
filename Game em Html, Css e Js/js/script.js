const personagem = document.querySelector('.personagem');

const pulo = () =>{
    personagem.classList.add('pulo');

    setTimeout(() => {
    personagem.classList.remove('pulo');
}, 500);
}
document.addEventListener('keydown', pulo);