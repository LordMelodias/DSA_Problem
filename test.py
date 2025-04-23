from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, File

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

# Create your views here.
@api_view(['POST'])
def login (request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
        print(user)
    except User.DoesNotExist:
        return Response({"error": "User does not exist"}, status=400)
    if user.password == password:
        return Response({"message": "Login successful"}, status=200)
    else:
        return Response({"error": "Invalid password"}, status=400)

@api_view(['POST'])
def register(request):
    print("It come in register")
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    try:
        user = User.objects.create(username=username, password=password, email=email)
        return Response({"message": "User created successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=400)



@api_view(['POST'])
def upload_excel(request):
    if request.method =='POST':
        file = request.FILES.get('files')
        if file:
            uploaded_file = File(file=file)
            uploaded_file.save()
            return Response({"message": "File uploaded successfully"}, status=200)
        else:
            return Response({"error": "No file provided"}, status=400)
        
        
@api_view(['GET'])
def get_uploaded_files(request):
    files = File.objects.all()
    file_list = []
    for file in files:
        file_url = file.file.url
        file_list.append(file_url)
    if not file_list:
        return Response({"message": "No files found"}, status=404)
    return Response({"files": file_list}, status=200)

@api_view(['GET'])
def getallUser(request):
    users = User.objects.all()
    user_list = []
    for user in users:
        user_data = {
            "username": user.username,
            "email": user.email,
            "password": user.password
        }
        user_list.append(user_data)
    return Response({"users": user_list}, status=200)

