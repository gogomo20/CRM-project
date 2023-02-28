var xhr = new XMLHttpRequest();
var dataSubmit = document.getElementById("submit");

//lista de funções ajax 27/02/2023c
var ajax = {
    //faz o tratamento e envia as informacoes de request 27/02/2023
    "openLogin":function(dtd) {
        xhr.open("POST",'auth/login',false)
        xhr.send(JSON.stringify(dtd))
    },
    //aguarda o status de finalização de
    "wating":function(){
        let tryRequests
        while (xhr.readyState != 4 && xhr.readyState != 200 && tryRequests != 15) {
            console.log(xhr.readyState)
            tryRequest += 1
        }
        if (tryRequests == 15) {
            alert("erro ao comunicar com o servidor tente novamente mais tarde")
        }
    },
    "response": function () {
        if (xhr.response) {
            return JSON.parse(xhr.response)
    }},
    "token": function() {
        return xhr.response
    }

}





dataSubmit.addEventListener("click", function () {
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value

    // substituições de if's em meu codido para condicional de switch 27/02/2023c

    
        if( email.includes("@") && password){ 
            var data = {"email": email,"password":password}
            ajax.openLogin(data)
            ajax.wating()
            
            if(!ajax.response().error && ajax.token){
                localStorage.setItem("token",ajax.token())
                let urlTo = window.location.href
                urlTo = urlTo.replace("login","")
                urlTo += "home"
                window.location.href = urlTo
                return;
            }
        }

        
        alert("usuario ou senhas invalidos")
    // se acaso o codigo acima quebre tente usar o comentado abaixo
    /*if (email.includes("@") && password != undefined) {
        //TODO - requisita os dados de login e autentica na roda correta 23/02/2023c
        data = {"email": email,"password": password}
        ajax.open("POST",'auth/login',false)
        ajax.send(JSON.stringify(data))
    }else{
        alert("usuario ou senha invalidos")
        return;
    }
    while (ajax.readyState != 4 &&   ajax.readyState != 200) {
        console.log(ajax.readyState)
    }
    retorno = JSON.parse(ajax.response)
    if(retorno.error){
        alert(retorno.error)
    }else{
        localStorage.setItem("token",ajax.response)
        let urlTo = window.location.href

        if (urlTo.includes("login")) {
            urlTo = urlTo.replace("login","")
        }
        urlTo += "home"
        window.location.href = urlTo
    }*/
})

xhr.onreadystatechange = function() {
    if (xhr.readyState == 4 || xhr.readyState == 200 ) {
        console.log("sucesss")
    }else{
        console.log(xhr.readyState)
    }
}