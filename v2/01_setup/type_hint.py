from typing import Literal
a: int = 1
b: float = 1.1
c: str = 'string'
d: bool = True

e: list[int] = [1, 2]
f: dict[str, bool] = {'key': True}
g: Literal['OK', 'NG'] = 'OK'

def sample(x: str) -> str:
    return x