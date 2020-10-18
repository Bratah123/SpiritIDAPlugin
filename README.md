# SpiritIDAPlugin
This Plugin utilizes the business logic from [MaplePacketPuller](https://github.com/Bratah123/MaplePacketPuller) project and therefore inherits any features or known problems from it.


Author: Brandon Nguyen

Any questions relating to setup or any errors can be redirected to `Not Brandon #4444`.


# Features
  - Ability to analyze any function's Packet Structure.
  - Writes down function to an output text file.
  - Writes down analyzed packet to an output text file.
  - Automatically search for all OutPacket Headers.
  - Automatically search for InPacket Structures.
  - Open any function in notepad for easier manual analysis (creates a txt file automatically).

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
  
  ![Functions](https://cdn.discordapp.com/attachments/631249406775132182/766328981460877322/6116524528cc2708c4f76d8727294831.png)
  
  - Outputs:
    
    -Packet Analysis:
    
      ![Out](https://cdn.discordapp.com/attachments/746519006961336370/765372958281170944/f982f56456131a78fb51a885d622f842.png)
      
    -InHeader Analysis:
    
      ![InHeader](https://cdn.discordapp.com/attachments/746519006961336370/765373302822273074/6ba9043852813e3dd132dd7ce22b822d.png)
      
    -OutPacket Info:
    
      ![OutPacket](https://cdn.discordapp.com/attachments/746519006961336370/765373520351723520/429e755fe5f3c7d7a6ac558a1a340747.png)
    
    
