from pydantic import BaseModel, ConfigDict


class RoleBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        str_to_lower=True,
        str_strip_whitespace=True
    )
    name: str


class RolePublic(RoleBase):
    id: int
    permissions: list[str]


class RoleCreate(RoleBase):
    permissions: list[str]


class RoleUpdate(RoleCreate):
    id: int
