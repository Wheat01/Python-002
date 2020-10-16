import pandas as pd
df = pd.DataFrame() 
# SELECT * FROM data;
# 查询所有数据
df

# SELECT * FROM data LIMIT 10;
# 查询10条数据
df.loc[:10,:]

# SELECT id FROM data;  //id 是 data 表的特定一列
# 查出数据的某一个字段的所有值
df['C']

# SELECT COUNT(id) FROM data;
# 查询数据条数
df['A'].shape[0]

# SELECT * FROM data WHERE id<1000 AND age>30;
# 查询满足某些条件的数据
df[df['id']<1000] & df[df['age']>30]

# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df.groupby('id').order_id.nunique()

# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# 内联合查询
pd.merge(table1, table2, on='id')

# SELECT * FROM table1 UNION SELECT * FROM table2;
pd.concat([table1, table2]).drop_duplicates()

# DELETE FROM table1 WHERE id=10;
# 查询满足某条件的的记录
table1.loc[table1['id']==10,:]

# ALTER TABLE table1 DROP COLUMN column_name;
df.drop(['column_name'], axis=1)
