
# Virtual Quantum Error Detection #

Our paper presents a novel approach called virtual quantum error detection (VQED),
which enables the extraction of computational outcomes from a quantum circuit based
on error detection results. Although VQED implies the detection of quantum errors, it
is primarily used as a quantum error mitigation technique to reduce noise in quantum
circuits. The paper begins with a brief overview of stabilizer formalism, followed by
an introduction to syndrome measurement, a widely used technique for quantum error
detection. Given the considerable overhead associated with syndrome measurement due
to the computation required on each stabilizer, we subsequently introduce symmetry
expansion, an effective quantum error mitigation strategy. The significance of VQED lies
in its ability to generalize the symmetry expansion method, allowing for efficient error
detection without the need for executing syndrome measurements.

## Overview ##

- syndrome_measurement.ipynb: Performs syndrome measurement to detect errors within quantum circuits. The current circuit detects bit-flip errors on three logical qubits.   
- symmetry_expansion.ipynb: Performs symmetry expansion as described within the paper to mitigate noise in quantum circuits. Given a generic density matrix, noise is applied which is then mitigated by projecting the result back into the noiseless codespace.
- VQED.ipynb: Performs Virtual Quantum Error Detection as described in the report (Found in virtual_quantum_error_detection.pdf).
- numerical_simulation.ipynb: Performs numerical analysis and simulation of the methods described in the paper. NOTE: this file will encounter an error when trying to replicate the full results of the paper due to limitations of the pennylane mixed.state device.
- helper_functions.ipynb: Contains helper functions common each of the notebooks to create a generator set and density matrix. 
- stabilizer.py: Contains helper functions for generating stabilizer codes used within the papers numerical results and building stabilizer groups.
- verification.ipynb: Contains code from exploration into the theory of the paper to better understand the major error mitigation methods described within the paper. 

## Report ##

A supplementary report that describes the work in reproducing the virtual quantum error detection can be found in 400Q_Report.pdf

## User Guide ##

Each method described within the paper has been modularized into files for ease of use and readibility. To run the files follow the procedure below:

1. Intall the latest version of Pennylane (0.29.0)
    - This can be checked with the qml.version() command
2. Install the latest version of numpy
3. Clone or Fork the repository
4. To run any of the notebooks:
    - Clear all outputs
    - Ensure that the python helper function files are located within the same directory
    - Execute the notebook cells in order starting from the beginning


## Contributions:
- Andrea Shao
- Joshua Yellowley
    - Collaborated and pair-programmed the circuits for syndrome measurement and virtual quantum error detection. Reformatted code from a larger main file into individual files per method with relevant documentation and equations from the paper.
- Marco Ser
    - Worked on coding the initial circuits for syndrome measurements and symmetry expansion. Referenced several other papers to find useful examples of stabliizer formalisms. Also wrote verification.ipynb to help us verify equations in the paper to help strengthen our understanding.
- Trevor Flanigan
    - Worked on VQED.ipynb, stabilizer.py, and general understanding of processes in paper, especially regarding stabilizer formalism
