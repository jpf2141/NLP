class Transition(object):
    """
        This class defines a set of transitions which are applied to a
        configuration to get the next configuration.
        """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'
    
    def __init__(self):
        raise ValueError('Do not construct this object!')
    
    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
            """
        
        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer[0]
        if(idx_wi==0):
            return -1
        for a in conf.arcs:
            if(a[2]==idx_wi):
                return -1
        conf.stack.pop()
        conf.arcs.append((idx_wj, relation, idx_wi))
    
    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
            """
        if not conf.buffer or not conf.stack:
            return -1
        
        # You get this one for free! Use it as an example.
        
        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)
        
        conf.stack.append(idx_wj)
    conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
            """
        
        idx_wi = conf.stack[-1]
        for a in conf.arcs:
            if(a[2]==idx_wi):
                conf.stack.pop()
                return

    return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
            """
        
        if not conf.buffer or not conf.stack:
            return -1
        
        idx_wi = conf.buffer.pop(0)
        conf.stack.append(idx_wi)
#class Transition(object):
#    """
#    This class defines a set of transitions which are applied to a
#    configuration to get the next configuration.
#    """
#    # Define set of transitions
#    LEFT_ARC = 'LEFTARC'
#    RIGHT_ARC = 'RIGHTARC'
#    SHIFT = 'SHIFT'
#    REDUCE = 'REDUCE'
#
#
#
##A parser configuration is the tuple C = (S, B, A), where S is the stack, B is the buffer, and A is
##the set of arcs that represent the dependency relations.
#
#
#    def __init__(self):
#        raise ValueError('Do not construct this object!')
#
#    @staticmethod
#    def left_arc(conf, relation):
##Add the arc (b, L, s) to A, and pop S. That is, draw an arc between the next node on the
##buffer and the next node on the stack, with the label L.
##Let s be the next node in the Stack, b be the next node in the Buffer.
#        """
#            :param configuration: is the current configuration
#            :return : A new configuration or -1 if the pre-condition is not satisfied
#        """
#        
#        #check pre-conditions
#        if not conf.buffer or not conf.stack:
#            return -1
#        elif(len(conf.stack) <= 1):     #check to make sure stack is more than just ROOT
#            return -1
#        else:
#            idx_wi = conf.stack[-1]  #check top of stack
#            idx_wj = conf.buffer.pop(0)
#            arc = tuple([idx_wj, relation, idx_wi]) #new dependency arc
#           
#            #check to make sure wi is not a dependant of some other word
#            for conf_arc in conf.arcs:
#                if conf_arc[2] == idx_wi:
#                    return -1
#
#
#            #preconditions satisified
#            conf.stack.pop()    #pop stack
#            conf.arcs.append(arc)
#
#
#    @staticmethod
#    def right_arc(conf, relation):
#        """
#            :param configuration: is the current configuration
#            :return : A new configuration or -1 if the pre-condition is not satisfied
#        """
#        #Add the arc (s, L, b) to A, and push b onto S.
#        if not conf.buffer or not conf.stack:
#            return -1
#
#        #You get this one for free! Use it as an example.
#
#
#        idx_wi = conf.stack[-1]
#        idx_wj = conf.buffer.pop(0)
#
#        conf.stack.append(idx_wj)
#        conf.arcs.append((idx_wi, relation, idx_wj))
#
#
#    @staticmethod
#    def reduce(conf):
#        """
#            :param configuration: is the current configuration
#            :return : A new configuration or -1 if the pre-condition is not satisfied
#        """
##The REDUCE transition pops the stack and is subject to the preconditions that the top
##token has a head.
#        if not conf.stack:
#            return -1
#        else:
#            idx_wi = conf.stack[-1]
#        
#            #check to make sure wi is a dependant of some other word
#            wi_exists = False
#            for conf_arc in conf.arcs:
#                if conf_arc[2] == idx_wi:
#                    wi_exists = True
#                    break
#            #wi is not a dependant of another word, dont reduce yet
#            if wi_exists is False:
#                return -1
#            else:   #we can reduce!
#                conf.stack.pop()
#
#
#    @staticmethod
#    def shift(conf):
#        """
#            :param configuration: is the current configuration
#            :return : A new configuration or -1 if the pre-condition is not satisfied
#        """
##The SHIFT transition removes the first node in the buffer and pushes it onto the stack.
#        if not conf.buffer:
#            return -1
#        else:
#            idx_wi = conf.buffer.pop(0)
#            conf.stack.append(idx_wi)
