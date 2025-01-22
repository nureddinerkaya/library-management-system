from sanic import Blueprint, response
from .AuthService import register_user, authenticate_user

auth_bp = Blueprint("auth", url_prefix="/auth")


@auth_bp.post("/register")
async def register(request):
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return response.json({"message": "Invalid input"}, status=400)

    try:
        await register_user(data["username"], data["password"])  # Async olarak çağrılıyor
        return response.json({"message": "User registered successfully"}, status=201)
    except Exception as e:
        return response.json({"message": str(e)}, status=500)


@auth_bp.post("/login")
async def login(request):
    data = request.json
    if not data or "username" not in data or "password" not in data:
        return response.json({"message": "Invalid input"}, status=400)

    try:
        user = await authenticate_user(data["username"], data["password"])  # Async olarak çağrılıyor
        if user:
            return response.json({"message": "Login successful"}, status=200)
        return response.json({"message": "Invalid credentials"}, status=401)
    except Exception as e:
        return response.json({"message": str(e)}, status=500)

