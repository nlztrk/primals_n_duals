###################################
##  SMART CITIES CHAPTER 7 CODE  ##
###################################
########### Main Script ###########
###################################
# Anil Ozturk # Fidan Khalilbayli #
###################################

from base_components import Node, Line, Network
from primal_network import PrimalNetwork
from dual_network import DualNetwork
from heatmap import plot_heatmap


example_net = Network()

example_net.create_node(pos=(0, 236), connected_lines=[0]) # Node 0
example_net.create_node(pos=(356, 118), connected_lines=[0,2]) # Node 1
example_net.create_node(pos=(435, 90), connected_lines=[0,1,3]) # Node 2
example_net.create_node(pos=(713, 59), connected_lines=[1,4]) # Node 3
example_net.create_node(pos=(822, 46), connected_lines=[1,11]) # Node 4
example_net.create_node(pos=(958, 30), connected_lines=[1]) # Node 5
example_net.create_node(pos=(0, 370), connected_lines=[8]) # Node 6
example_net.create_node(pos=(15, 383), connected_lines=[7,8]) # Node 7
example_net.create_node(pos=(303, 274), connected_lines=[2,7]) # Node 8
example_net.create_node(pos=(730, 210), connected_lines=[4,5]) # Node 9
example_net.create_node(pos=(847, 96), connected_lines=[5,6,11]) # Node 10
example_net.create_node(pos=(956, 91), connected_lines=[6,12]) # Node 11
example_net.create_node(pos=(998, 84), connected_lines=[6]) # Node 12
example_net.create_node(pos=(71, 441), connected_lines=[8,9]) # Node 13
example_net.create_node(pos=(262, 389), connected_lines=[2,9]) # Node 14
example_net.create_node(pos=(350, 372), connected_lines=[9,16]) # Node 15
example_net.create_node(pos=(435, 349), connected_lines=[3,9]) # Node 16
example_net.create_node(pos=(687, 283), connected_lines=[9,10]) # Node 17
example_net.create_node(pos=(734, 273), connected_lines=[4,9,18]) # Node 18
example_net.create_node(pos=(803, 239), connected_lines=[13]) # Node 19
example_net.create_node(pos=(969, 316), connected_lines=[11,12]) # Node 20
example_net.create_node(pos=(997, 374), connected_lines=[11,13]) # Node 21
example_net.create_node(pos=(173, 536), connected_lines=[8,14]) # Node 22
example_net.create_node(pos=(235, 475), connected_lines=[15]) # Node 23
example_net.create_node(pos=(250, 523), connected_lines=[14,15]) # Node 24
example_net.create_node(pos=(268, 584), connected_lines=[15]) # Node 25
example_net.create_node(pos=(376, 502), connected_lines=[16,17]) # Node 26
example_net.create_node(pos=(636, 438), connected_lines=[18,19]) # Node 27
example_net.create_node(pos=(563, 564), connected_lines=[17,18]) # Node 28
example_net.create_node(pos=(574, 541), connected_lines=[18,21]) # Node 29
example_net.create_node(pos=(611, 612), connected_lines=[20,21]) # Node 30
example_net.create_node(pos=(679, 564), connected_lines=[19,20]) # Node 31
example_net.create_node(pos=(350, 700), connected_lines=[8,25]) # Node 32
example_net.create_node(pos=(368, 719), connected_lines=[8]) # Node 33
example_net.create_node(pos=(414, 703), connected_lines=[16,25]) # Node 34
example_net.create_node(pos=(482, 704), connected_lines=[18,25]) # Node 35
example_net.create_node(pos=(610, 707), connected_lines=[22,25]) # Node 36
example_net.create_node(pos=(644, 682), connected_lines=[21,22]) # Node 37
example_net.create_node(pos=(707, 650), connected_lines=[19,22]) # Node 38
example_net.create_node(pos=(765, 624), connected_lines=[22,23,24]) # Node 39
example_net.create_node(pos=(789, 570), connected_lines=[24]) # Node 40
example_net.create_node(pos=(810, 626), connected_lines=[23]) # Node 41
example_net.create_node(pos=(996, 715), connected_lines=[25]) # Node 42
example_net.create_node(pos=(670, 340), connected_lines=[10]) # Node 43

example_net.create_line(start=(0, 240), end=(435,90)) # Line 0
example_net.create_line(start=(435, 90), end=(959,31)) # Line 1
example_net.create_line(start=(357, 118), end=(264,390)) # Line 2
example_net.create_line(start=(433, 90), end=(436,349)) # Line 3
example_net.create_line(start=(713, 58), end=(734,274)) # Line 4
example_net.create_line(start=(730, 210), end=(848,97)) # Line 5
example_net.create_line(start=(848, 97), end=(998,83)) # Line 6
example_net.create_line(start=(12, 382), end=(304,275)) # Line 7
example_net.create_line(start=(0, 370), end=(368, 719)) # Line 8
example_net.create_line(start=(71, 441), end=(734, 273)) # Line 9
example_net.create_line(start=(687, 283), end=(670, 340)) # Line 10
example_net.create_line(start=(822, 46), end=(997, 374)) # Line 11
example_net.create_line(start=(956, 91), end=(969, 316)) # Line 12
example_net.create_line(start=(803, 239), end=(997, 374)) # Line 13
example_net.create_line(start=(173, 536), end=(250, 523)) # Line 14
example_net.create_line(start=(235, 475), end=(268, 584)) # Line 15
example_net.create_line(start=(350, 372), end=(414, 703)) # Line 16
example_net.create_line(start=(376, 502), end=(563, 564)) # Line 17
example_net.create_line(start=(734, 273), end=(482, 704)) # Line 18
example_net.create_line(start=(636, 438), end=(707, 650)) # Line 19
example_net.create_line(start=(611, 612), end=(679, 564)) # Line 20
example_net.create_line(start=(574, 541), end=(644, 682)) # Line 21
example_net.create_line(start=(610, 707), end=(765, 624)) # Line 22
example_net.create_line(start=(765, 624), end=(810, 626)) # Line 23
example_net.create_line(start=(765, 624), end=(789, 570)) # Line 24
example_net.create_line(start=(350, 700), end=(996, 715)) # Line 25


'''
Show: 'nodes', 'lines', 'all'
Weighted: True, False
'''
example_net.autoscale_network()

aij = example_net.generate_aij_matrix()
print("Generated a_ij matrix;\n\n", aij)

example_net.show_network(show="nodes", weighted=True)
plot_heatmap(network=example_net, mode="nodes", sharpness_factor=10)

example_net.show_network(show="lines", weighted=True)
plot_heatmap(network=example_net, mode="lines", sharpness_factor=10)


# primal_net = PrimalNetwork(network=example_net, step_count = 1)
# primal_net.show_network() 

# primal_net = PrimalNetwork(network=example_net, step_count = 2)
# primal_net.show_network() 

# primal_net = PrimalNetwork(network=example_net, step_count = 3)
# primal_net.show_network() 

# dual_net = DualNetwork(network=example_net, step_count = 1)
# dual_net.show_network() 

# dual_net = DualNetwork(network=example_net, step_count = 2)
# dual_net.show_network() 

# dual_net = DualNetwork(network=example_net, step_count = 3)
# dual_net.show_network() 
