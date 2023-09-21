from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, update_session_auth_hash,logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from accounts.models import Text,Profile
from accounts.forms import ProfileForm

#トップページ
def index(request):
    username=request.user
    return render(request, 'index.html',{'username':username})

#会員登録
def regist(request):
    if request.method == 'GET':
        return render(request, 'regist.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password1 = request.POST.get('password1', None)
        user = User.objects.create_user(username=username, password=password1)
        profile = Profile(user=user)
        profile.save()
    return redirect('user_login')
#会員登録の時IDが重複かをLIVEで確認
def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username', '').strip()
        if not username:
            return JsonResponse({'result': 'error', 'message': 'IDを入力してください。','idck': False})
        users = User.objects.filter(username=username)
        if users.exists():
            return JsonResponse({'result': 'success', 'message': '使用できないIDです。','idck': False})
        else:
            return JsonResponse({'result': 'success', 'message': '使用可能なIDです.','idck': True})
#アカウントの削除
def deleteacc(request):
    user = request.user
    alert_message = None
    if user.is_superuser and user.username == "admin":
        alert_message = 'adminアカウントは削除できません!'
    elif request.method == "POST":
        user.delete()
        return redirect('index')
    return render(request, 'delacc.html', {'alert_message': alert_message})
#パスワードを変更
def change_password(request):
    if request.method == "POST":
        user = request.user
        origin_password = request.POST.get('origin_password')
        if check_password(origin_password, user.password):
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if origin_password == new_password:
                messages.error(request, '現在パスワード以外のパスワードを入力してください！')
            elif new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'パスワードを変更しました。')
                return redirect('index')
            else:
                messages.error(request, 'パスワードと再確認が異なります！')
        else:
            messages.error(request, '現在パスワードを確認してください。')
        return render(request, 'changepw.html')
    else:
        return render(request, 'changepw.html')

# ログイン
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        # ユーザー認証を試みる
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # 認証成功した場合、ログインセッションを開始
            login(request, user)
            return redirect('profile')  # ログイン後のリダイレクト先を設定してください
        else:
            # 認証失敗時の処理を行う（エラーメッセージなど）
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        # GETリクエストの場合はログインフォームを表示
        return render(request, 'login.html')

#ログアウト
def user_logout(request):
    logout(request)
    return redirect('index')

#ホームページ
def home(request):
    toukou = Text.objects.all
    if request.method =='POST':
        text = request.POST.get('text',None)
        created_by = request.user
        m = Text(text= text,created_by=created_by)#ここでつくった変数をTextというデータベースモデルに保存
        m.save()
    return render(request,'home.html',{'Text':toukou})

def profile(request):
    username = request.user.username
    form = ProfileForm(request.POST, instance=request.user.profile)
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            birth_month = form.cleaned_data.get('birth_month')
            birth_day = form.cleaned_data.get('birth_day')
            birth_year = form.cleaned_data.get('birth_year')
            intoroduction = form.cleaned_data.get('introduction_text')
            location = form.cleaned_data.get('location')
            birthday = f"{birth_month}/{birth_day}/{birth_year}"
            profile = form.save(commit=False)
            profile.birthday = birthday
            profile.introduction_text = intoroduction
            profile.location = location
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request,'profile.html',{'username':username,'form': form,'user_profile':user_profile})

def Delete(request, text_id):
    model = get_object_or_404(Text, id=text_id) #Textというデータベースモデルの中のidがtext_idのものを抽出して、modelという変数に入れる
    if request.method =='POST':
        model.delete()
        return redirect('home') #関数を実行

def reply(request, text_id):#text_idは返信された投稿のId
    toukou = Text.objects.get(id=text_id)#toukouは返信された投稿
    reply_ = Text.objects.filter(reply_to=text_id)#replyは返信した投稿
    if request.method == 'POST':#データベースに情報渡したいときはPOST #GETはページ移動のとき　#postかgetはhtml見たらわかる。getは記載なし
        text = request.POST.get('text', None)#nameがついてる部分の情報をgetしてtextに代入
        created_by = request.user #データベースからログインしてるユーザーの情報がcreated_byに入る
        reply_to = text_id#どの投稿に返信したかがわかるようにIDをいれておく
        m = Text(text=text, created_by=created_by, reply_to=reply_to)
        m.save()
        return redirect('reply', text_id=text_id)
    return render(request, 'reply.html', {'text': toukou, 'reply_': reply_})