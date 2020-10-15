from spiritms import FUNC_DIR, FUNC_OUT_DIR, KEYWORDS, KEYWORDS_PRINT
from spiritms.Util import Util
import time
import idaapi

class PacketAnalysis(idaapi.action_handler_t):
    """
        Same functionality as MaplePacketPuller Logic
        on github github.com/bratah123
    """

    def __init__(self):
        idaapi.action_handler_t.__init__(self)
        self._txt_file_name = ""
        self._packet_struct = ""
    
    
    def activate(self, ctx):
        self.run()
        return 1
    
        
    def update(self, ctx): # Always Avaliable
        return idaapi.AST_ENABLE_ALWAYS
    
    def write_func_output(self):
        with open(FUNC_OUT_DIR + "/{}Out.txt".format(self.txt_file_name), "w") as f:
            f.write(self.packet_struct)
    
    
    def assign_txt_file(self):
        self.txt_file_name = Util.create_func_name()
    
    
    def write_func_input(self):
        self.assign_txt_file()
        with open(FUNC_DIR + "/{}.txt".format(self.txt_file_name), "w") as f:
        
            decompiled_func = Util.get_decompiled_func()
            full_func = ""
            
            for line in decompiled_func:
                full_func += line + "\n"
            
            f.write(full_func)
    
    
    def beautify(self):
        with open("{}/{}Out.txt".format(FUNC_OUT_DIR, self.txt_file_name), "r") as f:
            file_list = f.readlines()
            return [s.rstrip('\n') for s in file_list]
    
    
    def get_func_name(self):
        with open("{}/{}.txt".format(FUNC_DIR, self.txt_file_name), "r") as f:
            name = f.readline()
            return name
    
    
    @property
    def txt_file_name(self):
        return self._txt_file_name
        
        
    @txt_file_name.setter
    def txt_file_name(self, x):
        self._txt_file_name = x
        
    
    @property
    def packet_struct(self):
        return self._packet_struct
        
    
    @packet_struct.setter
    def packet_struct(self, x):
        self._packet_struct = x
    
    
    def analyze_packet_structure(self):
    
        packet_struct = ""
        
        start_time = time.time()
        
        func_name = self.get_func_name()
        packet_struct += func_name
        
        in_if_statement = False
        
        arr_index = 0
        
        f = open("{}/{}.txt".format(FUNC_DIR, self.txt_file_name), "r")
        file = f.readlines()
        line_index = 0
        length_of_file = len(file)
        while line_index < length_of_file:
            line = file[line_index]
            decodes_in_if = []
            if_or_else = ""
            lines_to_skip = 0
            # It would prob be easier to print the line like it is in the txt file as it is already spaced
            if KEYWORDS[5] in line or KEYWORDS[6] in line:  # check if we are at an if / else statement
                if KEYWORDS[5] in line:
                    if_or_else += "if " + Util.check_keyword_and_return(line, False) + ":"
                if KEYWORDS[6] in line:
                    if_or_else += "else:"
                    
                check_next_line = file[arr_index + 1] == "  {\n"  # check if its a non nested if
                
                if not check_next_line:
                    decodes_in_if = Util.add_decode_to_list(decodes_in_if,
                                                            Util.check_keyword_and_return(file[arr_index + 1], False))
                    if len(decodes_in_if) > 0:
                        check_next_line = True
                        lines_to_skip += 2
                elif check_next_line:  # if we are in the scope of an if, find when it ends
                    i = 1
                    while file[arr_index + i] != "  }\n":
                        decodes_in_if = Util.add_decode_to_list(decodes_in_if, file[arr_index + i])
                        lines_to_skip += 1
                        i += 1
                    lines_to_skip += 1
                in_if_statement = check_next_line

            if len(decodes_in_if) > 0 and in_if_statement:
                packet_struct += if_or_else + "\n"
                for decode in decodes_in_if:
                    packet_struct += "  " + decode + "\n"
                line_index += lines_to_skip
            elif Util.check_keyword_and_print(line, False):  # if we aren't in an if statement print out the decodes normally
                packet_struct += Util.check_keyword_and_return(line, False) + "\n"
                line_index += 1

            arr_index = line_index

        end_time = time.time()
        print("[SPIRIT] Finished analysis in {} seconds!".format(end_time - start_time))
        f.close()
        self.packet_struct = packet_struct
        return packet_struct
        
        
    def run(self):
        """
        Function that executes all steps needed
        to analyze these packets!
        """
        # function that assigns a func name to txt file
        Util.clear_output_window()
        self.write_func_input()
        self.analyze_packet_structure()  # this will auto-assign the packet_struct property

        print("[SPIRIT] Saving down packet structure to {}Out.txt \n".format(self.txt_file_name.upper()))
        print("--------------------------------------------------")
        self.write_func_output()

        packet_struct_arr = self.beautify()

        write_output = ""
        for word in packet_struct_arr:  # re adds all the strings to make it cleaner
            if word != '':
                write_output += "{}\n".format(word)

        beautified_arr = write_output.split("\n")

        clean_output = ""
        beautified_len = len(beautified_arr)

        for i in range(beautified_len):  # removes all empty do while() with no decodes inside them
            if beautified_arr[i] == "do:" and beautified_arr[i + 1] == "while()":
                beautified_arr[i] = ''
                beautified_arr[i + 1] = ''
            if beautified_arr[i] == "  do:" and beautified_arr[i + 1] == "  while()":
                beautified_arr[i] = ''
                beautified_arr[i + 1] = ''

        for i in range(beautified_len):
            # checking for any contents inside a do while loop and spacing them out for visual aesthetics
            if beautified_arr[i] == "do:":
                j = i + 1
                while beautified_arr[j] != "while()":
                    beautified_arr[j] = "  {}".format(beautified_arr[j])
                    j += 1
            # some functions, this will cause an index out of range error (comment out this part if so)
            try:
                if beautified_arr[i] == "  do:":
                    j = i + 1
                    while beautified_arr[j] != "  while()":
                        beautified_arr[j] = "   {}".format(beautified_arr[j])
                        j += 1
            except Exception as e:
                print("Some error occured, but it shouldn't affect the decodes() just has to do with aesthetics:", e)

        for word in beautified_arr:  # re adds all the strings after removing do while()
            if word != '':
                clean_output += "{}\n".format(word)

        self.packet_struct = clean_output # set packet_struct to the new clean output for the rewrite
        print("[SPIRIT] Cleaned-up packet structure: \n")
        print(clean_output)
        print("\n[SPIRIT] Finished Packet Analysis!")
        self.write_func_output()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        