import pico2d
import time
frame_time = 0.0

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
    global frame_time
    global running, stack
    running = True
    stack = [start_state]
    start_state.enter()
    current_time = time.time()
    while(running):
        stack[-1].handle_events()
        stack[-1].update(frame_time)
        stack[-1].draw()
        frame_time = time.time() - current_time
        frame_rate = 1.0/frame_time
        current_time += frame_time
    while(len(stack) > 0):
        stack[-1].exit_state()
        stack.pop()


