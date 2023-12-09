class Lit:
    def __init__(self, chars, rest=None):
        self.chars = chars
        self.rest = rest
        # print(f"chars: {chars}, rest: {rest}")

    def match(self, text, start=0):
        end = start + len(self.chars)
        # print(f"start: {start}, end: {end}, text: {text}")
        if text[start:end] != self.chars:
            # print(text[start:end], self.chars)
            return False
        if self.rest:
            # print(f"self.rest: {self.rest}")
            return self.rest.match(text, end)
        return end == len(text)
    
pattern = Lit("a", Lit("b"))
result = pattern.match("ab")

print(f"Final result: {result}")