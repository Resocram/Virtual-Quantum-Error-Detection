import pennylane as qml
import numpy as np

# Create an arbitrary density matrix 
def generate_density_matrix():
    c1 = 1/np.sqrt(2)
    c2 = 1/np.sqrt(2)
    state = np.array([c1, 0, 0, 0, 0, 0, 0, c2])
    rho = np.outer(state, np.conj(state).T)
    # End result should have trace(rho) = 1
    return rho

# We want to create a generator set <Z1Z2, Z2Z3> to detect bit flip errors.  
# We found the following generator set by referencing http://mmrc.amss.cas.cn/tlb/201702/W020170224608149940643.pdf
def create_generators():
    # Create a generator set <Z1Z2, Z2Z3> by apply PauliZ to those wires 
    G1 = qml.Identity(0) @ qml.PauliZ(1) @ qml.PauliZ(2)
    G2 = qml.PauliZ(0) @ qml.PauliZ(1) @ qml.Identity(2)

    G1 = G1.matrix()
    G2 = G2.matrix()
    return [G1, G2]


