# 通过自定义装饰器来实现单例模式。
# 单例模式是一种设计模式，它确保一个类只有一个实例，并提供全局访问点以访问该实例。
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance
