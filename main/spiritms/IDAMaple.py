from __future__ import absolute_import, division, print_function

import os
import os.path as path

import idaapi
import ida_kernwin
import ida_hexrays
import ida_funcs
from spiritms import PIC_DIR, FUNC_DIR, FUNC_OUT_DIR
from spiritms.InHeader import InHeaderHandler
from spiritms.Util import Util
from spiritms.PacketAnalysis import PacketAnalysis
from spiritms.OutPacketInfo import OutPacketAnalysis
   
class Hooks(idaapi.UI_Hooks):

    def populating_tform_popup(self, form, popup):
        # You can attach here.
        pass

    def finish_populating_tform_popup(self, form, popup):
        # Or here, after the popup is done being populated by its owner.
        idaapi.attach_action_to_popup(form, popup, "my:InHeader", "Rename global items", idaapi.SETMENU_APP)
        idaapi.attach_action_to_popup(form, popup, "my:PacketStruct", "Rename global items", idaapi.SETMENU_APP)
        idaapi.attach_action_to_popup(form, popup, "my:OutPacket", "Rename global items", idaapi.SETMENU_APP)
        
        
class SpiritPlugin(idaapi.plugin_t):

    flags = idaapi.PLUGIN_FIX
    comment = "Packet Structure Analyzer"
    
    help = "This is help"
    wanted_name = "SpiritMS Packet Analyzer"
    wanted_hotkey = "Shift-Ctrl-Q"
    
    def __init__(self, *args, **kwargs):
        print("[SPIRIT] SpiritMS IDA Plugin succesfully loaded")
        idaapi.plugin_t.__init__(self)
        icon_data = str(open(PIC_DIR, "rb").read())
        self.icon_id = idaapi.load_custom_icon(data=icon_data)
        
        self.load_folders()
        self.load_actions()
        self.hooks = Hooks()
        self.hooks.hook()
        
        form = idaapi.get_current_tform()
        idaapi.attach_action_to_popup(form, None, "my:InHeader", None)
        
        
    def init(self):
        return idaapi.PLUGIN_KEEP
        
        
    def run(self, arg):
        Util.clear_output_window()
        Util.create_func_name()
        print("[SPIRIT] This is the SpiritMS IDA Plugin. Our plugin allows you to analyze packet structures and find InHeaders!\nShortcuts:\nShift + Ctrl + Q (Info)\nCtrl + H (Analyze InHeaders)\n")
        
        
    def term(self):
        print("[SPIRIT] term() called")
        
        
    def load_actions(self):
    
        action_desc = idaapi.action_desc_t(
        'my:InHeader',   # The action name. This acts like an ID and must be unique
        '[Spirit] Analyze InHeader Ops',  # The action text.
        InHeaderHandler(),   # The action handler.
        'Ctrl+H',      # Optional: the action shortcut
        'Analyzes InHeader Opcodes',  # Optional: the action tooltip (available in menus/toolbar)
        self.icon_id)
        
        packet_analysis = idaapi.action_desc_t(
        'my:PacketStruct',
        '[Spirit] Analyze Packet Structure',
        PacketAnalysis(),
        'Ctrl+Shift+E',
        'Analyzes Packet Structure.',
        self.icon_id)
        
        out_packet_analysis = idaapi.action_desc_t(
        'my:OutPacket',
        '[Spirit] Grab OutPacket Info',
        OutPacketAnalysis(),
        'Ctrl+Shift+F',
        'Provides some information on a given OutPacket function.',
        self.icon_id)
        
        idaapi.register_action(packet_analysis)
        idaapi.register_action(action_desc)
        idaapi.register_action(out_packet_analysis)
        
        form = idaapi.get_current_tform()
        idaapi.attach_action_to_popup(form, None, "my:InHeader", None)
        idaapi.attach_action_to_popup(form, None, "my:PacketStruct", None)
        idaapi.attach_action_to_popup(form, None, "my:OutPacket", None)
        
    
    def load_folders(self):  

        if not path.exists(FUNC_DIR):
          try:
            os.makedirs(FUNC_DIR)
          except OSError:
            print ("Creation of Functions folder failed")
        if not path.exists(FUNC_OUT_DIR):
          try:
            os.makedirs(FUNC_OUT_DIR)
          except OSError:
            print ("Creation of Output folder failed")
        