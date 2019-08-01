def arg_is_iter(arg):
    return '__iter__' in dir(arg)

def any_iter(arg):

    if arg_is_iter(arg):
        if 'any' in dir(arg):
            #Object has built in method
            
            return any_iter(arg.any())
            #Call the method again to make sure the object is
            #for sure iterable now
        
        return any(arg)
    else:
        return bool(arg)
