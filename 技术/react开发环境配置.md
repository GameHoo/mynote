# React开发环境配置


##涉及到的模块
webpack
>一个前端的包管理的npm库,让你的前端js代码可以引用其他文件(.js.css)

webpack-merge
>可以把webpack的配置分开，然后动态的整合。（不同的开发步骤需要不同的配置）

webpack-validator
>验证webpack的配置有没有语法错误，进行提示。
##加载器babel-loader,css-loader,style-loader
>babel-loader可以把不同的js语法转化成浏览器用的语法
>css-loader,style-loader,可以把css转化成js
#步骤
##安装
安装 webpack,webpack-merge，webpack-validator,babel-core,babel-loader,css-loader,style-loader
npm i xxx --save-dev
安装 babel perset
npm install --save-dev babel-preset-es2015
npm install --save-dev babel-preset-react
##配置
**package.json**
```javascript
"scripts": {
    "build": "webpack",
    "dev": "webpack-dev-server"
  },
```
build是只生成文件
dev是开启一个服务器，实时响应文件更改生成文件,用于开发。
**webpack.config.js**
```javascript
const path = require('path');
const webpack = require('webpack');
const merge = require('webpack-merge');
const validate = require('webpack-validator');
const PATHS = {
  entry: path.join(__dirname, 'src/main.js'),
  build: path.join(__dirname, 'dist')
};

const common = {
  // Entry accepts a path or an object of entries.
  // We'll be using the latter form given it's
  // convenient with more complex configurations.
  entry: {
    app: PATHS.entry
  },
  output: {
    path: PATHS.build,
    filename: 'bundle.js'
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin({
        multiStep: true
      })
  ],
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  module: {
  loaders: [
    { test: /\.js$/, exclude: /node_modules/, loader: "babel-loader" },
    { test: /\.css$/, loader: "style-loader!css-loader" }
  ]
}
};
var config;
// Detect how npm is run and branch based on that
switch(process.env.npm_lifecycle_event) {
  case 'build':
    config = merge(common, {});
    break;
  case "dev":
    config=merge(common, {
      watchOptions: {
        aggregateTimeout: 300,
        poll: 1000
      },
      devServer:{
        historyApiFallback: true,
        hot: true,
        inline: true,
        stats: 'errors-only',
      }
    });
    break;
  default:
    config = merge(common, {});
}
module.exports = validate(config);

```
**.babelrc**
```javascript
{
  "presets": [
    "es2015",
    "react"
  ]
}
```