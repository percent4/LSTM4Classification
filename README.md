# LSTM4Classification
Using LSTM model to complete short document classification task.

利用LSTM实现短文本分类，取字符特征。输入的数据格式为CSV,特征栏为eq,类别标签栏为label。模型主要为Embedding+LSTM+Softmax层，具体的组成如下图：

![模型示意图](https://github.com/percent4/LSTM4Classification/blob/master/model.png)


效果：

在train.csv上的测试结果如下：

|训练次数|测试集上的准确率|验证集上的准确率|
|---|---|---|
|1|52.18%|72.59%|
|3|83.68%|82.59%|
|5|88.81%|83.79%|
