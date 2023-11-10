def removeInvalidParentheses(s):
    def isValid(expression):
        count = 0
        for char in expression:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def dfs(index, left_count, right_count, left_removed, right_removed, current_expression):
        if index == len(s):
            if left_removed == right_removed == 0 and isValid(current_expression):
                result.append(current_expression)
            return

        if s[index] == '(' and left_removed > 0:
            dfs(index + 1, left_count, right_count, left_removed - 1, right_removed, current_expression)
        elif s[index] == ')' and right_removed > 0:
            dfs(index + 1, left_count, right_count, left_removed, right_removed - 1, current_expression)

        dfs(index + 1, left_count, right_count, left_removed, right_removed, current_expression + s[index])

        if s[index] == '(':
            dfs(index + 1, left_count + 1, right_count, left_removed, right_removed, current_expression)
        elif s[index] == ')' and left_count < right_count:
            dfs(index + 1, left_count, right_count + 1, left_removed, right_removed, current_expression)

    result = []
    dfs(0, 0, 0, 0, 0, "")
    return result

# Test cases
print(removeInvalidParentheses("()())()"))  # Output: ["(())()","()()()"]
print(removeInvalidParentheses("(a)())()"))  # Output: ["(a())()","(a)()()"]
print(removeInvalidParentheses(")("))        # Output: [""]
