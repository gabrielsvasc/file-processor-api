from pydantic import BaseModel, ConfigDict

MODEL_CONFIG = ConfigDict(
    from_attributes=True,
    str_to_lower=True,
    str_strip_whitespace=True
)


class RoleBase(BaseModel):
    model_config = MODEL_CONFIG
    name: str


class RolePublic(RoleBase):
    id: int
    permissions: list[str]


class RoleCreate(RoleBase):
    permissions: list[str]


class RoleUpdate(BaseModel):
    model_config = MODEL_CONFIG
    name: str | None = None
    permissions: list[str] | None = None
