# checkQNDXXtoExcel
对照名单统计青年大学习完成的情况~

Caution：
先选择后台输出的Excel文件（可以批量选择）
再选择名单的文件。

对名单文件的格式要求：（以下表述base1）
  内容存放在第一个sheet中，其中第一行为标题（无数据），姓名列的标题是“姓名”
  输出内容会生成在第四列

根据姓名（中英文字符）索引完成情况，自动过滤数字和其它字符

请注意备份名单文件，如果中途出现异常有可能使得名单文件丢失。
正常运行的情况下，名单除第三列右侧的新增列之外的列不会发生改变。

@AleryXiao
2022.11.21

constructed with Pysider6
