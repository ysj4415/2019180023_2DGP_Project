import pico2d

class GameState:
    def __init__(self, state):
        self.enter = state.enter
        self.eixt_state = state.exit_state
        self.pause = state.pause
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw
        self.resume = state.resume

running = None
stack = None


def change_state(state):
    global stack
    if len(stack) > 0:
        stack[-1].exit_state
        stack.pop()
    stack.append(state)
    stack.enter()

def push_state(state):
    global stack
    if len(stack) > 0:
        stack[-1].pause()
    stack.append(state)
    state.enter()

def pop_state():
    global stack
    if len(stack) > 0:
        stack[-1].exit_state()
        stack.pop()
    if len(stack) > 0:
        stack[-1].resume()



def quit():
    global running
    running = False

def run(start_state):
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()
    while(running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        pico2d.delay(0.05)

    while(len(stack) > 0):
        stack[-1].exit_state()
        stack.pop()


