import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, message, sys_obj: sys):
        self.message = str(message)
        _, _, exc_tb = sys_obj.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_no = exc_tb.tb_lineno
        super().__init__(self.message)

    def __str__(self):
        return f"Error occurred in script [{self.file_name}] at line [{self.line_no}] | Message: {self.message}"

    
    
# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block")
#         a = 1/0
#         print("this will not be printed",a)
#     except Exception as e:
#         raise(NetworkSecurityException(e,sys))

        