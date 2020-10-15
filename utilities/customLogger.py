import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C:\\Users\\Priyabrata Debolina\\PycharmProjects\\Selenium with python\\Logs\\automation.log",
                            format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m%d%y %H:%M:%S')

        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
