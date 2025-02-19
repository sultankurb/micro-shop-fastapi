import bcrypt


async def hash_password(password: str) -> str:
    result = bcrypt.hashpw(password.lower().encode("utf-8"), bcrypt.gensalt())
    return result.decode("utf-8")


async def check_password(password: str, hashed_password: str) -> bool:
    result = bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
    return result
