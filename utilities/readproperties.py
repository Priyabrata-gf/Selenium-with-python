import configparser
config=configparser.RawConfigParser()
config.read('C:\\Users\\Priyabrata Debolina\\PycharmProjects\\Selenium with python\\Configurations\\config.ini')
class ReadConfig:
    @staticmethod
    def getapplicationURL():
        url=config.get('common info','URL')
        return url
    @staticmethod
    def username():
        Username=config.get('common info','username')
        return Username
    @staticmethod
    def password():
        Password=config.get('common info','password')
        return Password
    @staticmethod
    def getapplicationURL1():
        urladmin=config.get('common info','URLADMIN')
        return urladmin
