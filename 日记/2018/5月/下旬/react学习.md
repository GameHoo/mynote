# react原理

virtual DOM 由 react element 组成 是 JavaScript object

react.createElement  生成 react element

>参数: attributes,properties,childrens

ReactDOM.render 把 react element 使用DOM API 转化为 DOM element

# 三种不同的创造组件的方法

## React.createClass

```jsx
const IngredientsList = React.createClass({
displayName: "IngredientsList",
renderListItem(ingredient, i) {
return React.createElement("li", { key: i }, ingredient)
},
render() {
return React.createElement("ul", {className: "ingredients"},
this.props.items.map(this.renderListItem)
)
}
})
```

>最早的方法

## 继承React.Component

```jsx
class IngredientsList extends React.Component {
renderListItem(ingredient, i) {
return React.createElement("li", { key: i }, ingredient)
}
render() {
return React.createElement("ul", {className: "ingredients"},
this.props.items.map(this.renderListItem)
)
}
}
```

## Stateless Functional Components

一个接受props返回 react element的函数

没有this？

>使用class this是绑定在object
>
>但是函数的this指代不明 最好不用

**Stateless functional components are functions that take in properties and return**
**a DOM element.**

```jsx
const IngredientsList = ({items}) =>
React.createElement("ul", {className: "ingredients"},
items.map((ingredient, i) =>
React.createElement("li", { key: i }, ingredient)
)
)
```



# Factories

**If you would like to simplify your code by calling components as functions,**
**you need to explicitly create a factory**

```jsx
const { render } = ReactDOM;
const IngredientsList = ({ list }) =>
React.createElement('ul', null,
list.map((ingredient, i) =>
React.createElement('li', {key: i}, ingredient)
)
)
const Ingredients = React.createFactory(IngredientsList)
const list = [
"1 lb Salmon",
"1 cup Pine Nuts",
"2 cups Butter Lettuce",
"1 Yellow Squash",
"1/2 cup Olive Oil",
"3 cloves of Garlic"
]
render(
Ingredients({list}),
document.getElementById('react-container')
)
```

#  JSX

props destructuring

# refs

## in ES6 class

```jsx
import { Component } from 'react'
class AddColorForm extends Component {
constructor(props) {
super(props)
this.submit = this.submit.bind(this)
}
submit(e) {
const { _title, _color } = this.refs
e.preventDefault();
alert(`New Color: ${_title.value} ${_color.value}`)
_title.value = '';
_color.value = '#000000';
_title.focus();
}
render() {
return (
<form onSubmit={this.submit}>
<input ref="_title"
type="text"
placeholder="color title..." required/>
<input ref="_color"
type="color" required/>
<button>ADD</button>
</form>
)
}
}
```

## in Stateless Functional Components

```jsx
const AddColorForm = ({onNewColor=f=>f}) => {
let _title, _color
const submit = e => {
e.preventDefault()
onNewColor(_title.value, _color.value)
_title.value = ''
_color.value = '#000000'
_title.focus()
}
return (
<form onSubmit={submit}>
<input ref={input => _title = input}
type="text"
placeholder="color title..." required/>
<input ref={input => _color = input}
type="color" required/>
<button>ADD</button>
</form>
)
}
```

