
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book,FruitsInfo,FruitsVendors
from .serializer import UserSerializer,BookSerializer,FruitsSerializer



@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # if User.objects.filter(email=request.data['email']).exists():
        #     return Response({"email": f"email {request.data['email']} arleady exist"})
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)

        # serializer = UserSerializer(instance=user)
        
        return Response({'token':token.key,'user':serializer.data})
    
        
    return Response(serializer.errors,status=400)
        
@api_view(['POST'])
def login_user(request):
    username = request.data["username"]
    password= request.data["password"]  
    try:
        user=User.objects.get(username=username)
    except:
        return Response({'detail':"input not found"},status=404)        
    if not user.check_password(password):
        return Response({'detail':"input not found"},status=404)
    token,created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({'token':token.key,'user':serializer.data})

    
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
@authentication_classes
def test_token(request):
    return Response({'detail':"input not found"},)





@api_view(['GET'])
def getBook(request,id):
    try:
       book_obj = Book.objects.get(id=id)
       
       return Response(BookSerializer(book_obj).data)
    except:
        return Response({'error':'detail not found'})

@api_view(['PUT','GET'])
def UpdateBook(request,id:int):
    try:
       book_obj = Book.objects.get(id=id)
       if request.method == 'PUT':
           print(request.data)
           book_obj.title = request.data.get('title')
           book_obj.author = request.data.get('author')
           book_obj.published = bool(request.data.get('published'))

           book_obj.save()

        #    serializer = BookSerializer(book_obj,data=request.data)
        #    print(serializer)
        #    if serializer.is_valid():
        #        serializer.save()
        #     #    return Response(serializer.data)
       
       return Response(BookSerializer(book_obj).data)
    
    
    except:
        return Response({'error':'detail not found'})




@api_view(['GET'])
def getFruitInfo(request,id:int):
    try:
       book_obj = FruitsInfo.objects.get(id=id)
       
       return Response(FruitsSerializer(book_obj).data)
    except:
        return Response({'error':'detail not found'})

@api_view(['GET'])
def filterFruits(request):
    try:
    #    book_objs = FruitsInfo.objects.filter(name=name)
       fruits = FruitsInfo.objects.all()
       book_bjs = Book.objects.all()
    #    book_json = BookSerializer(book_bjs,many=True)
       serializer = FruitsSerializer(fruits,many=True)
       return Response(serializer.data)
    except:
        return Response({'error':'detail not found'})
    
@api_view(['GET'])
def getFruitInfo(request,id):
    try:
       book_obj = FruitsInfo.objects.get(id=id)
       serializer = FruitsSerializer(book_obj)
       return Response(serializer.data)
    except:
        return Response({'error':'detail not found'})


@api_view(['POST'])
def createBook(request):
    try:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        
        return Response(serializer.error,status=400)
        
    except:
        return Response({'error':'detail not found'})
    