### 学习笔记
---
### `pandas`
- 对数据做处理，比如切分，清洗数据等等操作

- 加载文件：可以通过`read_*()`引入，`*`代表文件类型。比如：`read_csv(),read_sql(),read_excel()等等`
  - 如果文件在当前项目可执行目录中
    - `df = pandas.read_csv()`
      - 如果文件和该脚本不在一个目录下，可以先获取执行脚本的目录，再定位：`file = os.path.dirname(os.path.realpath(__file__))`然后再`book=os.path.join(file, 文件名)`
      - 在交互模式下，这种方式不友好。在虚拟环境下会定位到你虚拟环境下的执行目录
    - 文件导入示例
      ```python
      
        # pip install xlrd
        # 导入excel文件
        xcel1 = pd.read_excel(r'1.xlsx')
        # 指定导入哪个Sheet
        pd.read_excel(r'1.xlsx',sheet_name = 0)

        # 支持其他常见类型
        pd.read_csv(r'c:\file.csv',sep=' ', nrows=10, encoding='utf-8')

        pd.read_table( r'file.txt' , sep = ' ')

        import pymysql
        sql  =  'SELECT *  FROM mytable'
        conn = pymysql.connect('ip','name','pass','dbname','charset=utf8')
        df = pd.read_sql(sql,conn)

        # 显示前几行
        excel1.head(3)

        # 行列数量
        excel1.shape

        # 详细信息
        excel1.info()
      ```
  - 显示前三行：`df[0:3]`  
  - 添加表头：`df.columns=[字段1,字段2,字段3]`
  - 取出某列：`df[字段]`
  - 过滤字段
    - 字段是否等于某个值：`df[字段] == 值`
    - 字段等于某个值的行所有信息：`df[df[字段]== 值]`
  - 显示特定行、列：`df[0:3,[字段]]`
  - 删除缺失数据：`df.dropna()`
  - 数据聚合：`df.groupby(字段).sum()`
  - 值的替换
    ```python
        strat_to_number = {
            '力荐' : 5,
            '推荐' : 4,
            '还行' : 3,
            '较差' : 2,
            '很差' : 1
        }

        df['new_start] = df['start'].map(start_to_number)
    ```
- 数据类型
  - `DataFrame`：相当于Excel里的表格多行和多列的结构
    - 有行的索引和列的索引
    - 操作
      - 列表创建dataframe：`pd.DataFrame(['a', 'b', 'c', 'd'])`
      - 嵌套列表创建dataframe：`pd.DataFrame([['a', 'b'], ['c', 'd']])`
      - 自定义列索引：`df1.columns= ['one', 'two']`
      - 自定义行索引：`df1.index = ['first', 'second']`
      - 获取全部值：`df1.values`
  - `Series`：相当于Excel中的一行或者一列。由numpy库而来，在numpy中是列
    - 会默认加上索引，并且索引是可以修改的
    - 操作
      - 通过列表创建：`pandas.Series(['a','b','c'])`
      - 通过字典创建：`pandas.Series({'a':1,'b':2,'c':3})`
      - 通过关键字创建时指定索引`pandas.Series([11,22,33],index=['a','b','c'])`
      - 获取全部索引：`s1.index`
      - 获取全部值：`s1.values`
      - 转换为列表：s1.values.tolist()
    - 查询效率
      - 如果`index`是唯一的，pandas通过查询时间复杂度是O(1)
      - 如果`index`有序不唯一，时间复杂度是O(logN)
      - 如果`index`是完全随机的，时间复杂度是O(N),因为要全表扫描
    - 示例
      ```python
        import re
        emails = pd.Series(['abc at amazom.com', 'admin1@163.com', 'mat@m.at', 'ab@abc.com'])
        pattern = '[A-Za-z0-9._]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,5}'
        mask = emails.map(lambda x: bool(re.match(pattern,x)))
        email[mask]
      ```
- 数据处理
  - 缺失值处理
    - `Series`：`s = pd.Series([ 1, 2, np.nan, 3, 4, 5, 6, np.nan, 8])`
      - `s.hasnans`：检验序列中是否有缺失值
      - `s.fillna()`：将缺失值填充为平均值
    - `Dataframe`：`df = pd.DataFrame({"A":[5,3,None,4], "B":[None,2,4,3], "C":[4,3,8,5], "D":[5,4,2,None]})`
      - `df.isnull().sum()`：查看缺失值汇总
      - `df.ffill()`：用上一行填充
      - `df.ffill(axis=1)`：用前一列填充
      - `df.info()`：查询有多少非空数值
      - `df.dropna()`：缺失值删除整行
      - `df.fillna()`：填充缺失值
      - `df.drop_duplicates()`
  - 数据调整
    - `df[ ['A', 'C'] ]`：列的选择,多个列要用列表
    - `df.iloc[:, [0,2]]`：表示所有行，获得第1和第3列
    - `df.loc[[0, 2]]`： 选择第1行和第3行
    - `df.loc[0:2]`：选择第1行到第3行
    - `df[(df['A']<5) & (df['C']<4)]`：比较
    - `df['C'].replace(4,40)`：数值替换
    - `df.replace([4,5,8], 1000)`：多对一替换
    - `df.replace({4:400,5:500,8:800})`：多对多替换
    - `df.sort_values ( by = ['A'] ,ascending = False)`：按照指定列降序排序
    - `df.sort_values ( by = ['A','C'] ,ascending = [True,False])`：多列指定排序
    - `df.drop( 'A' ,axis = 1)`：删除列
    - `df.drop( 3 ,axis = 0)`：删除行
    - `df[df['A']<4]`：删除特定行
    - `df.T`,`df.T.T`：行列互换
    - 数据：`df4 = pd.DataFrame([['a', 'b', 'c'],['d', 'e', 'f']], columns= ['one', 'two', 'three'], index = ['first', 'second'])`
      - `df4.stack()`：堆栈，一行一行写入
      - `df4.unstack()`：一列一列写入
      - `df4.stack().reset_index()`：重置索引
