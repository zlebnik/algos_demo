# Задача: "Скобочная последовательность"
# Определите, является ли указанная скобочная последовательность корректной
import string

closing_bracket = {
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_correct_bracket_seq(lst):
    stack = []

    def inner_check(curr: str):
        if not curr:
            return len(stack) == 0

        current_bracket, new_curr = curr[0], curr[1:]

        if current_bracket in closing_bracket:
            if not stack:
                return False

            last_bracket = stack.pop()

            if closing_bracket[current_bracket] != last_bracket:
                return False
        else:
            stack.append(current_bracket)

        return inner_check(new_curr)

    return inner_check(lst)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    brackets = input()
    print(is_correct_bracket_seq(brackets))

