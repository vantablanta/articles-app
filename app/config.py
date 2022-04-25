class Config:
    """
    Parent config class 
    """
    pass

class ProdConfig(Config):
    """
    production config
    """
    pass

class DevConfig(Config):
    """
    Developemnt configuartions
    """
    DEBUG = True
