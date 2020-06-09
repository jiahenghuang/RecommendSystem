#coding:utf-8
from sklearn.metrics.pairwise import cosine_similarity
from bert4keras.backend import keras
from bert4keras.models import build_transformer_model
from bert4keras.tokenizers import Tokenizer
import numpy as np
from annoy import AnnoyIndex

class textSim(object):
    '''
    搜索最相似问题
    '''
    def __init__(self):
        self.config_path = '/Users/heng/work/bert4keras/data/chinese_L-12_H-768_A-12/bert_config.json'
        self.checkpoint_path = '/Users/heng/work/bert4keras/data/chinese_L-12_H-768_A-12/bert_model.ckpt'
        self.dict_path = '/Users/heng/work/bert4keras/data/chinese_L-12_H-768_A-12/vocab.txt'
        self.tokenizer = Tokenizer(self.dict_path, do_lower_case=True)  # 建立分词器
        self.model = build_transformer_model(self.config_path, self.checkpoint_path)  # 建立模型，加载权重
        self.tree = AnnoyIndex(768,'angular')
        self.tree.load('tree100_maxpool.ann')

    def QuestionEmbedding(self,question='',method='maxpool'):
        '''
        生成句子的向量表示
        '''
        token_ids, segment_ids = self.tokenizer.encode(question)
        embedding = self.model.predict([np.array([tokenizer]),np.array([segment_ids])])
        if method == 'cls':
            embedding = embedding[0][0].reshape(1,-1).tolist()
        if method == 'maxpool':
            embedding = embedding[0][1:-1].max(0).reshape(1,-1).tolist()
        return embedding

    def Similarity(self, q1, q2, method='maxpool'):
        '''
        计算文本之间相似度
        '''
        # 编码测试
        if method == 'cls':
            q1_embedding = self.QuestionEmbedding(q1,method='cls')
            q2_embedding = self.QuestionEmbedding(q2,method='cls')
        
        elif method == 'maxpool':
            q1_embedding = self.QuestionEmbedding(q1,method='maxpool')
            q2_embedding = self.QuestionEmbedding(q2,method='maxpool')
        return cosine_similarity(q1_embedding,q2_embedding)

    def NearQuestion(self, question='', topk=10):
        '''
        找到一个问题对应的top10问题
        '''
        embedding = self.QuestionEmbedding(question)
        question2score = {}
        result = self.t.get_nns_by_vector(embedding,topk,include_distances=True)
        indexs = result[0]
        scores = result[1]
        scores = [1-score for score in scores]
        for i, index in enumerate(indexs):
            question2score[i] = scores[i]
        return question2score

sim_text = textSim()
if __name__=='__main__':
    text_sim=textSim()
