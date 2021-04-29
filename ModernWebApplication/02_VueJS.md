---
title: 02.Vue.js
description: 
published: true
date: 2021-04-29T23:43:43.248Z
tags: 
editor: markdown
dateCreated: 2021-04-19T05:36:56.365Z
---

# 기본개념
## Vue 인스턴스
1. 루트 인스턴스 생성
```javascript
new Vue({/*option*/})
```
### index.html
```html
<!DOCTYPE html>
<html>
<head>
  <title>Message App</title>
  <style>
    [v-cloak] {display: none;}
    boby > div {width: 500px; margin:0 auto;}
    textarea {width: 100%;}
    ul {padding: 0 15px;}
  </style>
</head>
<body>
	<div id="app" v-cloak>
    <message-list :items="messages" @delete="deleteMessage"></message-list>
  	<ul>
      	<li v-for="message in messages">
          {{ message.text }} - {{message.createAt}}
          <button v-on:click="deleteMessage(message)">X</button>
        </li>
    </ul>
    <form @submit.prevent="addMessage">
      	<textarea v-model="newMessage" placeholder="Leave a message">
      	</textarea>
      	<div>
          <button v-bind:disable="addDisabled" type="submit">Add</button>
        </div>
    </form>
  </div>
  <script src="https://unpkg.com/vue@2.5.13/dist/vue.js"></script>
  <script>
    let vm = new Vue({
    	el: '#app',
      data:{
        	message:[],
        	newMessage: ''
      },
      computed: {
      	addDisabled(){
        	return this.messages.length >= 10 || this.newMessage.length > 50;
        }
      },
      methods: {
        addMessage (event) {
        	if(!this.newMessage){return;}
          this.messages.push({
            	text: this.message, crateAt: new Date()
          });
          this.newMessage = '';
        },
        deleteMessage (message) {
        	this.messages.splice(this.messages.indexOf(message), 1)
        }
      }
    });
  </script>
</body>
</html>
```
- 6,13 line : 브라우저는 Vue.js를 로드하고 실행하기전에 HTML을 그대로 표시하며, Vue.js가 DOM 제어권을 가져온 뒤 로딩된 지점부터 템플릿 마크업을 제거하고 Vue.js가 종적으로 새롭게 생성한 DOM으로 대체할 때까지 유지한다.
	* v-cloak 지시자 : 템플릿 마크업을 숨길 수 있는 CSS 규칙 추가, Flash 현상 발지
- 16 line : [v-for 지시자] 메시지 리스트를 랜더링
- 17 line : [이중중괄호 구문] messages 리스트에 있는 message 객체의 text 프로퍼티와 createAt 프로퍼티를 출력한다. 텍스트 보간법은 자바스크립트 표현식도 지원한다. ex. {{message.text.toLowerCase()}}
- 18 line : [v-on] click 이벤트에 리스너인 deleteMessage 메소드를 연결한다. 메소드 실행후 변경사항은 Vue.js가 자동으로 업데이트 한다.
- 21 line : [v-on:submit 축약형 -> @submit] submit 이벤트에 이벤트 리스너를 할당. 
	* click과 mouseover와 같은 DOM 이벤트를 할당할 수 있다.
	* prevent는 브라우저가 실제로 Form 객체를 제출하지 않도록 Vue.js에 event.preventDefault() 호출을 지시한다.
  * addMessage는 폼의 submit 이벤트가 Trigger 될때 호출되는 메소드
- 22 line : [v-model] textarea 요소와 data 객체의 newMessage 프로퍼티 사이에 양방향 바인딩을 생성
- 25 line : [v-bind:addDisabled 축약형 -> :addDisabled] 폼의 submit 이벤트를 트리거 할 수 있게 버튼 추가. Add 버튼의 disable 속성과 computed의 addDisabled 를 연결한다.
	* class와 style 같은 HTML 요소의 내장된 속성을 연결할 수 있다.
- 32 line : [el] element 줄임말, DOM 객체 ID에 Vue 객체를 삽입
- 32-26 line : [data] data 객체, 초기값 설정
- 37-41 line : [computed] 계산된 값으로 computed 프로퍼티에 종속된 대상을 추적하고 변경될때 프로퍼티의 값을 갱신한다.
- 42-53 line : 객체에서 사용하는 모든 메소드를 담는다. 메소드 내에서 this로 data 객체의 프로퍼티에 접근, 화살표 함수 구문은 사용하여서는 안된다.(this로 data 객체 참조가 불가능)

## 컴포넌트

