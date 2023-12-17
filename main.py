import pandas as pd
import os
import shutil

# 读取CSV文件
csv_file = 'csv_files/train.csv'
df = pd.read_csv(csv_file)

# 统计每个类别的图像数量
category_counts = df['label'].value_counts()

# 打印类别数量和每个类别的图像数量
print(f"总共需要拷贝的类别数量: {len(category_counts)}")
for label, count in category_counts.items():
    print(f"类别 {label} 有 {count} 张图像")

# 源文件夹路径
source_folder = '/mnt/mmtech01/dataset/lzy/ILSVRC2012/train'

# 目标文件夹路径
target_folder = '/mnt/mmtech01/usr/liuwenzhuo/torch_ds/miniImageNet'

# 遍历CSV文件中的每一行，复制图像到目标文件夹
for index, row in df.iterrows():
    source_path = os.path.join(source_folder, row['label'], row['filename'])
    target_path = os.path.join(target_folder, row['label'])

    # 如果目标类别文件夹不存在，则创建
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        print(f"创建目录 {target_path}")

    # 复制文件
    shutil.copy(source_path, os.path.join(target_path, row['filename']))
    print(f"文件 {row['filename']} 已从 {source_path} 拷贝到 {target_path}")

print("所有文件拷贝完成。")
