import idaapi
import ida_kernwin
import ida_hexrays
import ida_funcs
import ida_lines
from spiritms import KEYWORDS, KEYWORDS_PRINT

class Util:

    @staticmethod
    def is_ida70():
        major, minor = map(int, idaapi.get_kernel_version().split("."))
        return major == 7 and minor >= 0


    @staticmethod
    def clear_output_window():
        if Util.is_ida70():
            from PyQt5 import QtGui, QtCore, QtWidgets
            form = idaapi.find_tform("Output window")
            w = idaapi.PluginForm.FormToPyQtWidget(form)
            w.setFocus()
        else:
            from PySide import QtGui, QtCore
            form = idaapi.find_tform("Output window")
            w = idaapi.PluginForm.FormToPySideWidget(form)
            w.setFocus()
        idaapi.process_ui_action("msglist:Clear")
        
        
    @staticmethod
    def get_decompiled_func():
        f = ida_funcs.get_func(ida_kernwin.get_screen_ea())
        if f is None:
            Util.clear_output_window()
            print("[SPIRIT] Please position the cursor within a function")
            return True

        cfunc = ida_hexrays.decompile(f)
        if cfunc is None:
            Util.clear_output_window()
            print("[SPIRIT] Failed to decompile!")
            return True

        sb = cfunc.get_pseudocode()
        function_arr = []
        for line in sb:
            function_arr.append(ida_lines.tag_remove(line.line))
        return function_arr
        
    
    @staticmethod
    def check_keyword_and_print(keyword, GET_ALL_DECODES):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    return True
            elif key not in keyword.lower() and "decode" in keyword.lower() and GET_ALL_DECODES:
                return True # just incase our keywords array doesn't have that decode already set
            return True
        return False
    
    
    @staticmethod
    def check_keyword_and_return(keyword, GET_ALL_DECODES):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    return KEYWORDS_PRINT[KEYWORDS.index(key)]
            elif key not in keyword.lower() and "decode" in keyword.lower() and GET_ALL_DECODES:
                return keyword  # just in case our keywords array doesn't already have that Decode saved
        return ""
        
    
    @staticmethod
    def add_decode_to_list(list, keyword):
        for key in KEYWORDS:
            if key in keyword.lower():
                if key != "if" and key != "else":
                    list.append(KEYWORDS_PRINT[KEYWORDS.index(key)])
        return list
        
    
    @staticmethod
    def create_func_name():
        function = Util.get_decompiled_func()
        full_func_name = function[0]
        func_name_arr = full_func_name.split(" ")
        name_arr_len = len(func_name_arr)
        for i in range(name_arr_len):
            if "::" not in func_name_arr[i]:
                func_name_arr[i] = ''
        
        new_name = ""
        
        for word in func_name_arr:
            if word != '':
                new_name += word
        
        final_name = ""
        
        for c in range(len(new_name)):
            if new_name[c] == ':':
                i = c + 2 # we start at 2 because 1 would mean we begin at the 2nd ":"
                while new_name[i] != "(":
                    final_name += new_name[i]
                    i += 1
                break
                
        return final_name
        
        
    @staticmethod
    def is_decode_func(func_name):
        for key in KEYWORDS:
            if key in func_name:
                return True
        return False
                