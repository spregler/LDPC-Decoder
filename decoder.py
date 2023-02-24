import numpy as np
import matplotlib.pyplot as plt
import scipy


# Parity check matrix
H = np.array([
    [1,1,1,0,0,1,1,0,0,1],
    [1,0,1,0,1,1,0,1,1,0],
    [0,0,1,1,1,0,1,0,1,1],
    [0,1,0,1,1,1,0,1,0,1],
    [1,1,0,1,0,0,1,1,1,0]
])

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
    while iter_count < max_iter:

        # Check node to variable node step
        for check_node_m in C_V_mat:
            for variable_node_n in np.where(check_node_m != 0):
                C_V_mat[check_node_m][variable_node_n] = compute_message_C_V(V_C_mat[check_node_m])
                






    return 0


def compute_message_C_V(messages_variable_to_check):
    v_nodes = 
    message_C_V = 
    return 0



print(ldpc_decoder(y,MAX_ITER))

