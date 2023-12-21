
class Variable:
    def __init__(self,domain:list[int]=None,value:int=0) -> None:
        self.value = value
        if domain is None:
            self.domain = [1,2,3,4,5,6,7,8,9]
    
    def __str__(self) -> str:
        return f'{self.value}'