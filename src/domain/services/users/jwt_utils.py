from datetime import timedelta, datetime, timezone
from src.domain.schemas import UserBase
from pathlib import Path

import jwt

TOKEN_TYPE_FIELD = "type"
ACCESS_TOKEN_TYPE = "access"
REFRESH_TOKEN_TYPE = "refresh"



def encode_jwt(
    payload: dict,
    private_key: str,
    algorithm: str,
    expire_minutes: int,
    expire_timedelta: timedelta | None = None,
) -> str:
    to_encode = payload.copy()
    now = datetime.now(timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str,
    algorithm: str,
) -> dict:
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )
    return decoded


def create_jwt(
    token_type: str,
    token_data: dict,
    expire_minutes: int | None = None,
    expire_timedelta: timedelta | None = None,
) -> str:
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
        algorithm="RS256",
        private_key=f'{Path(__file__).parent.parent}/certificate/jwt-public-key.pem',
    )


def create_access_token(user: UserBase) -> str:
    jwt_payload = {
        # subject
        "sub": user.phone_number,
        "phone": user.phone_number
        # "logged_in_at"
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=15,
    )


def create_refresh_token(user: UserBase) -> str:
    jwt_payload = {
        "sub": user.phone_number,
        # "username": user.username,
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=30),
    )
