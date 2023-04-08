"""
通过函数封装，将对数据库的操作封装成函数
对于不同的表可以建立不同的文件
再在文件里对要实现的功能进行包装实现。

例如对emp表的操作封装在emp.py文件中。。。
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

url = 'mysql+pymysql://root:12345679@localhost:3306/world'
engine = create_engine(url)
Session = sessionmaker(bind=engine)



