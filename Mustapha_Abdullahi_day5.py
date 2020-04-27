def faithful(nth_faithful: int):
    """
    returns the 'nth_faithful' number
    
    :param nth_faithful: the nth faithful number to be returned
    :return: 
    :rtype: int
    """
    index = 0
    faithfuls = []
    faith_numbers = 0   # holds the number of 'faithful numbers' calculated

    while True:
        
        faithful = 7 ** index
        faithfuls.append(faithful)
        faith_numbers += 1
        len_prev_faithfuls = len(faithfuls) - 1
        
        for n in range(0, len_prev_faithfuls):
            next_faithful = faithful + faithfuls[n]
            faithfuls.append(next_faithful)
            faith_numbers += 1
        index += 1

        if nth_faithful <= faith_numbers:
            '''checks if the required faithful number is found'''
            return faithfuls[nth_faithful - 1]