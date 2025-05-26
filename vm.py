class SimpleVM:
    def __init__(self):
        self.variables = {}

    def execute(self, intermediate_code, output_callback=print):
        for instr in intermediate_code:
            op = instr[0]

            if op == 'assign':
                _, var, value = instr
                self.variables[var] = self._resolve(value)

            elif op == 'binop':
                _, operator, arg1, arg2 = instr
                val1 = self._resolve(arg1)
                val2 = self._resolve(arg2)
                result = self._binary_op(operator, val1, val2)
                temp_var = f't{len(self.variables)}'
                self.variables[temp_var] = result

            elif op == 'print':
                _, val = instr
                output_callback(str(self._resolve(val)))

    def _resolve(self, val):
        if isinstance(val, (int, float)):
            return val
        if isinstance(val, str) and val.isdigit():
            return int(val)
        return self.variables.get(val, 0)

    def _binary_op(self, operator, val1, val2):
        try:
            if operator == '+': return val1 + val2
            if operator == '-': return val1 - val2
            if operator == '*': return val1 * val2
            if operator == '/': return val1 / val2
            if operator == '==': return val1 == val2
            if operator == '!=': return val1 != val2
            if operator == '<': return val1 < val2
            if operator == '<=': return val1 <= val2
            if operator == '>': return val1 > val2
            if operator == '>=': return val1 >= val2
            if operator == '&&': return val1 and val2
            if operator == '||': return val1 or val2
        except Exception as e:
            output_callback(f"Runtime Error: {e}")
        return 0
