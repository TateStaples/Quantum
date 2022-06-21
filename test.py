from framework import *

if __name__ == '__main__':
    build_circuit(1, 1)
    q1 = Qubit()
    Qubit.draw("default")
    q1.superpose()
    Qubit.draw("superposed")
    q1.rotate(direction='rz')
    Qubit.draw("rz")
    q1.rotate(direction='ry')
    Qubit.draw("ry")
    q1.root()
    Qubit.draw("root")

