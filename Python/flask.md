$ git clone https://github.com/miguelgrinberg/flasky.git
$ cd flasky
$ git checkout 1a

# 创建项目

1.为这个项目创建一个单独的环境(venv)

>在项目目录 python venv ./

2.为这个项目安装flask

>pip install flask

3.编写脚本,激活环境,运行脚本

>Script/activate
>
>(venv) python hello.py

# flask程序的基本结构

## 初始化

生成flask的**app**变量

app = Flask(\_\_name\_\_)

## 处理请求

使用@app.route标记 请求函数

url_for():

​	可以让你用软编码方式生成url，参数为：填路由函数名，函数参数

## 返回响应

返回元组

特殊的重定向响应

# WEB表单



# 使用Jinjia2模板引擎

## 安装

pip install Jinja2

## 初始化

```python
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__)
bootstrap = Bootstrap(app)
env = Environment(
    loader=PackageLoader('yourapplication', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
```

## 设置：Environment

一个Environment的实例表示关于模板引擎的一个环境（各种设置和资源在这个环境里），操作是在环境里进行的。

即使你没有自己设置Environment，系统也会为你自己创一个。

### 属性：

* loader
* autoescape (自动转置 ‘\’)

### 方法:

* get_template

## 模板的表示和显示：Template

## 模板的载入：loader



**模板接收变量**

render_template('index.html',name=name)

**使用变量过滤器**

Hello, {{ name|capitalize }}

>safe 渲染值时不转义
>capitalize 把值的首字母转换成大写，其他字母转换成小写
>lower 把值转换成小写形式
>upper 把值转换成大写形式
>title 把值中每个单词的首字母都转换成大写
>trim 把值的首尾空格去掉
>striptags 渲染之前把值中所有的HTML 标签都删掉

**使用控制语句**

if else

for 循环

**宏（相当于函数）**

**block标签与extends**

为空是默认继承，不为空默认覆盖（不想覆盖用**{{super()}}**）

# 使用Flask-Bootstrap



# flask程序的拓展

Flask-Script 使用命令行而不是传参