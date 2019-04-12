import state
import io
import streamreader

# using backtracking search to build an NFA

class NFAStateMachine:

    def __init__(self, states, startStateId, classes):
        self.states = states
        self.startStateId = startStateId
        self.classes = classes

        for stateId in self.states:
            self.states[stateId].setClasses(classes)

    def accepts(self, strm):
        def acceptsSuffix(stateId):

            if (stateId, strm.numCharsRead()) in visited:
                return False
            visited.add((stateId, strm.numCharsRead()))
            theState = self.states[stateId]

            c = strm.readChar()
            if strm.eof() and theState.isAccepting():

                return True

            strm.unreadChar(c)

            for onClass, toStateId in theState.getTransitions():

                if onClass == "epsilon":
                    if acceptsSuffix(toStateId):
                        return True

                else:
                    c = strm.readChar()

                    if c in self.classes[onClass] and acceptsSuffix(toStateId):
                        return True

                    strm.unreadChar(c)
            return False
        visited = set()
        return acceptsSuffix(self.startStateId)


def main():

    q0 = state.State(0)
    q1 = state.State(1)
    q2 = state.State(2)
    q3 = state.State(3, True)
    q4 = state.State(4)
    q5 = state.State(5)
    q6 = state.State(6)
    q7 = state.State(7)
    q8 = state.State(8, True)

    classes = {"a": frozenset(["a"])}

    q0.addTransition("a", 1)
    q0.addTransition("a", 4)

    q1.addTransition("a", 2)
    q2.addTransition("a", 3)

    q3.addTransition("a", 1)

    q4.addTransition("a", 5)
    q5.addTransition("a", 6)
    q6.addTransition("a", 7)
    q7.addTransition("a", 8)

    q8.addTransition("a", 4)

    nfa = NFAStateMachine(
        {0: q0, 1: q1, 2: q2, 3: q3, 4: q4, 5: q5, 6: q6, 7: q7, 8: q8}, 0, classes)

    done = False

    s = input(
        "Please enter a string of zeros and ones (type done to quit): ").strip()

    while s != "done":

        strm = streamreader.StreamReader(io.StringIO(s))

        if nfa.accepts(strm):
            print("The string is accepted by the finite state machine.")
        else:
            print("The string is not accepted.")

        s = input(
            "Please enter a string of zeros and ones (type done to quit): ").strip()

    print("Program Completed.")

if __name__ == "__main__":
    main()
