from typing import List                      # 定义嵌套实体所需List类型
from common.db import session                # DB连接session
from model.userModel import UserTable, User  # 导入对应的模型
from app import app
from common.log import logger

# ----------定义API------------

# 获取表中的全部数据 GET
@app.get("/users")
def read_users():
    logger.info("收到请求：获取用户表数据")
    users = session.query(UserTable).all()
    return users

# 根据ID获取数据 GET
@app.get("/users/{user_id}")
def read_user(user_id: int):
    logger.info("收到请求：获取指定用户的数据")
    user = session.query(UserTable).\
        filter(UserTable.id == user_id).first()
    return user

# 创建数据 POST
@app.post("/user")
# /user?name="三郎"&age=10
async def create_user(name: str, age: int):
    logger.info("收到请求：创建用户数据")
    user = UserTable()
    user.name = name
    user.age = age
    session.add(user)
    session.commit()

# 更新多条记录 PUT
@app.put("/users")
# model中定义的User模型的请求body以list形式获取
# users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
async def update_users(users: List[User]):
    for new_user in users:
        logger.info("收到请求：更新用户数据")
        user = session.query(UserTable).\
            filter(UserTable.id == new_user.id).first()
        user.name = new_user.name
        user.age = new_user.age
        session.commit()

