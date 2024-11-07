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


# Definisikan DFSM yang menerima string dengan 0 habis dibagi 3 dan 1 genap
states = {
    'q0_even', 'q0_odd', 'q1_even', 'q1_odd', 
    'q2_even', 'q2_odd'
}
alphabet = {'0', '1'}
transition_function = {
    # q0 states (1's count mod 3 == 0)
    ('q0_even', '0'): 'q0_odd', ('q0_even', '1'): 'q1_even',
    ('q0_odd', '0'): 'q0_even', ('q0_odd', '1'): 'q1_odd',

    # q1 states (1's count mod 3 == 1)
    ('q1_even', '0'): 'q1_odd', ('q1_even', '1'): 'q2_even',
    ('q1_odd', '0'): 'q1_even', ('q1_odd', '1'): 'q2_odd',

    # q2 states (1's count mod 3 == 2)
    ('q2_even', '0'): 'q2_odd', ('q2_even', '1'): 'q0_even',
    ('q2_odd', '0'): 'q2_even', ('q2_odd', '1'): 'q0_odd',
}

start_state = 'q0_even'
accept_states = {'q0_even'}
# Buat DFSM
dfsm = DFSM(states, alphabet, transition_function, start_state, accept_states)

# Menerima input dari pengguna
input_string = input("Masukkan string biner (0, 1): ")

# Cek apakah string diterima atau tidak
if dfsm.accepts(input_string):
    print(f"String '{input_string}' diterima oleh Mesin.")
else:
    print(f"String '{input_string}' tidak diterima oleh Mesin.")



