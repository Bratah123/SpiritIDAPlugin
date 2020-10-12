from spiritms import FUNC_DIR, FUNC_OUT_DIR, KEYWORDS, KEYWORDS_PRINT
from spiritms.Util import Util
import time
import idaapi

class OutPacketAnalysis(idaapi.action_handler_t):

    def __init__(self):
        idaapi.action_handler_t.__init__(self)
        self._function = []
    
    
    def activate(self, ctx):
        self.get_all_encodes()
        return 1
    
        
    def update(self, ctx): # Always Avaliable
        return idaapi.AST_ENABLE_ALWAYS
        
    def get_all_encodes(self):
        Util.clear_output_window()
        print("[SPIRIT] Grabbing all encodes.\n")
        function = Util.get_decompiled_func()
        print(function[0])
        encode_amount = 0
        for line in function:
            if "encode" in line.lower():
                print(line)
                encode_amount += 1
        print("\n[SPIRIT] Total encodes: {}".format(encode_amount))
        print("[SPIRIT] Grabbed OutPacketInfo successfully.")