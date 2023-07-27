var idck = false;

const sendit = () => {
    const username = document.regiform.username;
	const userpassword1 = document.regiform.password1;
    const userpassword2 = document.regiform.password2;
    const useremail = document.regiform.email;

    if(username.value == '') {
        alert('IDを入力してください。');
        username.focus();
        return false;
    }
    if(userpassword1.value == '') {
        alert('パスワードを入力してください。');
        userpassword1.focus();
        return false;
    }
    if(userpassword2.value == '') {
        alert('パスワード再確認を入力してください。');
        userpassword2.focus();
        return false;
    }
    if(userpassword1.value != userpassword2.value) {
        alert('パスワードと再確認が異なります！');
        userpassword2.focus();
        return false;
    }
    if(useremail.value == '') {
        alert('メールアドレスを入力してください。');
        useremail.focus();
        return false;
    }
    const expEmailText = /^[A-Za-z0-9\.\-]+@[A-Za-z0-9\.\-]+\.[A-Za-z0-9\.\-]+$/;
    if(!expEmailText.test(useremail.value)) {
        alert('正しいメールアドレスではありません。');
        useremail.focus();
        return false;
    }
    if(idck==0){
        alert('ID使用可否を確認してください。');
        return false;
    }
    if(idck==false){
        alert('使用できないIDです。');
        return false;
    }
    return true;
}

$(function(){
    $('#username').change(function () {
        $('#idcheck').show();
        idck=false;
    });

    $('#idcheck').click(function(){
        var username = $('#username').val()
        if(username == ''){
            alert('IDを入力してください。')
            return;
        }

        $.ajax({
            url:'checkname?username='+username,
            type:'get',
            dataType:'json',
            success:function(response){
                if(response.result != 'success'){
                    console.error(response.data)
                    return;
                }
                if(response.data == 'exist'){
                    alert("使用できないIDです。");
                    $('#username').val('').focus();
                    return;
                }else{
                    $('#idcheck').hide();
                    $("#regist-submit").attr("name_check_result", "success");
                    idck=true;
                    return;
                }
            },
            error : function(xhr, error){
                alert("通信問題！");
                console.error("error : " + error);
            }
        })
    });
$('#regi-form').submit(function() {
       console.log($("#regist-submit").attr("name_check_result"));

       if($("#regist-submit").attr("name_check_result") == "fail") {
          alert("ID checkボータンを押してください。");
          $("#username").focus();
          return false;
       }
    });

    $("#username").on("propertychange change keyup paste input", function(){
       $('#idcheck').show();
       $("#regist-submit").attr("name_check_result", "fail");
    });
});

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