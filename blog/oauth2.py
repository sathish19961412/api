from fastapi import Depends, HTTPException, status
from . import token
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentails_exception = HTTPException(
    status_code = status.HTTP_401_UNAUTHORIZED,
    details= "Could not validate credentails",
    headers={"WWW-Authenticate": "Bearer"}
    )

    return token.verify_token( data , credentails_exception )
