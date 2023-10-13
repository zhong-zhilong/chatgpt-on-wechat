# -*- coding: utf-8 -*-
# 连接DB
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


# 数据库连接信息
user_name = "wsb"
password = "a8f8c7e62b295c63A!"
host = "rm-bp18skv36564h77m2go.mysql.rds.aliyuncs.com"  # docker-composeで定義したMySQLのサービス名
database_name = "wsbcms"

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    user_name,
    password,
    host,
    database_name,
)

# DB连接
ENGINE = create_engine(
    DATABASE,
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するか
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
# DB接続用のセッションクラス、インスタンスが作成されると接続する
Base.query = session.query_property()
