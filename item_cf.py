#coding:utf-8
from text_sim import textSim

class itemCf(textSim):
    '''
    推荐相似的物品给user
    '''
    def __init__(self):
        super(itemCf,self).__init__()
        self.index2question = {}

    def FilterItem(self):
        '''
        按照部门过滤相似问题
        '''

    def RecallItem(self, question):
        '''
        召回问题
        '''
        sim_question = NearQuestion(self, question='', topk=10)
        return sim_question

if __name__=='__main__':
    question = ''
    
