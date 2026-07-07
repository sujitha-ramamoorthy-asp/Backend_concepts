from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth
import json
from fastapi.responses import RedirectResponse

load_dotenv()

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY"))

oauth = OAuth()

# Register Auth0
oauth.register(
    name="auth0",
    client_id=os.getenv("AUTH0_CLIENT_ID"),
    client_secret=os.getenv("AUTH0_CLIENT_SECRET"),
    server_metadata_url=f"https://{os.getenv('AUTH0_DOMAIN')}/.well-known/openid-configuration",
    client_kwargs={"scope": "openid profile email"},
)


@app.get("/")
def home():
    return {
        "domain": os.getenv("AUTH0_DOMAIN"),
        "client_id": os.getenv("AUTH0_CLIENT_ID"),
    }

    # return {"message": "FastAPI is running"}


@app.get("/login")
async def login(request: Request):
    return await oauth.auth0.authorize_redirect(
        request, os.getenv("AUTH0_CALLBACK_URL")
    )


@app.get("/callback")
async def callback(request: Request):
    token = await oauth.auth0.authorize_access_token(request)
    print(json.dumps(token, indent=4))
    request.session["user"] = token

    return {"message": "Login Successful", "token": token}


@app.get("/profile")
async def profile(request: Request):
    user = request.session.get("user")

    if not user:
        return {"error": "Not logged in"}

    return user["userinfo"]

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()

    return RedirectResponse(
        f"https://{os.getenv('AUTH0_DOMAIN')}/v2/logout"
        f"?client_id={os.getenv('AUTH0_CLIENT_ID')}"
        f"&returnTo=http://localhost:8000"
    )
