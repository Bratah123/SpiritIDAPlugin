# SpiritIDAPlugin
This Plugin utilizes the business logic from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller) project and therefore inherits any features or known problems from it.


Author: Brandon Nguyen

# Features
  - Ability to analyze any function's Packet Structure.
  - Writes down function to an output text file.
  - Writes down analyzed packet to an output text file.
  - Automatically search for all OutPacket Headers.
  - Automatically search for InPacket Structures

# Instructions for Use:
  - NOTE: The plugin is assuming you have all the `decode` functions named.
    - If a decode function seems not to appear, you should check `init.py` and add it to KEYWORD and KEYWORD_PRINT arrays accordingly.
  - Drag the following contents of the `main` directory and drag it into `plugins` directory located in your main IDA folder.
    - change _init_.py's directory constants for the image to where SpiritMS.png is (located in the `spiritms` directory).
  - Now run IDA and a "Succesfully Loaded message" should appear in your output window!
  - Right click functions to access the tools provided by the plugin!
