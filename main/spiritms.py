from __future__ import absolute_import, division, print_function

def PLUGIN_ENTRY(*args, **kwargs):
    from spiritms.IDAMaple import SpiritPlugin
    return SpiritPlugin(*args, **kwargs)
