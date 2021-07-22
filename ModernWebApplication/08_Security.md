---
title: 08. Spring Security
description: 
published: true
date: 2021-07-22T07:22:03.891Z
tags: 
editor: markdown
dateCreated: 2021-07-22T07:22:03.891Z
---

# Web Application Security
## Single Sign-On
프로토콜
- SAML(Security Assertion Markup Lanquage)
- CAS(Cenral Authentication Service)

1. 어플리케이션이 사용자를 아이덴티티 서버(Identity Server)로 리다이렉트
2. 인증을 수행하기 위해 아이덴티티 서버에 응답
3. 인증 결과를 어플리케이션 전달

SAML
서비스 제공자(Service Provider, SP)(어플리케이션)는 SAML asserion(인증 결과)을 인증 제공자(Identity Provider, IdP)(아이덴티티 서버) 로부터 받는다.
인증 결과는 사용자 정보(이름, 이메일 주소, 인증 제공자 측에서 활용하는 사용자 ID)를 포함한다.

CAS
CAS 서버에 인증을 요청하고 성공시 어플리케이션으로 리다이렉트 되면서 서비스 티켓을 벋눈더, 어플리케이션은 받은 티켓이 유효한지 티켓을 이용해 CAS 서버로 요청을 보낸다.

## OAuth 2.0
서드 파티 서비스(third-party service) 가 사용자 데이터에 접근할 때 권한을 부여하기 위해 디자인

- 리소스 소유자 : 

