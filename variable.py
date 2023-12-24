
class Variable:
    def __init__(self,domain:list[int]=None,value:int=0) -> None:
        self.value = value
        # self.domain = domain if domain is not None else [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if domain is None:
            self.domain = [1,2,3,4,5,6,7,8,9]
        else:
            self.domain = [self.value]
    
    def __str__(self) -> str:
        return f'{self.value}'