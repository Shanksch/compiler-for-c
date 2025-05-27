import tkinter.simpledialog

class SimpleVM:
    def __init__(self):
        self.variables = {}
        self.labels = {}
        self.instructions = []
        self.pc = 0

    def resolve(self, val):
        if isinstance(val, str) and val in self.variables:
            return self.variables[val]
        return val

    def execute(self, code, output_callback=print, input_callback=None):
        self.instructions = code
        self.pc = 0

        # First pass: resolve labels
        for idx, instr in enumerate(self.instructions):
            if instr[0] == 'label':
                self.labels[instr[1]] = idx

        while self.pc < len(self.instructions):
            instr = self.instructions[self.pc]
            op = instr[0]

            if op == 'assign':
                _, var, val = instr
                self.variables[var] = self.resolve(val)

            elif op == 'binop':
                _, target, operator, left, right = instr
                left = self.resolve(left)
                right = self.resolve(right)
                result = self.evaluate(operator, left, right)
                self.variables[target] = result

            elif op == 'print':
                _, message = instr
                output_callback(str(message))

            elif op == 'scanf':
                _, var = instr
                value = self.gui_input(f"Enter value for {var}:")
                try:
                    self.variables[var] = int(value)
                except ValueError:
                    output_callback(f"Invalid input for {var}, defaulting to 0.")
                    self.variables[var] = 0

            elif op == 'ifFalse':
                _, condition, label = instr
                cond_value = self.resolve(condition)
                if not cond_value:
                    self.pc = self.labels.get(label, self.pc)
                    continue

            elif op == 'goto':
                _, label = instr
                self.pc = self.labels.get(label, self.pc)
                continue

            elif op == 'label':
                pass  # labels already processed

            else:
                output_callback(f"Unknown instruction: {instr}")

            self.pc += 1

    def evaluate(self, op, a, b):
        try:
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return a // b if b != 0 else 0
            if op == '>': return a > b
            if op == '<': return a < b
            if op == '>=': return a >= b
            if op == '<=': return a <= b
            if op == '==': return a == b
            if op == '!=': return a != b
            if op == '&&': return bool(a and b)
            if op == '||': return bool(a or b)
        except:
            return 0

    def gui_input(self, prompt):
        return tkinter.simpledialog.askstring("Input", prompt)