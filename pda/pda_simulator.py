from collections import deque

# ---------------------------------------------------------
# PDA SIMULATOR: BALANCED PARENTHESES AND PALINDROMES
# Based on the PDA designs in the presentation.
# ---------------------------------------------------------

BOTTOM = "Z0"


def balanced_parentheses_pda(string):
    """
    Deterministic PDA for balanced parentheses.
    Push X for '(' and pop X for ')'.
    Accept when the input is finished and only Z0 remains.
    """
    stack = [BOTTOM]
    trace = [(string, "".join(reversed(stack)))]

    for position, symbol in enumerate(string):
        if symbol == "(":
            stack.append("X")
        elif symbol == ")":
            if stack[-1] == BOTTOM:
                trace.append((string[position + 1:], "".join(reversed(stack))))
                return False, trace, "Closing parenthesis has no matching opening parenthesis."
            stack.pop()
        else:
            return False, trace, f"Invalid symbol: {symbol!r}. Only '(' and ')' are allowed."

        trace.append((string[position + 1:], "".join(reversed(stack))))

    accepted = stack == [BOTTOM]
    reason = "Input finished with only the bottom marker on the stack." if accepted \
        else "Input finished while unmatched opening parentheses remained."
    return accepted, trace, reason


def palindrome_npda(string):
    """
    NPDA for palindromes over {a, b}, including the empty string.
    It nondeterministically guesses the middle:
      - epsilon move for even-length palindromes
      - consume one middle symbol for odd-length palindromes

    BFS explores all possible configurations.
    A configuration is (state, input_position, stack).
    """
    if any(ch not in "ab" for ch in string):
        return False, [], "Invalid input. Only 'a' and 'b' are allowed."

    # stack is a tuple; its final element is the top.
    start = ("push", 0, (BOTTOM,))
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (state, position, stack), path = queue.popleft()

        # Accept when all input is read and only bottom marker remains.
        if state == "match" and position == len(string) and stack == (BOTTOM,):
            return True, path, "An accepting NPDA branch was found."

        next_configurations = []

        if state == "push":
            # Option 1: push the next input symbol onto the stack.
            if position < len(string):
                symbol = string[position]
                next_stack = stack + (symbol,)
                next_configurations.append(
                    ("push", position + 1, next_stack)
                )

            # Option 2: guess the middle using an epsilon transition (even length).
            next_configurations.append(("match", position, stack))

            # Option 3: guess the middle by consuming one symbol (odd length).
            if position < len(string):
                next_configurations.append(("match", position + 1, stack))

        elif state == "match":
            # Match the remaining input against the stack in reverse order.
            if position < len(string) and len(stack) > 1:
                symbol = string[position]
                if stack[-1] == symbol:
                    next_stack = stack[:-1]
                    next_configurations.append(
                        ("match", position + 1, next_stack)
                    )

        for next_config in next_configurations:
            if next_config not in visited:
                visited.add(next_config)
                queue.append((next_config, path + [next_config]))

    return False, [], "All possible NPDA branches failed."


def print_parentheses_result(string):
    accepted, trace, reason = balanced_parentheses_pda(string)

    print("\nBALANCED PARENTHESES PDA")
    print("-" * 55)
    print(f"Input: {string!r}")
    print(f"{'Step':<8}{'Remaining input':<22}{'Stack (top first)'}")
    for step, (remaining, stack) in enumerate(trace):
        print(f"{step:<8}{remaining!r:<22}{stack}")
    print("Result:", "ACCEPTED" if accepted else "REJECTED")
    print("Reason:", reason)


def print_palindrome_result(string):
    accepted, path, reason = palindrome_npda(string)

    print("\nPALINDROME NPDA (BFS SIMULATION)")
    print("-" * 55)
    print(f"Input: {string!r}")

    if path:
        print(f"{'Step':<8}{'State':<12}{'Position':<12}{'Stack (top last)'}")
        for step, (state, position, stack) in enumerate(path):
            print(f"{step:<8}{state:<12}{position:<12}{''.join(stack)}")
    else:
        print("No accepting path was found.")

    print("Result:", "ACCEPTED" if accepted else "REJECTED")
    print("Reason:", reason)


def main():
    while True:
        print("\n==============================================")
        print("          PDA SIMULATION PROGRAM")
        print("==============================================")
        print("1. Balanced Parentheses PDA")
        print("2. Palindrome NPDA")
        print("3. Run sample test cases")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            value = input("Enter a parentheses string, e.g. (()()): ")
            print_parentheses_result(value)

        elif choice == "2":
            value = input("Enter a palindrome string using a and b, e.g. abba: ")
            print_palindrome_result(value)

        elif choice == "3":
            print("\n--- Balanced Parentheses Test Cases ---")
            for value in ["(()())", "(()", "())", "", "()()"]:
                print_parentheses_result(value)

            print("\n--- Palindrome Test Cases ---")
            for value in ["abba", "aba", "aabbaa", "abab", "a", ""]:
                print_palindrome_result(value)

        elif choice == "4":
            print("Exiting PDA Simulator. Thank you!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
