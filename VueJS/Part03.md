---
title: Part03.SPA구조
description: 
published: true
date: 2021-05-10T07:30:32.726Z
tags: 
editor: markdown
dateCreated: 2021-05-10T07:29:45.077Z
---

# Tempate 구조와 컴포넌트
1. 기본 템플릿 구조
- node_modules/ : npm 라이브러리
- public/
	* index.html : 브라우저에 보여지는 페이지
- src/
	* assets/ : Static 파일(image, css 등)
  * components/
  	* HellowWorld.vue : Vue 컴포넌트
  * views/ : Vue 정적 단일 Tempalte
  * App.vue
  * main.js : Main. Vue 인스턴스 생성, 각종 모듈 IMPORT
  * router/
  	* index.js : 앱 라우터 설정
  * store/
  	* index.js : vuex. 상태광리 모듈 설정
- package.json : npm 설정