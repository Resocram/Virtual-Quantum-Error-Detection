import pennylane as qml
import numpy as np

def get_pauli_generator(pauli_word):
  return qml.pauli.PauliWord({k:v for k, v in enumerate(pauli_word)}).to_mat([i for i in range(len(pauli_word))])

def get_4_1_2():
  G1 = get_pauli_generator("XXXX")
  G2 = get_pauli_generator("ZZZZ")
  G3 = get_pauli_generator("IZZI")
  Z_L = get_pauli_generator("ZZII")
  X_L = get_pauli_generator("IXXI")
  return [G1, G2, G3, Z_L, X_L]

def get_5_1_3():
  G1 = get_pauli_generator("XZZXI")
  G2 = get_pauli_generator("IXZZX")
  G3 = get_pauli_generator("XIXZZ")
  G4 = get_pauli_generator("ZXIXZ")
  Z_L = get_pauli_generator("ZZZZZ")
  X_L = get_pauli_generator("XXXXX")
  return [G1, G2, G3, G4, Z_L, X_L]

def get_7_1_3():
  G1 = get_pauli_generator("IIIZZZZ")
  G2 = get_pauli_generator("IZZIIZZ")
  G3 = get_pauli_generator("ZIZIZIZ")
  G4 = get_pauli_generator("IIIXXXX")
  G5 = get_pauli_generator("IXXIIXX")
  G6 = get_pauli_generator("XIXIXIX")
  Z_L = get_pauli_generator("ZZZZZZZ")
  X_L = get_pauli_generator("XXXXXXX")
  return [G1, G2, G3, G4, G5, G6, Z_L, X_L]

def get_stabilizers(G_list):
  def find_subsets_of_indices(index_list):
    index_subsets = []
    dfs_subset_helper(index_list, [], index_subsets)
    return index_subsets[1:] # first is always empty set
    
  def dfs_subset_helper(index_list, path, index_subsets):
      index_subsets.append(path)
      for i in range(len(index_list)):
          dfs_subset_helper(index_list[i+1:], path+[index_list[i]], index_subsets)

  def create_stabilizer_subset(index_list, G_list):
      ans = []
      for index_set in index_list:
          stabilizer_group = G_list[index_set[0]]
          for i in range(1, len(index_set)):
              next_stabilizer = G_list[index_set[i]]
              stabilizer_group = stabilizer_group @ next_stabilizer
          ans.append(stabilizer_group)
      
      ans.append(np.eye(G_list[0].shape[0]))
      return ans

  index_subsets = find_subsets_of_indices(list(range(len(G_list))))

  return create_stabilizer_subset(index_subsets, G_list)