# SpiritIDAPlugin
Author: Brandon Nguyen

# Features
  - Ability to analyze any function's Packet Structure.
  - Writes down function to an output text file.
  - Writes down analyzed packet to an output text file.
  - Automatically search for all OutPacket Headers.
  - Automatically search for InPacket Structures

# Instructions for use:
  - Drag the following contents of the `main` directory and drag it into `plugins` directory located in your main IDA folder.
    - change __init__.py's directory constants for the image to where SpiritMS.png is (located in the `spiritms` directory).
  - Now run IDA and a "Succesfully Loaded message" should appear in your output window!
  - Right click functions to access the tools provided by the plugin!
