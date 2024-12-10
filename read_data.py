import zipfile

import pandas as pd

zip_file_path = 'data/fresh_comp_offline.zip'


def read_item_file():
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        with zip_ref.open('tianchi_fresh_comp_train_item.csv') as file:
            item_df = pd.read_csv(file, encoding='utf-8', header=0, sep=',')
    return item_df


def read_user_file():
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # 打开 tianchi_fresh_comp_train_user.csv 文件
        with zip_ref.open('tianchi_fresh_comp_train_user.csv') as file:
            user_df = pd.read_csv(file, encoding='utf-8', header=0, sep=',')
    return user_df


user_df = read_user_file()
item_df = read_item_file()
# 查看数据集量级
print('user整体数据的大小为', len(user_df))
print('user数据集中用户数量是：', len(set(user_df['user_id'])))
print('user数据集中商品数量是：', len(set(user_df['item_id'])))
print('user数据集中商品类别数量是：', len(set(user_df['item_category'])))

print('item数据集中商品数量是：', len(set(item_df['item_id'])))
print('item数据集中商品类别数量是：', len(set(item_df['item_category'])))
# 查看数据缺失情况
# print(user_df.isnull().sum())

# 查看字段类型：
# print(user_df.dtypes)
