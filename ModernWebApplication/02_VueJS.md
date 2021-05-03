---
title: 02.Vue.js
description: 
published: true
date: 2021-05-03T07:58:00.355Z
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
- 15 line : [v-for 지시자] 메시지 리스트를 랜더링
- 16 line : [이중중괄호 구문] messages 리스트에 있는 message 객체의 text 프로퍼티와 createAt 프로퍼티를 출력한다. 텍스트 보간법은 자바스크립트 표현식도 지원한다. ex. {{message.text.toLowerCase()}}
- 17 line : [v-on] click 이벤트에 리스너인 deleteMessage 메소드를 연결한다. 메소드 실행후 변경사항은 Vue.js가 자동으로 업데이트 한다.
- 20 line : [v-on:submit 축약형 -> @submit] submit 이벤트에 이벤트 리스너를 할당. 
	* click과 mouseover와 같은 DOM 이벤트를 할당할 수 있다.
	* prevent는 브라우저가 실제로 Form 객체를 제출하지 않도록 Vue.js에 event.preventDefault() 호출을 지시한다.
  * addMessage는 폼의 submit 이벤트가 Trigger 될때 호출되는 메소드
- 21 line : [v-model] textarea 요소와 data 객체의 newMessage 프로퍼티 사이에 양방향 바인딩을 생성
- 24 line : [v-bind:addDisabled 축약형 -> :addDisabled] 폼의 submit 이벤트를 트리거 할 수 있게 버튼 추가. Add 버튼의 disable 속성과 computed의 addDisabled 를 연결한다.
	* class와 style 같은 HTML 요소의 내장된 속성을 연결할 수 있다.
- 31 line : [el] element 줄임말, DOM 객체 ID에 Vue 객체를 삽입
- 32-35 line : [data] data 객체, 초기값 설정
- 36-40 line : [computed] 계산된 값으로 computed 프로퍼티에 종속된 대상을 추적하고 변경될때 프로퍼티의 값을 갱신한다.
- 42-51 line : 객체에서 사용하는 모든 메소드를 담는다. 메소드 내에서 this로 data 객체의 프로퍼티에 접근, 화살표 함수 구문은 사용하여서는 안된다.(this로 data 객체 참조가 불가능)

## 컴포넌트
vue 애플리케이션에서 코드를 재사용할 수 있는 기본적인 방법
```html
Vue.component(id, [definition])
```
###### index.html
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
    import MessageList from './components/MessageList.js'
    let vm = new Vue({
    	el: '#app',
      components: {
      	MessageList
      },
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
          let now = new Date();
        	if(!this.newMessage){return;}
          this.messages.push({
            	id: now.getTiem(), text: this.message, crateAt: new Date()
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
- 14 line : 사용자 정의 컴포넌트와 네이티브 HTML 요소에 같은 방식으로 데이터를 바인딩 하고 이벤트 리스너를 부착
	* v-bind:items -> :items
  * v-on:delete -> @delete
- 28-30 line : 사용자 정의 컴포넌트를 등록

###### components/MessageList.js
```javascript
import MessageListItem from './MessageListItem.js'
export default {
	name: 'MessageList',
	template: 
  '<ul>
  	<message-list-item v-for="item in items" :item="item" :key="item.id" @delete="deleteMessage(item)">
		</message-list-item>
	</ul>',
	components: {
  	MessageListItem
  },
	porps: {
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    deleteMessage(message) {
    	this.$emit('delete', message);
    }
  }
}
```
- 3 line : component name 프로퍼티, 필수는 아니나 디버깅에 도움
	* 프로퍼티의 이른을 파스칼표기(첫단어를 대문자로 시작)를 케밥표기법(하이픈으로 연결)으로 변환하고 컴포넌트 등록시 컴포넌트 ID로 활용
  * 부모 컴포넌트와 밀접하게 연결된 자식 컴포넌트는 부모 컴포넌트의 이름을 접두사로 표함하여야 한다.
- 4 line : inline-template
- 12-17 line : item의 프로퍼티 정의, type이 배열이고 필수 항목으로 지정, 만약 다른 값이 들어온다면 에러 발생
	* props : 자식 컴포넌트에서 부모 데이터를 참조하기 위해 선언, v-bind 지시자로 연결
- 19 line : Delete 버튼의 Cilck 이벤트 수신, $emit 으로 이벤트를 트리거, 부모 컴토넌트에서 @delete 에서 수신


###### components/MessageListItem.js
```javascript
export default {
	name: 'MessageListItem',
	template: 
  '<li v-for="item in items" :item="item">
  		{{ item.text }} - {{ item.createdAt }}
    <button @click="deleteMessage(item)">X</button>
	</li>',
	porps: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    deleteClicked(message) {
    	this.$emit('delete');
    }
  }
}
```

## Vue 인스턴스 라이프 사이클
1. beforeCreate : 인스턴스 내부 이벤트와 라이프 사이클 상태가 초기화 된 후에 호출된다.
2. created : 인스턴스의 주입과 반응형 시스템이 초기화된 후 호출된다. 이 단계에서 인스턴스는 기능을 수행하지만 DOM이 없데이트 되지 않아 사용자는 UI에서 아무것도 볼 수 없다.
3. beforMount : Vue.js가 템플릿 컴파일을 마치고 생성된 DOM을 랜더링할 준비가 된 후 호출도니다.
4. mounted : DOM이 업데이트된 후에 호출된다. 이 시점에서 사용자는 UI와 상호작용할 수 있으며 인스턴스는 완전한 기능을 수행한다.
5. beforeMount : 데이터가 변경된 이후 DOM이 업데이트되기 전에 호출된다. 이 훅에서 여전히 데이터 변경을 수행할 수 있으며, 이 변경이 추가적인 DOM 업데이트를 트리거하지 않는다.
6. updated : DOM이 데이터 변경 사항을 기반으로 업데이트 된 후에 호출된다.
7. activated : keep-alive 컴포넌트가 활성화 될 때 호출된다.
8. deactivated : keep-alive 컴포넌트가 비활성화 될 때 호출된다.
9. beforeDestroy : 인스턴스가 파괴되지 전에 호출된다. 이 단계에서 인스턴스는 여전히 완전한 기능을 수행한다.
10. destroyed : 인스턴스가 파괴된 후에 호출도니다. 이 단계에서 인스턴스의 모든 지시자 바인딩이 해제되고 모든 이벤트 리스너가 제거되며 모든 하위 Vue 인스턴스가 파괴된다.
11. errorCaptured : 자손 컴포넌트에서 에러가 검출될 때마다 호출된다.
