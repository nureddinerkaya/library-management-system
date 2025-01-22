from sanic import Blueprint
from sanic.response import json

from backend.app.auth.AuthService import AuthService

# Define the Blueprint for Auth entity
auth_bp = Blueprint("AuthBlueprint", url_prefix="/api/auth")


@auth_bp.route("/login", methods=["POST"])
async def login(request):
    """
    Endpoint to authenticate a user and generate a token.
    Expected JSON request body:
    {
        "username": "user_name",
        "password": "user_password"
    }
    """
    return await AuthService.login(request)


@auth_bp.route("/logout", methods=["POST"])
async def logout(request):
    """
    Endpoint to logout a user by invalidating their session or token.
    """
    return await AuthService.logout(request)


@auth_bp.route("/verify", methods=["GET"])
async def verify_token(request):
    """
    Endpoint to verify if the user has a valid token.
    Expected headers: Authorization: Bearer <token>
    """
    return await AuthService.verify_token(request)

