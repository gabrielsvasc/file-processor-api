from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
from app.core.database import create_session

SessionDep = Annotated[Session, Depends(create_session)]
