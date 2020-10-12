import idaapi
import time
from spiritms.Util import Util

class InHeaderHandler(idaapi.action_handler_t):

    def __init__(self):
        idaapi.action_handler_t.__init__(self)
        self._function = []
        
        
    # Say hello when invoked.
    def activate(self, ctx):
        self._function = Util.get_decompiled_func()
        Util.clear_output_window()
        print("[SPIRIT] Analyzing InHeader Ops....\n")
        opcodes = self.get_in_header_ops()
        if len(opcodes) < 1:
            print("No InHeaders were found for this function")
        print("\n[SPIRIT] Analysis Complete!")
        return 1
        
        
    # This action is always available.
    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS
        
    
    def get_func_name(self):
        return self.function[0]
    
    
    def get_in_header_ops(self):
        total_ops =[]
        print(self.get_func_name() + ":")
        for line in self.function:
            if "coutpacket::coutpacket" in line.lower():
                print("  " + line.strip())
                total_ops.append(line)
        return total_ops
        
        
    @property
    def function(self):
        return self._function