// $('.message a').click(function(){
//     $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
//  });


function userLogar() {
    login = document.getElementById('login')
    senha = document.getElementById('senha')

    if (login.value == 'teste' & senha.value == '12345'){
        let active = document.querySelector('.success')
        active.classList.remove("active")
        location.href = "http://127.0.0.1:5500/logado.html"

    } else {
        alert('erro')
    }
}
