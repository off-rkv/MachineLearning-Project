import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() #exc_tb`**: the traceback object —> contains information about where the exception occurred
    file_name=exc_tb.tb_frame.f_code.co_filename #frame(filename,no. arguments,function name).f_code().co_filename(exract the file name)
    error_message="Error occured in python script name [{0}] line number [{1}] error messgae [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

