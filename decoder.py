import numpy as np
import matplotlib.pyplot as plt
import scipy


# Parity check matrix
H = np.array([
    [1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,1,1,0,1,1,0],
    [0,0,1,1,1,0,1,0,1,1],
    [0,1,0,1,1,1,0,1,0,1],
    [1,1,0,1,0,0,1,1,1,0],
], dtype=float)

MAX_ITER = 1

b = np.array([0,0,0,1,0,1,0,1,0,1]) # Encoded message vector
y = np.array([-0.63, -0.83, -0.73, -0.04, 0.1, 0.95, -0.76, 0.66, -0.55, 0.58]) # Encoded message through AWGN channel


# Input: {parity check matrix, max_iter} 
# Output: {Codeword estimate}
def ldpc_decoder(received_codeword, max_iter):
    # Initialize messages from Vn to Cm using channel log-likelihood ratios
    llr = -2*received_codeword # Calculate channel poseterior LLRs
    init_V_C = np.array([row*llr for row in H])

    iter_count = 0
    C_V_mat = H
    V_C_mat = init_V_C


    # while iter_count < max_iter:

    # Check node to variable node step (Horizontal Step)
    for row_idx, check_node_m in enumerate(V_C_mat):

        v_nodes = np.where(check_node_m != 0)[0] # Variable nodes with edges connected to current check node
    
        for current_vnode in v_nodes:
            
            other_vnodes = np.delete(v_nodes, np.where(v_nodes == current_vnode))
            message = 2*np.arctanh(np.product([np.tanh(check_node_m[i]/2) for i in other_vnodes]))

            C_V_mat[row_idx][current_vnode] = message
    
    # Variable node to check node step (Vertical Step)
    

    return 0


# def compute_message_C_V(messages_variable_to_check):
#     v_nodes = 
#     message_C_V = 
#     return 0



print(ldpc_decoder(y,MAX_ITER))

