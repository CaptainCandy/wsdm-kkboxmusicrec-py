# wsdm-kkboxmusicrec-py

An attempt of music recommendation.

CRISP-DM

## Business Understanding

### 音乐推荐算法

- 从网易云音乐的年度报告与每日推荐引出
  - 唱片和DJ的光荣时代已经过去了（Kaggle页面上的闲话）
  - 这个时代属于音乐推荐算法
- 音乐推荐算法要解决的问题是什么？
  - 用户是否会喜欢一首推荐给他的歌曲或歌手
  - 怎么知道一个新用户会喜欢什么类型的歌曲
- 现有两大思路
  - 基于内容
  - 以人为本
- 好的音乐推荐算法？
  - 更好的用户体验
  - 更强的用户黏性
    - 音乐版权大量缺失的网易云留住用户离不开推荐系统

### KKBOX

- 客户端的图片；公司logo
- 起源于台湾的数字音乐媒体服务商
- 提供付费的音乐服务

### 业务需求和目标

KKBOX现有一个基于矩阵分解的协同过滤的音乐推荐系统

KKBOX想看到效果更好的预测方法，以帮助他们更加精准地向用户推荐他们喜欢的歌曲

目标：提高预测的准确率

### 问题定义

- 预测某位用户在初次听过某一首歌之后的一段时间里，再次选择播放这首歌曲的概率。
  - 依据某位用户播放某一首歌的记录作出判断
  - target表示在未来一个月内是否会再次播放

## Data Understanding

### 数据概览

除了train和test以外，还有songs,song_extra_info,members三张数据表。

- train与test：KKBOX的用户听歌记录
  - 只选取一段时间内某位用户首次听某一首歌的记录信息
  - 用户ID与歌曲ID的匹配
  - 听歌时的操作环境
  - 目标变量target
- songs与songs_extra_info
  - 歌曲ID和歌名
  - 歌手、作曲、作词
  - 音乐风格
  - 音乐时长
  - 歌曲语言
  - ISRC:国际标准录音编码
- members：会员信息
  - 用户ID
  - 城市、性别、年龄
  - 注册渠道
  - 注册时间与会员资格过期时间

### 深入数据

#### ISRC

- International Standard Recording Code
- 编码规则：country publisher year

#### 音乐风格

- genre_ids: `124|324|754`
- 统计ids个数分布，说明为什么只选前三个

#### 年龄与性别

缺失值简直不要太多

#### 操作环境

- source system tab
- source screen name
- source type
- 展示每个属性有哪些取值

## Data Preparation

### 歌曲相关信息

- 从 genre_ids 提取出 genre_1st genre_2nd genre_3rd
- 同一首音乐有多个歌手、作曲、作词的情况，提取第一个人
- ISRC的分拆
  - 提取每个年份/国家/公司的歌曲数量

### 会员相关信息

日期格式数据的变换

### 值变换

- 连续变量
  - 取对数，减小异常值影响
- 分类变量
  - LabelEncoder，转为编号

### 时间序列

- 说明
  1. train和test里的记录是有序排列的
  1. 某条记录在整个数据集中的位置体现这个播放行为发生时间的先后顺序
  1. 据此能提取出一系列有趣的特征

- 特征
  - 某个会员前一次听这位歌手的音乐，迄今为止过去了多长时间

## Modeling

- Xgboost
  - 决策树
  - 集成学习 boosting
- 参数设置
  - 展示2秒钟

## Evaluation

## Deploying
