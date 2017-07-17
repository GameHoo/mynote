# Dijkstra算法

给定起点，求到其它所有点最短路（单源最短路问题）

## 思路

1. 维护“每个点离起点的距离”，开始时只有起点距离为0，其它点距离不存在。

   >距离不存在的意思就是，还需要搭桥

   顶点分为两个集合，“确定了最短距离的”，和“没确定最短距离的”。

2. 在“没确定最短距离”的点里面找个距离最短的，就是距离已经确定了的，用这个确定的点作为中继点，如果找不到这个点，算法结束。

   >距离存在的点里，距离最短的点肯定不需要搭桥

3. 用这个中继点更新“没有确定最短距离的”点的距离，继续执行第2步。

## 应用

### 路径记录

如果要记录路径，用一个数组记录各个节点的前驱结点。在算法进行第3步的时候更新这个数组。

### 最短路径条数记录





## 示例代码

```c++
//简便函数式 带路径还原 带增加路径要求
void shortest()
{
	bool *used = new bool[N];
	int *l = new int[N];//距离
	int *t = new int[N];//时间
	int *pre = new int[N];//前驱节点
	for (int i = 0; i < N; i++)
	{
		l[i] = INT_MAX;
		t[i] = INT_MAX;
		used[i] = false;
		pre[i] = i;
	}
	l[S] = 0;
	t[S] = 0;
	while (true)
	{
		int u = -1;
		for (int i = 0; i < N; i++)
		{
			if (used[i] == false && (u == -1 || l[i] < l[u]))
			{
				u = i;
			}
		}
		if (u == -1)break;
		used[u] = true;
		for (int i = 0; i < N; i++)
		{
			if (Length[u][i] != INT_MAX && used[i]==false)
			{
				if (l[u] + Length[u][i] < l[i])
				{
					pre[i] = u;
					l[i] = l[u] + Length[u][i];
					t[i] = t[u] + Time[u][i];
				}
				//增加路径要求 长度相同选时长需要最小的
				if (l[u] + Length[u][i] == l[i])
				{
					if (t[i] > t[u] + Time[u][i])
					{
						pre[i] = u;
						l[i] = l[u] + Length[u][i];
						t[i] = t[u] + Time[u][i];
					}
				}
			}
		}
 
	}
	int i = T;
	ShortestPath.push_back(T);
	while (i != S)
	{
		ansDis += Length[pre[i]][i];
		i = pre[i];
		ShortestPath.push_back(i);
	}
}

```