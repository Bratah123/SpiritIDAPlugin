from spiritms import FUNC_DIR, FUNC_OUT_DIR, KEYWORDS, KEYWORDS_PRINT
from spiritms.Util import Util
import time
import idaapi
import os

class FileOpener(idaapi.action_handler_t):

    def __init__(self):
        idaapi.action_handler_t.__init__(self)
        self.txt_file_name = ""
    
    
    def activate(self, ctx):
        self.write_func_input()
        return 1
    
        
    def update(self, ctx): # Always Avaliable
        return idaapi.AST_ENABLE_ALWAYS
        
        
    def write_func_input(self):
        self.assign_txt_file()
        with open(FUNC_DIR + "/{}.txt".format(self.txt_file_name), "w") as f:
        
            decompiled_func = Util.get_decompiled_func()
            full_func = ""
            
            for line in decompiled_func:
                full_func += line + "\n"
            
            f.write(full_func)
            open_file()
    
    
    def assign_txt_file(self):
        self.txt_file_name = Util.create_func_name()
        
        
    def open_file(self):
        os.system("notepad {}/{}".format(FUNC_DIR,  self.txt_file_name)
        
    
    