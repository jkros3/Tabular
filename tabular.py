class table:
    header = []
    column_widths = []
    rows = []
    center_alignment = False

    header_str = " | "
    break_line_str = " | "

    def __init__(self, header: list):
        self.header = header
        self.column_widths = [0] * len(header)
        
        #Sets the initial width of each column
        for i in range(len(self.header)):
            self.column_widths[i] = len(self.header[i])
    
    def new_row(self, data: list):
        '''Takes a list as a parameter to generate a new row for the table'''
        self.rows.append(data)

    def center_align(self, string: str, max_width: int) -> str:
        
        new_string = string
        string_length = len(string)

        if string_length == max_width:
            return new_string
        
        spacing_calc = int((max_width - string_length) / 2)
        new_string = " " * spacing_calc
        new_string += string

        return new_string
      
    def display_table(self):
        
        #Get each item of data and compare the length of it to the initial width of the column and sets the max width to the column
        for column in range(len(self.column_widths)):
            for data in range(len(self.rows)):
                self.column_widths[column] = max(self.column_widths[column], len(str(self.rows[data][column])))

        #Generate the header string for the top of the table
        if self.center_alignment:
            for item in range(len(self.header)):
                self.header_str += "{:<{}}".format(self.center_align(self.header[item], self.column_widths[item]), self.column_widths[item])
                self.header_str += " | "
        else:
            for item in range(len(self.header)):
                self.header_str += "{:<{}}".format(self.header[item], self.column_widths[item])
                self.header_str += " | "

        #Generate the break line or the line between the header and data
        for item in range(len(self.header)):
            self.break_line_str += "-" * self.column_widths[item]
            self.break_line_str += " | "
        
        print(self.header_str)
        print(self.break_line_str)
        
        if self.center_alignment:
            for row in range(len(self.rows)):
                data_index = 0
                row_string = " | "
                while data_index < len(self.rows[row]):
                    string = str(self.rows[row][data_index])
                    column_width = self.column_widths[data_index]
                    row_string += "{:<{}} | ".format(self.center_align(string, column_width), column_width)
                    data_index += 1
                print(row_string)
        else:
            for row in range(len(self.rows)):
                data_index = 0
                row_string = " | "
                while data_index < len(self.rows[row]):
                    string = str(self.rows[row][data_index])
                    column_width = self.column_widths[data_index]
                    row_string += "{:<{}} | ".format(string, column_width)
                    data_index += 1
                print(row_string)