#使用NumPy中的随机数
from numpy import random

#设定随机数种子
random.seeds(1234)

#均匀分布，产生2*3矩阵
random.rand(2,3)#在[0,1)中生成
random.uniform(low = 1, high = 5, size = (2,3))

#标准正态分布，产生2*3矩阵
random.randn(2,3)

#[0,1)内产生随机数
random.random(2,3)

#指定区间内生成随机整数
random.randint(low = 2, high = 6, size = (2,3))

#正态分布, loc表示均值，scale表示方差
random.normal(loc = 0, scale = 1, size = (2,3))

#泊松分布, lam表示参数
random.poisson(lam = 100, size = (2,3))

#生成Beta分布
random.beta(a = 3, b = 5, size = (2,3))

#二项分布
random.binomial(n = 4, p = 0.8, size = (2,3))

#指数分布
random.exponential(scale = 3, size = (2,3))

#F分布
random.f(dfnum = 100, dfden = 5, size = (2,3))

#随机采样
samples = ['1','2','3','4','5']
random.choice(samples, size = 5, replace = True)#有放回随机采样
random.choice(samples, size = 5, replace = False)#无放回随机采样

#随机打乱顺序
samples = ['1','2','3','4','5']
random.shuffle(samples)
