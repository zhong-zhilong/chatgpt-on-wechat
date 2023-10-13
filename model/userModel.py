# -*- coding: utf-8 -*-
# 定义模型
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from common.db import Base
from common.db import ENGINE


# 定义用户表的模型
class UserTable(Base):
    __tablename__ = 'fa_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False)
    email = Column(String(32), nullable=False)


# 定义POST和PUT时接收的Request Body的模型
class User(BaseModel):
    id: int
    username: str
    email: int


def createTable():
    # 表不存在时，创建表
    Base.metadata.create_all(bind=ENGINE)

