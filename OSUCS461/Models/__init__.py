from pydantic import BaseModel

class BasePydanticModel(BaseModel):
	class Config:
		from_attributes = False
		validate_assignment = True

class user(BaseModel):
	uuid: str
	name: str
	time_created: int

class UserPost(BaseModel):
	uuid: str
	user_uuid: str
	post_9char: str
	text: str
	time_created: int