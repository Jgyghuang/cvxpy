from cvxpy.expressions.variables.variable import Variable


def abs_canon(expr, args):
    x = args[0]
    shape = expr.shape
    t = Variable(*shape)
    constraints = [t >= x, t >= -x]
    return t, constraints