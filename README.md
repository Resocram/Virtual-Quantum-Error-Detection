
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