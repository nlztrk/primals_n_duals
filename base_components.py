###################################
##  SMART CITIES CHAPTER 7 CODE  ##
###################################
######## Component Library ########
###################################
# Anil Ozturk # Fidan Khalilbayli #
###################################

import cv2  
import numpy as np
import sys
from numpy import linalg as LA
np.set_printoptions(edgeitems=30, threshold=sys.maxsize, linewidth=500)

class Node:
    def __init__(self, pos_x, pos_y, connected_lines):
        self.x = pos_x
        self.y = pos_y
        self.size = len(connected_lines)*6
        self.connected_lines = connected_lines

class Line:
    def __init__(self, start_x, start_y, end_x, end_y, connected_nodes):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.size = len(connected_nodes)
        self.connected_nodes = connected_nodes

class Network:
    def __init__(self):
        self.nodes = []
        self.lines = []
        self.print_offset = 150
        self.desired_size = 850

    def create_node(self, pos, connected_lines):
        self.nodes.append(Node(pos[0], pos[1], connected_lines))

    def get_connected_nodes(self):
        new_id = len(self.lines)
        connected_nodes = []
        for i, node in enumerate(self.nodes):
            if node.connected_lines.count(new_id)>0:
                connected_nodes.append(i)
        return connected_nodes

    def create_line(self, start, end):
        self.lines.append(Line(start[0], start[1], end[0], end[1], self.get_connected_nodes()))

    def print_node(self, node, img, show, weighted):

        if (show == "nodes" or show == "all"):
            if weighted:
                cv2.circle(img, (int(node.x), int(node.y)), int(node.size), (255,255,255), -1)
            else:
                cv2.circle(img, (int(node.x), int(node.y)), 5, (255,255,255), -1)
        else:
            cv2.circle(img, (int(node.x), int(node.y)), 1, (255,255,255), -1)

        return img

    def print_line(self, line, img, show, weighted):

        if (show == "lines" or show == "all"):
            if weighted:
                cv2.line(img, (int(line.start_x), int(line.start_y)), (int(line.end_x), int(line.end_y)), (255,255,255), int(line.size)) 
            else:
                cv2.line(img, (int(line.start_x), int(line.start_y)), (int(line.end_x), int(line.end_y)), (255,255,255), 4) 
        else:
            cv2.line(img, (int(line.start_x), int(line.start_y)), (int(line.end_x), int(line.end_y)), (255,255,255), 1) 
        return img

    def show_network(self, show="lines", weighted=False):

        img = np.zeros((self.desired_size,self.desired_size,3), np.uint8)

        for node in self.nodes:
            img = self.print_node(node, img, show, weighted)

        for line in self.lines:
            img = self.print_line(line, img, show, weighted)

        cv2.imshow("Network", img)
        k = cv2.waitKey(0)
        if k==27:    # Esc key to stop
            return

    def generate_aij_matrix(self):
        aij = np.zeros((len(self.lines)+1, len(self.nodes)+1))

        for i, node in enumerate(self.nodes):
            for j in node.connected_lines:
                aij[j,i] = 1
        
        aij[-1,:] = aij.sum(axis=0)
        aij[:,-1] = aij.sum(axis=1)

        return aij


    def autoscale_network(self):

        min_x = 100000
        max_x = 0
        min_y = 100000
        max_y = 0

        top_left_node_id = 0
        top_left_curr_dist = 100000

        # FINDING MIN AND MAX COORDINATES FOR BOTH AXES
        for i, node in enumerate(self.nodes):
            x, y = node.x, node.y
            dist = LA.norm([x,y])
            
            if dist<top_left_curr_dist:
                top_left_curr_dist = dist
                top_left_node_id = i

            if x<min_x:
                min_x = x
            if x>max_x:
                max_x = x
            if y<min_y:
                min_y = y
            if y>max_y:
                max_y = y

        x_gap = max_x-min_x
        y_gap = max_y-min_y
        max_gap = max(x_gap, y_gap)

        ## CENTERIZING-SHIFTING OPERATION
        ## first taking them to the top-left, then centerizing based on maximum gap calc

        topleft_x = min_x
        topleft_y = min_y

        for i in range(len(self.nodes)):
            rel_x = self.nodes[i].x - topleft_x
            rel_y = self.nodes[i].y - topleft_y

            if max_gap == x_gap:
                self.nodes[i].x = int(rel_x*max_gap/x_gap)
                self.nodes[i].y = int(rel_y + (max_gap/2 - y_gap/2))

            if max_gap == y_gap:
                self.nodes[i].y = int(rel_y*max_gap/y_gap)
                self.nodes[i].x = int(rel_x + (max_gap/2 - x_gap/2))

        for i in range(len(self.lines)):
            rel_sx = self.lines[i].start_x - topleft_x
            rel_sy = self.lines[i].start_y - topleft_y
            rel_ex = self.lines[i].end_x - topleft_x
            rel_ey = self.lines[i].end_y - topleft_y

            if max_gap == x_gap:
                self.lines[i].start_x = int(rel_sx*max_gap/x_gap)
                self.lines[i].start_y = int(rel_sy + (max_gap/2 - y_gap/2))
                self.lines[i].end_x = int(rel_ex*max_gap/x_gap)
                self.lines[i].end_y = int(rel_ey + (max_gap/2 - y_gap/2))

            if max_gap == y_gap:
                self.lines[i].start_y = int(rel_sy*max_gap/y_gap)
                self.lines[i].start_x = int(rel_sx + (max_gap/2 - x_gap/2))
                self.lines[i].end_y = int(rel_ey*max_gap/y_gap)
                self.lines[i].end_x = int(rel_ex + (max_gap/2 - x_gap/2))

        ## SCALING OPERATION
        scale_ratio = (self.desired_size - self.print_offset) / max_gap

        for i in range(len(self.nodes)):
            self.nodes[i].x *= scale_ratio
            self.nodes[i].y *= scale_ratio
            self.nodes[i].size *= scale_ratio

        for i in range(len(self.lines)):
            self.lines[i].start_x *= scale_ratio
            self.lines[i].start_y *= scale_ratio
            self.lines[i].end_x *= scale_ratio
            self.lines[i].end_y *= scale_ratio
            self.lines[i].size *= scale_ratio

        ## OFFSET OPERATION
        for i in range(len(self.nodes)):
            self.nodes[i].x += self.print_offset/2
            self.nodes[i].y += self.print_offset/2

        for i in range(len(self.lines)):
            self.lines[i].start_x += self.print_offset/2
            self.lines[i].start_y += self.print_offset/2
            self.lines[i].end_x += self.print_offset/2
            self.lines[i].end_y += self.print_offset/2
