from framework import *
from math import *


def oracle(qubits, set=(True, True)):
    q1, q2 = qubits

    # target 11
    q2.superpose()
    q1.cx(q2)
    q2.superpose()

    set1, set2 = set
    if set1: q1.x()
    if set2: q2.x()


def inversion(qubits):
    q2.superpose()
    q1.cx(q2)
    q1.superpose()


def grover(qubits, n):
    for q in qubits:
        q.superpose()
    for i in range(int(sqrt(n))):
        oracle(qubits)
        Qubit.draw(f"Iteration {i} after oracle")
        inversion(qubits)
        Qubit.draw(f"Iteration {i} after inversion")
    Qubit.measure((0, 1), (0, 1))


def to_binary(number):
    n = ceil(log(number, 2))+1 if number > 0 else 1
    binary = tuple(number % (2**i) == 0 for i in range(n, 1))
    return binary


if __name__ == '__main__':
    test_list = [0, 0, 0, 0, 1, 0, 0, 0, 0]  # n = nine
    build_circuit(2, 2)
    q1 = Qubit()
    q2 = Qubit()
    grover((q1, q2), 1)
    result = get_result()
    print(result.get_counts())