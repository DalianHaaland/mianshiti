
import pandas as pd

# 读取测试数据
data = pd.read_csv("https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv")

# 将数据转换为列表
data_list = data.values.tolist()

# 将列表拆分为多个数组
batch_size = 80
batches = [data_list[i:i+batch_size] for i in range(0, len(data_list), batch_size)]

# 打印输出每个数组
for i, batch in enumerate(batches):
    print(f"Batch {i+1}:")
    print(batch)