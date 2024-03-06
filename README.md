# SpiritIDAPlugin
This Plugin utilizes the business logic from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller) project and therefore inherits any features or known problems from it.

Open source as of: 10/18/2020

Any questions relating to setup or any errors can be redirected to `Not Brandon #4444`. Make sure to check github for any new updates to the plugin.

# Tech Stack
  - IDA Pro 7.0 (Target)
    - Note: This plugin is currently not working in IDA 7.5 Pro 
  - Python 2.7 (Native to IDAPython)
  - Notepad++ (Used for developing)
    - Note PyCharm does work too, but autocomplete and weird syntax highlighting was distracting.

# Features
  - Ability to analyze any function's Packet Structure.
  - Writes down function to an output text file.
  - Writes down analyzed packet to an output text file.
  - Automatically search for all OutPacket Headers.
  - Automatically search for InPacket Structures.
  - Open any function in notepad for easier manual analysis (creates a txt file automatically).

# Note
   - The Packet Structure analysis is best left to packets that do not call any functions that will call more decodes (smaller packets would work best)
   - Opening function in Notepad will save it to a text file, located in C: Drive named `SpiritIDA`

# Instructions for Use
  - NOTE: The plugin is assuming you have all the `decode` functions named in the function you'd like to analyze (same for OutPacket).
    - If a decode function seems not to appear, you should check `init.py` and add it to KEYWORD and KEYWORD_PRINT arrays accordingly.
  - Drag the following contents of the `main` directory and drag it into `plugins` directory located in your main IDA folder.
    - ~~change _init_.py's directory constants for the image to where SpiritMS.png is (located in the `spiritms` directory).~~
    - Fixed as of commit `ff4249e2a696aa0a4cafc740b57239a59e7fa656`
  - Now run IDA and a "Succesfully Loaded message" should appear in your output window!
  - Right click functions to access the tools provided by the plugin!

# Gallery
  - Utilities:
  
  ![Function](https://github.com/Bratah123/SpiritIDAPlugin/assets/58405975/f5e721cf-61eb-4002-9762-bfcd566116c9)
  
  - Outputs:
    
    -Packet Analysis:
    
      ![Out](https://github.com/Bratah123/SpiritIDAPlugin/assets/58405975/078b5639-bade-464a-99b5-c9825f85813c)
      
    -InHeader Analysis:
    
      ![InHeader](https://github.com/Bratah123/SpiritIDAPlugin/assets/58405975/31e80460-7f8b-4dc2-a1fb-e9d9ecce2def)

    -OutPacket Info:
    
      ![OutPacket](https://github.com/Bratah123/SpiritIDAPlugin/assets/58405975/8f5cce49-9a17-4195-9ab9-4407351f8899)
    
