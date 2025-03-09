from pydantic import BaseModel, ConfigDict, Field

MODEL_CONFIG = ConfigDict(
    from_attributes=True,
    str_to_lower=True,
    str_strip_whitespace=True
)


class RoleBase(BaseModel):
    model_config = MODEL_CONFIG
    name: str = Field(max_length=20)


class RolePublic(RoleBase):
    id: int


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass
