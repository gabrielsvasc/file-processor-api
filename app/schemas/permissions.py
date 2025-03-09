from pydantic import BaseModel, ConfigDict, Field

MODEL_CONFIG = ConfigDict(
    from_attributes=True,
    str_to_lower=True,
    str_strip_whitespace=True
)


class PermissionBase(BaseModel):
    model_config = MODEL_CONFIG
    name: str = Field(max_length=30)


class PermissionPublic(PermissionBase):
    id: int


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(PermissionBase):
    pass
