# shortcuts -> 진짜 자주 쓸 함수들 모아놓은 곳.
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # 전체 게시글 조회
    # todos = <QuerySet [<Todo Object (1)>, <Todo Object (2)>]>
    todos = Todo.objects.all()
    # work = request.GET.get('work')
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    return render(request, 'todos/create.html')

def new(request):
    # print(request.POST)
    # 사용자가 form을 통해서 요청 보낸 데이터로
    # 새로운 Todo를 생성 해야한다.
    todo = Todo()
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    # 사용자가 직접 입력하지 않아도 되는 데이터
    # 하지만, 데이터가 생성되려면 필수적으로 값이 있어야 하는 데이터
    # 그럼, 저장하는 과정 함수를 정의할 때, 내가 적절한 값을 넣어주면 된다.
    todo.is_completed = False
    # created_at -> auto_now_add 설정이 되어 있어서. 따로 안넣어도 된다.
    todo.save()

    # 사용자의 요청 -> 자기가 입력한 데이터를 토대로 `todo`를 `만들어 달라는 것`
    # new 함수는 그 요청에 맞춰서 todo.save() 생성까지 마쳤다.
    # 그럼 할 일 끝났는데? -> 사용자가 우리 서비스를 계속 이용할 수 있도록 해줘야 겠다.
        # 너의 게시글 생성 요청이 정상적으로 완료되었음을 알려줄 수 있어야겠다.
        # `게시글 생성 완료 되었습니다.` 라는 쓸데없는 페이지를 보여줄 이유가 없다.
        # 너가 만들어 달라고 했었던 그 데이터가 잘 만들어졌는지 확인하는 가장 쉬운방법
        # 그 게시글의 상세 페이지를 보여주면 되겠다.
            # 근데.. 상세페이지? 이거 우리 처리해주는 부서 따로 있다.
            # detail view 함수가 처리 해준다.
        # 마치 공무원이 `그거 우리 관할 아닙니다. 해당 부서 연결해 드릴게요.`
            # 와 같이 redirect 시켜주면 된다.
            # 근데 우리는 redirect 라는거 정의 한 적 없다?
        # 어디로?? -> 특정 앱이 가진, 어떤 기능을 호출.
            # 특정 앱이 가진 어떤 기능 : 이름을 정해놨다.
            # app_name, pattern_name
    # return redirect(f'todos/{todo.pk}') -> 하드코딩 안한다.
    return redirect('todos:detail', todo.pk) # detail 경로는? arg 필요로한다. todo.pk

# todo_pk : 사용자가 주소창에 입력한 값.
def detail(request, todo_pk):
    # 상세 페이지 -> pk값이 todo_pk인 할일 정보 하나 조회
    # get함수에 pk라는 값이 todo_pk 인 값을 찾는 것.
    # pk -> Todo가 가지고 있는 속성들 중 하나.
    # get 메서드 호출한 결과를 나중에도 쓸거기 때문에 todo 변수에 할당.
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request, todo_pk):
    # 누구를? 사용자가 삭제 해달라고 한 pk값을 가진 대상 데이터를
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    # 삭제 요청에 맞춰서, 삭제 담당 부서가 해당 데이터를 삭제 했다.
    # 삭제 완료 되셨구요, 다른 볼 일이 있으시면, index 경로로 가시면 됩니다.
    return redirect('todos:index')

# 수정 대상에 수정할 데이터를 입력 할 수 있는 페이지
def update(request, todo_pk):
    # 수정 할거야 누구를?
    todo = Todo.objects.get(pk=todo_pk)
    # 할 일을 생성 -> 처음엔 당연히 0부터 시자이다.
    # 할 일을 수정 -> 수정 대상이 원래 가지고 있는 데이터
        # 그걸 html에 같이 그려주면 좋겠다.
    context = {
        'todo': todo
    }
    return render(request, 'todos/update.html', context)

def edit(request, todo_pk):
    # 새 Todo instance가 아니라, 기존에 있는 정보를 가지고
    todo = Todo.objects.get(pk=todo_pk)
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    # todo.is_completed는 용? -> 지금 안만듬.
    todo.save()
    # 할 일 정보 수정이 끝났으면? -> 해당 상세 정보 페이지로 보낸다.
    return redirect('todos:detail', todo_pk)