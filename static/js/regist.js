var idck = false;

const sendit = () => {
  const username = document.regiform.username;
  const userpassword1 = document.regiform.password1;
  const userpassword2 = document.regiform.password2;

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
  const expPwText = /^.{6,}$/;
  if(!expPwText.test(userpassword1.value)) {
    alert('パスワードは6文字以上で入力してください。');
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
  if(idck==0){
    alert('ID使用可否を確認してください。');
    username.focus();
    return false;
  }
  if(idck==false){
    alert('使用できないIDです。');
    username.focus();
    return false;
  }
  alert("登録成功！");
return true;
}

$(document).ready(function() {
  $('#username').on('keyup', function() {
  var username = $(this).val();
    $.ajax({
      type: 'GET',
      url: "check_username/",
      data: { 'username': username },
      dataType: 'json',
      success: function (data) {
        if (data.result === 'success') {
          idck = data.idck;
        if (data.idck) {
          idck = true;
            $('#result').text(data.message).css('color', 'green');
            $('#username').removeClass('is-invalid').addClass('is-valid');
        } else {
          idck = false;
          $('#result').text(data.message).css('color', 'red');
          $('#username').removeClass('is-valid').addClass('is-invalid');
        }
          $('#result').text(data.message);
        } else {
          idck=false;
          console.log("Error:", data.message);
          $('#result').text(data.message).css('color', 'red');
          $('#username').removeClass('is-valid').addClass('is-invalid');
        }
      },
        error: function(error) {
        console.log("Error:", error);
      }
    });
  });
});

let isPwdValid = false;
let isPwdValid2 = false;

function checkPwdlength(){
  const pwd = document.querySelector("#password1");
  pwd.classList.remove("is-invalid");
  pwd.classList.remove("is-valid");
  
  if(pwd.value.length > 5){
    pwd.classList.add("is-valid");
    isPwdValid = true;
  }else{
    pwd.classList.add("is-invalid");
    isPwdValid = false;
  }
}

function checkPwd(){
  const pwd = document.querySelector("#password1");
  const pwd2 = document.querySelector("#password2");
  pwd2.classList.remove("is-invalid");
  pwd2.classList.remove("is-valid");

  if(pwd.value == pwd2.value){
    pwd2.classList.add("is-valid");
    isPwdValid2 = true;
  }else{
    pwd2.classList.add("is-invalid");
    isPwdValid2 = false;
  }
}

document.querySelector("#password1").addEventListener("input",function(){
  checkPwdlength();
});

document.querySelector("#password2").addEventListener("input",function(){
  checkPwd();
});