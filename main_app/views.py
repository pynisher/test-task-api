from django.http import JsonResponse, HttpResponse
from .models import Encrypt, Decrypt
from .serializers import EncryptSerializer, DecryptSerializer
from .eas256 import PyAesCrypt


def encrypt(request):
    try:
        text = request.GET['text']
    except:
        text = 'Hello World'
    try:
        password = request.GET['password']
    except:
        password = '123'

    encr = Encrypt(text=text, password=password)
    try:
        aes_crypt = PyAesCrypt()
        encr_text = aes_crypt.encrypt(password, text)
        encr.encrypted_text = encr_text.decode()
    except:
        encr.encrypted_text = 'encrypt error. wrong data'
    encr.save()

    serializer = EncryptSerializer(encr)
    return JsonResponse(serializer.data, safe=False)


def decrypt(request):
    try:
        text = request.GET['text']
        text = text.replace(' ', '+')
    except:
        text = 'MJG1JBE24i8WygatRp6JFw=='
    try:
        password = request.GET['password']
    except:
        password = '123'

    decr = Decrypt(text=text, password=password)
    try:
        aes_crypt = PyAesCrypt()
        encr_text = aes_crypt.decrypt(password, text.encode())
        decr.decrypted_text = encr_text.decode()
    except:
        decr.decrypted_text = 'decrypt error. wrong data'
    decr.save()

    serializer = DecryptSerializer(decr)
    return JsonResponse(serializer.data, safe=False)


def index(request):
    return HttpResponse("""Hello.<br>API usage:<br>/encrypt/?text=text_to_encrypt&password=your_password
    <br>/decrypt/?text=text_to_decrypt&password=your_password""")
