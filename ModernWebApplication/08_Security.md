---
title: 08. Spring Security
description: 
published: true
date: 2021-07-23T04:35:18.434Z
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

- 리소스 소유자 : 리소스 서버에 있는 데이터를 소유한 사람
- 리소스 서버 : 클라이언트가 접근하기를 원하는 데이터를 저장하는 서버
- 권한 부여 서버 : 클라이언트가 요청한 데이터로 접근할 수 있도록 권한 부여를 수행하는 서버
- 클라리언트 : 데이터에 접근하기를 원하는 어플리케이션

![screenshot_20210723-132857~2.png](/screenshot_20210723-132857~2.png)

## 권한 부여 방식
- 역할 기반(Role-bsed) : 리소스 종류 단위로 접근을 컨트롤
- 접근 제어 목록(Access Control List, ACL) : 특정 데이터에 대한 사용 및 접근 권한 목록, 작은 단위(fine-grainded)의 섬세한 권한 부여 가능

## 공격 예방
Open Web Application Security Project(OWASP) 에서 정의한 10가지 항목
1. 인젝션(Injection)
2. 취약한 인증(Broken Authentication)
3. 민감한 데이터 노출
4. XML 외부 개체(XML External Entities, XXE)
5. 취약한 접근 통제(Broken Access Control)
6. 잘못되 보안 구성
7. 크로스 사이트 스크립팅(Cross-Site Scripting)
8. 안전하지 않는 역직렬화(Insecure Desserialzation)
8. 알려진 약점이 있는 구성요소 활용
9. 불충분한 로깅 및 모니터링

# Spring Security



