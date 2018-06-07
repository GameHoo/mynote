# 要学啥

从数据库获取List<Class> Objects

ListView 显示,更改,删除 Objects

.cs里 查询，更改，删除 Object

# 问题日志

### 问题1

ItemSource=List<Account> Accounts

Class Account 里有个 List<Character> Characters

Characters[i].PorpertyChanged，不会引起Account.PorPertyChanged

### 解决办法

**目标：在Character.PropertyChanged 的时候 引起Account.PorpertyChanged**

>Account.函数1 订阅 Characters.CollectionChanged
>
>这样 Charaters 添加新Character时 会调用函数1
>
>函数1：
>
>​	新Character.PorpertyChanged 订阅 Account.PorpertyChanged

### 问题2

有LAccounts和SAccounts

希望这两个列表和一个ListView绑定

### 解决办法

> 编写一个新的集合类
>
> 集合类包含LAccounts和SAccounts
>
> 然后订阅LAccounts和SAccounts的变化
>
> LAccounts[i].PorpertyChanged 引发 LAccounts.
>
> 但是希望

测试

>创建一个ALL_ACCOUNTS与Listview绑定
>
>在LAccounts里插入一个数据
>
>在SAccounts里插入一个数据
>
>在LAccounts里删除一个数据
>
>在SAccounts里删除一个数据
>
>LAccounts.Clear
>
>SAccounts.Clear
>
>修改LAccounts里的数据
>
>修改SAccounts里的数据

### 问题

is_done