"""
routes/auth.py
--------------
Handles Google OAuth login & callback logic
"""
from fastapi import APIRouter,Depends,Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.schemas.database  import sessionLocal
from app.models.models import User
from app.authentication.oauth import oauth
from app.authentication.auth import create_jwt

#router with/auth prefic

router=APIRouter(prefix="/auth",tags=["Auth"])

def get_db():
    """
    Dependency to get DB session
    Automatically closes session after request
    """
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()
from fastapi import Request
from app.configurations.auth import settings


@router.get("/google/login")
async def google_login(
    request: Request,
    platform: str = "web"
):
    """ Redirect user to google login """
    """
    platform can be:
        web (default)
        android
        ios
    """

    request.session["platform"] = platform.lower()

    redirect_uri = (
        f"{settings.BACKEND_URL}/auth/google/callback"
    )

    return await oauth.google.authorize_redirect(
        request,
        redirect_uri,
        access_type="offline",
        prompt="consent",
    )


"""
    Step 2:
    Google redirects back to this endpoint after login

    - Fetch user info from Google
    - Store user in DB if not exists
    - Generate JWT token
  from app.config import settings

"""
@router.get("/google/callback")
async def google_callback(
    request: Request,
    db: Session = Depends(get_db)
):
    

    token = await oauth.google.authorize_access_token(request)

    access_token = token.get("access_token")
    refresh_token = token.get("refresh_token")

    user_info = token.get("userinfo")

    email = user_info.get("email")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:

        user = User(
            email=email,
            provider="google",
            access_token=access_token,
            refresh_token=refresh_token,
        )

        db.add(user)

    else:

        user.access_token = access_token

        if refresh_token:
            user.refresh_token = refresh_token

    db.commit()

    jwt_token = create_jwt(email)

    platform = request.session.get("platform", "web")

    if platform == "android":
        redirect_url = settings.ANDROID_REDIRECT

    elif platform == "ios":
        redirect_url = settings.IOS_REDIRECT

    else:
        redirect_url = f"{settings.WEB_URL}/login-success"

    return RedirectResponse(
        url=f"{redirect_url}?token={jwt_token}"
    )