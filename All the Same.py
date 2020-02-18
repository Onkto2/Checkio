#check.io - All the Same - 28/01/20
#look up required -

def all_the_same(elements: List[Any]) -> bool:
     is_all_equal = len(set(elements)) <= 1
    return is_all_equal