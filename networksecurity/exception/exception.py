import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception): # inharited from Exception class 
    def __init__(self, message, sys_info=None):
        super().__init__(str(message))
        self.message = str(message)
        self.sys_info = sys_info

    def __str__(self): # This is overriding method in this class this not present in parent class
        return "Error occured in python script name [{0}] line no [{1}] error message [{2}]".format() 
    
    
# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block")
#         a = 1/0
#         print("this will not be printed",a)
#     except Exception as e:
#         raise(NetworkSecurityException(e,sys))

        