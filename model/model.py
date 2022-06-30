import paddle.fluid as fluid
from paddle.fluid.dygraph import Pool2D, Conv2D
from paddle.fluid.dygraph import Linear


class MyLeNet(fluid.dygraph.Layer):
    def __init__(self):
        super(MyLeNet, self).__init__()
        self.c1 = Conv2D(3, 6, 5, 1)
        self.s2 = Pool2D(pool_size=2, pool_type='max', pool_stride=2)
        self.c3 = Conv2D(6, 16, 5, 1)
        self.s4 = Pool2D(pool_size=2, pool_type='max', pool_stride=2)
        self.c5 = Conv2D(16, 120, 5, 1)
        self.f6 = Linear(120, 84, act='relu')
        self.f7 = Linear(84, 10, act='softmax')

    def forward(self, input):
        # print(input.shape)
        x = self.c1(input)
        # print(x.shape)
        x = self.s2(x)
        # print(x.shape)
        x = self.c3(x)
        # print(x.shape)
        x = self.s4(x)
        # print(x.shape)
        x = self.c5(x)
        # print(x.shape)
        x = fluid.layers.reshape(x, shape=[-1, 120])
        # print(x.shape)
        x = self.f6(x)
        y = self.f7(x)
        return y
