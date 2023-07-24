let isusernameValid = false;
let isPwdValid = false;
let isEmailValid = false;

document.querySelector("#username").addEventListener("input",function(){
    this.classList.remove("is-valid");
     this.classList.remove("is-invalid");
     const inputusername=this.value;
     if(inputusername==0){
        this.classList.add("is-invalid");
        isusernameValid = false;
     }else{
        this.classList.add("is-valid");
        isusernameValid = true;
     }
});

    function checkPwd(){
    const pwd = document.querySelector("#password1");
    const pwd2 = document.querySelector("#password2");

    pwd.classList.remove("is-invalid");
    pwd.classList.remove("is-valid");
    pwd2.classList.remove("is-invalid");
    pwd2.classList.remove("is-valid");

    if(pwd.value == pwd2.value ){
        pwd.classList.add("is-valid");
        pwd2.classList.add("is-valid");
        isPwdValid = true;
    }else{
        pwd.classList.add("is-invalid");
        pwd2.classList.add("is-invalid");
        isPwdValid = false;
    }
}

document.querySelector("#password1").addEventListener("input",function(){
    checkPwd();
});

document.querySelector("#password2").addEventListener("input",function(){
    checkPwd();
});

document.querySelector("#email").addEventListener("input", function(){
     this.classList.remove("is-valid");
     this.classList.remove("is-invalid");
     const inputEmail=this.value;
     const reg= /^[A-Za-z0-9\.\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z0-9\.\-]+$/;
     if(!reg.test(inputEmail)){
        this.classList.add("is-invalid");
        isEmailValid = false;
     }else{
        this.classList.add("is-valid");
        isEmailValid = true;
     }
  });