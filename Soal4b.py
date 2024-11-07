class DFSM:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol in self.alphabet:
                current_state = self.transition_function.get((current_state, symbol), None)
                if current_state is None:
                    return False
            else:
                return False
        return current_state in self.accept_states

# Definisi DFSM untuk string yang menerima jumlah `0` habis dibagi 5 dan jumlah `1` genap
states = {'q0_even', 'q0_odd', 'q1_even', 'q1_odd', 'q2_even', 'q2_odd', 'q3_even', 'q3_odd', 'q4_even', 'q4_odd'}
alphabet = {'0', '1'}
transition_function = {
    # q0 states (jumlah `0` habis dibagi 5)
    ('q0_even', '0'): 'q1_even', ('q0_even', '1'): 'q0_odd',
    ('q0_odd', '0'): 'q1_odd', ('q0_odd', '1'): 'q0_even',

    # q1 states
    ('q1_even', '0'): 'q2_even', ('q1_even', '1'): 'q1_odd',
    ('q1_odd', '0'): 'q2_odd', ('q1_odd', '1'): 'q1_even',

    # q2 states
    ('q2_even', '0'): 'q3_even', ('q2_even', '1'): 'q2_odd',
    ('q2_odd', '0'): 'q3_odd', ('q2_odd', '1'): 'q2_even',

    # q3 states
    ('q3_even', '0'): 'q4_even', ('q3_even', '1'): 'q3_odd',
    ('q3_odd', '0'): 'q4_odd', ('q3_odd', '1'): 'q3_even',

    # q4 states
    ('q4_even', '0'): 'q0_even', ('q4_even', '1'): 'q4_odd',
    ('q4_odd', '0'): 'q0_odd', ('q4_odd', '1'): 'q4_even',
}

start_state = 'q0_even'
accept_states = {'q0_even'}

# Buat DFSM
dfsm = DFSM(states, alphabet, transition_function, start_state, accept_states)

# Input dari user
input_string = input("Masukkan string biner (0, 1): ")

# Cek apakah string diterima
if dfsm.accepts(input_string):
    print(f"String '{input_string}' diterima oleh DFSM.")
else:
    print(f"String '{input_string}' tidak diterima oleh DFSM.")
