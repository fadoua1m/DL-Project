import os 
import sys

def error_message_details(error:Exception,error_detail:sys)->str:
    _,_,exc_tb=error_detail.exc_info()
    file_name:str=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message = f"Error occurred in Python script [{file_name}] at line number [{exc_tb.tb_lineno}] with error [{str(error)}]  "
    return error_message

class XrayException(Exception):
    def __init(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message:str=error_message_details(error_message,error_detail)
    def __str__(self):
        return self.error_message
