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
states = {('q0', 'even'), ('q0', 'odd'), ('q1', 'even'), ('q1', 'odd'), ('q2', 'even'), ('q2', 'odd')}
alphabet = {'0', '1'}
transition_function = {
    (('q0', 'even'), '0'): ('q1', 'even'), (('q0', 'even'), '1'): ('q0', 'odd'),
    (('q0', 'odd'), '0'): ('q1', 'odd'), (('q0', 'odd'), '1'): ('q0', 'even'),
    
    (('q1', 'even'), '0'): ('q2', 'even'), (('q1', 'even'), '1'): ('q1', 'odd'),
    (('q1', 'odd'), '0'): ('q2', 'odd'), (('q1', 'odd'), '1'): ('q1', 'even'),
    
    (('q2', 'even'), '0'): ('q0', 'even'), (('q2', 'even'), '1'): ('q2', 'odd'),
    (('q2', 'odd'), '0'): ('q0', 'odd'), (('q2', 'odd'), '1'): ('q2', 'even')
}
start_state = ('q0', 'even')
accept_states = {('q0', 'even')}

# Buat DFSM
dfsm = DFSM(states, alphabet, transition_function, start_state, accept_states)

# Menerima input dari pengguna
input_string = input("Masukkan string biner (0, 1): ")

# Cek apakah string diterima atau tidak
if dfsm.accepts(input_string):
    print(f"String '{input_string}' diterima oleh Mesin.")
else:
    print(f"String '{input_string}' tidak diterima oleh Mesin.")
