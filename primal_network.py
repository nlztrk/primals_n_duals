###################################
##  SMART CITIES CHAPTER 7 CODE  ##
###################################
######## PrimalNet Library ########
###################################
# Anil Ozturk # Fidan Khalilbayli #
###################################

import cv2  
import numpy as np

class PrimalNetwork:
    def __init__(self, network, step_count):
        self.nodes = network.nodes
        self.lines = network.lines
        self.print_offset = network.print_offset
        self.desired_size = network.desired_size
        self.step_count = step_count
        self.adjust_primals()

    def recursive_step_func(self, line, i, step, connected_lines):
        
        for connected_node in line.connected_nodes: # getting connected nodes of the line
            for connected_line in self.nodes[connected_node].connected_lines: # getting connected lines of that node (1-step evaluation)
                if (connected_line != i and connected_lines.count(connected_line)==0): # if the connected line of that node isn't this node
                    if step>self.step_count: return connected_lines
                    connected_lines.append(connected_line) # append that line into the connected lines of this line    
                    connected_lines = self.recursive_step_func(self.lines[connected_line], i, step+1, connected_lines)

        return connected_lines

    def adjust_primals(self):

        for i, line in enumerate(self.lines):
            self.lines[i].center_x = (line.start_x + line.end_x) / 2
            self.lines[i].center_y = (line.start_y + line.end_y) / 2
            connected_lines = []
            step = 1

            connected_lines = self.recursive_step_func(line, i, step, connected_lines)

            self.lines[i].connected_lines = connected_lines

    def print_primal_lines(self, img):

        for line_1 in self.lines:
            for line_2 in line_1.connected_lines:
                line_2 = self.lines[line_2]
                cv2.line(img, (int(line_1.center_x), int(line_1.center_y)), (int(line_2.center_x), int(line_2.center_y)), (255,255,255), 1) 

        for line in self.lines:
            cv2.circle(img, (int(line.center_x), int(line.center_y)), 7, (255,255,255), -1)
            cv2.circle(img, (int(line.center_x), int(line.center_y)), 5, (0,0,0), -1)

        return img

    def show_network(self):

        img = np.zeros((self.desired_size,self.desired_size,3), np.uint8)

        img = self.print_primal_lines(img)

        cv2.imshow("Primal Network ("+str(self.step_count)+"-step)", img)
        k = cv2.waitKey(0)
        if k==27:    # Esc key to stop
            return
