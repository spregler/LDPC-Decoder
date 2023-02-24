import numpy as np


MAX_ITER = 10
# Parity check matrix
H = np.array([
    [1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,1,1,0,1,1,0],
    [0,0,1,1,1,0,1,0,1,1],
    [0,1,0,1,1,1,0,1,0,1],
    [1,1,0,1,0,0,1,1,1,0],
], dtype=float)


# Input: {parity check matrix, max_iter} 
# Output: {Codeword estimate}
def ldpc_decoder(received_codeword, max_iter):

    # Initialize messages from Vn to Cm using channel log-likelihood ratios
    llr = -2*received_codeword # Calculate channel poseterior LLRs
    init_V_C = np.array([row*llr for row in H])

    iter_count = 0
    C_V_mat = H
    V_C_mat = init_V_C
    llr_out = np.zeros(H.shape[1])
    cout = np.zeros(H.shape[1])

    while iter_count < max_iter:
        # Check node to variable node step (Horizontal Step)
        for row_idx, check_node_m in enumerate(V_C_mat):
            v_nodes = np.where(check_node_m != 0)[0] # Variable nodes with edges connected to current check node
            # For each variable node
            for current_vnode in v_nodes: 
                # Set of variable nodes except for current variable node     
                other_vnodes = np.delete(v_nodes, np.where(v_nodes == current_vnode))
                # Compute message from check node to current variable node
                message = 2*np.arctanh(np.product([np.tanh(check_node_m[i]/2) for i in other_vnodes]))

                # Copy message to Check-to-Variable matrix
                C_V_mat[row_idx][current_vnode] = message

        # Variable node to check node step (Vertical Step)
        for col_idx, v_node_n in enumerate(C_V_mat.T): #col index is n          
            c_nodes = np.where(v_node_n != 0)[0] # Check nodes with edges connected to current variable node
            # For each check node
            for current_cnode in c_nodes:  
                # Set of check nodes except for current check node
                other_cnodes = np.delete(c_nodes, np.where(c_nodes == current_cnode))
                # Compute message from variable node to current check node
                message =  np.sum([v_node_n[i] for i in other_cnodes]) + llr[col_idx]
                # Compute LLR
                message_llr_out = np.sum([v_node_n[i] for i in c_nodes]) + llr[col_idx]

                # Copy message to Variable-to-Check matrix and LLR output array
                V_C_mat.T[col_idx][current_cnode] = message
                llr_out[col_idx] = message_llr_out

        iter_count += 1
        print("llr output of iter {}: \n".format(iter_count), llr_out)
        print("\n")

        # Threshold test: If llr < 0 bit = 1 else bit = 0
        cout = [1 if llr_out[n] < 0 else 0 for n in range(H.shape[1])]
    
    return cout


if __name__ == "__main__":
    b = np.array([0,0,0,1,0,1,0,1,0,1]) # Encoded message vector (from example)
    y = np.array([-0.63, -0.83, -0.73, -0.04, 0.1, 0.95, -0.76, 0.66, -0.55, 0.58]) # Encoded message through AWGN channel (from example)

    out = ldpc_decoder(y,MAX_ITER)
    print(out)
    print("Hello_world")
