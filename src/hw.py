""" 
A hello world to be sure all my tools work.
"""

from dataclasses import dataclass 

@dataclass
class Greeting:
    greeting: str
    auidence: str

    def __str__(self) -> str:
        return f"{self.greeting} {self.auidence}"

    
def main() -> None:
    g = Greeting("Hello", "world")
    print(g)

if __name__ == "__main__":
    main()