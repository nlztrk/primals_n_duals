###################################
##  SMART CITIES CHAPTER 7 CODE  ##
###################################
######### DualNet Library #########
###################################
# Anil Ozturk # Fidan Khalilbayli #
###################################

import cv2  
import numpy as np

class DualNetwork:
    def __init__(self, network, step_count):
        self.nodes = network.nodes
        self.lines = network.lines
        self.print_offset = network.print_offset
        self.desired_size = network.desired_size
        self.step_count = step_count
        self.adjust_duals()

    def recursive_step_func(self, node, i, step, connected_nodes):
        
        for connected_line in node.connected_lines: # getting connected nodes of the line
            for connected_node in self.lines[connected_line].connected_nodes: # getting connected lines of that node (1-step evaluation)
                if (connected_node != i and connected_nodes.count(connected_node)==0): # if the connected line of that node isn't this node
                    if step>self.step_count: return connected_nodes
                    connected_nodes.append(connected_node) # append that line into the connected lines of this line    
                    connected_nodes = self.recursive_step_func(self.nodes[connected_node], i, step+1, connected_nodes)

        return connected_nodes

    def adjust_duals(self):

        for i, node in enumerate(self.nodes):

            connected_nodes = []
            step = 1

            connected_nodes = self.recursive_step_func(node, i, step, connected_nodes)

            self.nodes[i].connected_nodes = connected_nodes

    def print_dual_nodes(self, img):

        for node_1 in self.nodes:
            for node_2 in node_1.connected_nodes:
                node_2 = self.nodes[node_2]
                cv2.line(img, (int(node_1.x), int(node_1.y)), (int(node_2.x), int(node_2.y)), (255,255,255), 1) 

        for node in self.nodes:
            cv2.circle(img, (int(node.x), int(node.y)), 7, (255,255,255), -1)
            cv2.circle(img, (int(node.x), int(node.y)), 5, (0,0,0), -1)

        return img

    def show_network(self):

        img = np.zeros((self.desired_size,self.desired_size,3), np.uint8)

        img = self.print_dual_nodes(img)

        cv2.imshow("Dual Network ("+str(self.step_count)+"-step)", img)
        k = cv2.waitKey(0)
        if k==27:    # Esc key to stop
            return
