from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram

# Step1 함수 : Hadamard Gate 통과(균등하게 확률을 분배시키는 함수)
def init(n) :
    circuit = QuantumCircuit(n + 1)
    for i in range(n):
        circuit.h(i) # 모든 큐비트에 하다마드 게이트 통과시킴
    circuit.x(n) #마지막 큐비트에 파울리(Pauli) X게이트 통과시킴
    circuit.h(n) #마지막 큐비트에 하다마드 게이트를 통과시킴
    return circuit

# Step2 함수 : Oracle 함수(위상을 반전시키는 함수)
def oracle(n, x)# 몇개의 비트냐, 찾고자하는 값은 무엇이냐?
    circuit = QuantumCircuit(n + 1)
    for i in range(n)
        if x & (1 << i) == 0: 
            circuit.x(i) #모든 큐비트에 파울리(Pauli) X게이트 통과시킴
    if n==2:
        circuit.ccx(0, 1, 2) #토폴리 CCX 게이트 통과시킴 
    for i in range(n):
        if x & (1 << i) == 0 :
            circuit.x(i) #모든 큐비트에 다시 파울리(Pauli) X게이트 통과시킴
    return circuit

# Step3 함수 : Diffusion게이트를 증폭시키는 함수
def diffusion(n, x)
    circuit = QuantumCircuit(n + 1)
    for i in range(n):
        circuit.h(i) #모든 큐비트에 하다마드 게이트 통과시킴
        circuit.x(i) #모든 큐비트에 파울리(Pauli) X 게이트 통과시킴
    if n == 2 :
        circuit.h(1) #두번째 큐비트에 하다마드 게이트 통과시킴
        circuit.cx(0, 1) #두번째 큐비트에 제어 파울리 Controlled-X 게이트 통과시킴
        circuit.h(1) #두번째 큐비트에 하다마드 게이트 통과시킴
    for i in range(n):
        # 첫 반복문과 대칭구조 h,x >> x,h
        circuit.x(i) #모든 큐비트에 파울리(Pauli) X 게이트 통과시킴
        circuit.h(i) #모든 큐비트에 하다마드 게이트 통과시킴
    return circuit
    
# 실제 그로버 알고리즘 코드
n = 2 # 큐비트가 2개이다.
x = 2 # 찾고자하는 타겟은 2이다.
circuit = QuantumCircuit(3, 2)
circuit += init(n) # 초기화 균등분배(하다마드 게이트 통과)
circuit.barrier()
circuit += oracle(n, x) # 위상을 반대로 바꿈(오라클 함수)
circuit.barrier()
circuit += diffusion(n, x) # 진폭을 증폭시킴(Diffusion게이트 통과)
circuit.barrier()
bits = [i for i in range(n)]
circuit.measure(bits, bits) # 측정
circuit.draw() # 차트 그리기

# 찾은 값 출력
backend = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend).result()
counts = result.get_counts()
print(counts)