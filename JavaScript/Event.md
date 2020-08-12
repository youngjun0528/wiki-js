***
### 참조링크
[이벤트 리스너와 콜백(event listener, callback)](https://www.zerocho.com/category/JavaScript/post/57432d2aa48729787807c3fc)
[이벤트 버블링, 이벤트 캡처 그리고 이벤트 위임까지](https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/#%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%B2%84%EB%B8%94%EB%A7%81---event-bubbling)

***
# 이벤트 등록
```html
<button>add one item</button>
```
```javascript
var button = document.querySelector('button');
button.addEventListener('click', addItem);

function addItem(event) {
	console.log(event);
}
```
