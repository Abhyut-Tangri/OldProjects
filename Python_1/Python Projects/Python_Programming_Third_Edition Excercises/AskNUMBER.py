def ask_number(question, low, high):
    # """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response