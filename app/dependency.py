from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth


# 認証関数の定義
def get_current_user(
    cred: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> HTTPAuthorizationCredentials:
    if not cred:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={"WWW-Authenticate": "Bearer"},
        )
    try:
        cred = auth.verify_id_token(cred.credentials)
    except auth.ExpiredIdTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return cred
