def run_fba(model):
    solution = model.optimize()
    return solution