class LeastMatchingExponent:
    def __init__(self, innerMatch):
        self.matcher = innerMatch
    
    def parser(self, body : str, hard_fail = True):
        for i in range(1, len(body) + 1):
            sub_body = body[:i]
            result = self.matcher.parser(sub_body, False)
            if not result:
                if i == len(body):
                    return result
                else:
                    continue
            return result
    
    def __str__(self):
        return str(self.matcher)