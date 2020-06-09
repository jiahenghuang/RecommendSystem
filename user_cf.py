#coding:utf-8
class UserCf(object):
    '''
    用于计算用户之间相似度
    '''
    def __init__(self):
        self.answer2question={} #问题和答案的一一对应关系
        self.user2item = {}  #用户访问了哪些问题
        self.item2user = {}  #这个问题被哪些用户访问了

    def BuildUser2item(self,):
        '''
        构建用户访问了哪些问题
        '''
    
    def BuildItem2user(self,):
        '''
        构建item被哪些用户访问了
        用于通过item推荐
        '''

    def JaccardSim(self, set1, set2):
        '''
        使用jaccard计算用户之间相似度
        '''
        intersect = set1 & set2
        union = set1 | set2
        intersect_num = len(intersect)
        union_num = len(union)
        if intersect_num and union_num:
            return intersect_num/union_num
        return 0

    def 

if __name__=='__main__':
    a=set([1,2,3,4,5])
    b=set([2,3,4,10,40,90])
    # b=set(['a','b','c'])
    user_cf = UserCf()
    print(user_cf.jaccard_sim(a,b))
