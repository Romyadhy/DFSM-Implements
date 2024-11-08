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


# Definisikan DFSM yang menerima substring "aabb"
states = {'q0', 'q1', 'q2', 'q3', 'q4'}
alphabet = {'a', 'b'}
transition_function = {
    ('q0', 'a'): 'q1',
    ('q1', 'a'): 'q2',
    ('q2', 'b'): 'q3',
    ('q3', 'b'): 'q4',
    ('q4', 'a'): 'q4',  # Keadaan akhir dapat terus menerima input
    ('q4', 'b'): 'q4'   # apa pun
}
start_state = 'q0'
accept_states = {'q4'}

# Buat DFSM
dfsm = DFSM(states, alphabet, transition_function, start_state, accept_states)

# Tes dengan beberapa string
test_strings = ["aabb", "aaaabb", "ab", "aabba", "baaabb", "aabbaa"]
for string in test_strings:
    result = dfsm.accepts(string)
    print(f"DFSM accepts '{string}': {result}")