- 基本操作。数据：`df = pandas.DataFrame({"A":[5,3,None,4], "B":[None,2,4,3], "C":[4,3,8,5], "D":[5,4,2,None]})`
  - 算数运算
    - `df['A']+df['C']`：两列之间的加减乘除
    - `df['A']+5`：任意一列加/减一个常数值，这一列中的所有值都加/减这个常数值

  - 比较运算
    - `df['A']>df['C']`
  - `df.count()`：count非空值计数
  - `df.sum()`：非空值每列求和
  - `df['A'].sum()`：某列非空值求和
  - mean求均值
  - max求最大值
  - min求最小值
  - median求中位数  
  - mode求众数
  - var求方差
  - std求标准差

- 分组聚合
  ```python
  import pandas as pd
  import numpy as np

  # 聚合
  sales = [{'account': 'Jones LLC','type':'a', 'Jan': 150, 'Feb': 200, 'Mar': 140},
          {'account': 'Alpha Co','type':'b',  'Jan': 200, 'Feb': 210, 'Mar': 215},
          {'account': 'Blue Inc','type':'a',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
  df = pd.DataFrame(sales)
  ```
  - `.groupby('type').groups`：分组
  - `df.groupby('type').count()`：统计分组后的每组数量
  - `df2.groupby('type').aggregate( {'type':'count' , 'Feb':'sum' })`：各类型产品的销售数量和销售总额
  ```python
  group=['x','y','z']
  data=pd.DataFrame({
      "group":[group[x] for x in np.random.randint(0,len(group),10)] ,
      "salary":np.random.randint(5,50,10),
      "age":np.random.randint(15,50,10)
      })
  ```
  - `data.groupby('group').agg('mean')`：每组平均值
  - `data.groupby('group').mean().to_dict()`：平均值（使用一个函数时可以使用）计算之后转为字典
  - `data.groupby('group').transform('mean')`：计算平均值，是分配给每个元素，没有合并显示
  - 数据透视表
    ```python
    pd.pivot_table(data, 
               values='salary', 
               columns='group', 
               index='age', 
               aggfunc='count', 
               margins=True  
            ).reset_index()
    ```

- 数据拼接
  - `pd.merge(data1, data2)`：一对一拼接，一个公共列
  - `pd.merge(data3, data2, on='group')`：多对一拼接，多个公共列，通过on指定对应列
  - `pd.merge(data3, data2)`：多对多拼接
  - `pd.merge(data3, data2, left_on= 'age', right_on='salary')`：没有公共列，指定两个数据的各自的列作为参照
  - `pd.merge(data3, data2, on= 'group', how='inner')`：内连接，不指明连接方式，默认都是内连接（how还可以为left、right、outer）
  - `pd.concat([data1, data2])`：纵向连接

- 数据输出和绘图
  - `df.to_excel( excel_writer = r'file.xlsx')`：导出为.xlsx文件
  - `df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1')`：设置Sheet名称
  - `df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', index = False)`：设置索引,设置参数index=False就可以在导出时把这种索引去掉
  - `df.to_excel( excel_writer = r'file.xlsx', sheet_name = 'sheet1', index = False, columns = ['col1','col2'])`：设置要导出的列
  - `enconding = 'utf-8'`：设置编码格式
  - `na_rep = 0 # 缺失值填充为0`：缺失值处理
  - `inf_rep = 0`：无穷值处理
  - `to_csv()`：导出为.csv文件
  - `df.to_pickle('xx.pkl') `：性能
  - `agg(sum)`：快
  - `agg(lambda x: x.sum())`：慢
    ```python
    import matplotlib.pyplot as plt
    plt.plot(df.index, df['A'], )
    plt.show()
    lt.plot(df.index, df['A'], 
        color='#FFAA00',    # 颜色
        linestyle='--',     # 线条样式
        linewidth=3,        # 线条宽度
        marker='D')         # 点标记

    plt.show()
    # seaborn其实是在matplotlib的基础上进行了更高级的API封装，从而使绘图更容易、更美观
    import seaborn as sns
    # 绘制散点图
    plt.scatter(df.index, df['A'])
    plt.show()

    # 美化plt
    sns.set_style('darkgrid')
    plt.scatter(df.index, df['A'])
    plt.show()
    ```