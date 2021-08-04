---
title: PersonalWorkHistory
description: 
published: true
date: 2021-05-01T05:56:08.682Z
tags: 
editor: markdown
dateCreated: 2021-05-01T05:55:08.963Z
---

### Test

#### Test Service Center 업무

2013-2015

1. 단말 대여 시스템 구축 및 운영
    1. Android Mobile App Test를 위한 각 제조사별 단말 대여 시스템 구축 운영
    2. Apache/Tomcat + Java Spring Framework + Mysql
    3. 기본적인 MVC 패턴으로 구현
2. 테스트 업무
    1. LG 그룹 자매사 및 공공 Open 사업 Android App Test
    2. 성능 테스트
        1. App 이용시 응답시간, 자원 사용률 등을 파악
    3. 3자 테스트
        1. 단위 테스트 케이스 개발/수행
            1. UI 시나리오를 준수하고 있는지?
            2. 각 단말별 호환성이 확보되어 있는지?
            3. 응답시간 및 자원사용량 등 성능에 이상이 있는지?
    4. 통합 테스트 
        1. 시나리오 테스트



### Develop

#### Android Mobile App Test 자동화 Tool 개발

2014

Android 모바일 UI 자동화 테스트를 위한 Program

1. 환경구성

   1. Web System
      1. Apache/Tomcat + Java Spring Framework + Mysql + Web Basic Tec.(Javascript, JQuery, HTML, JSP)
   2. Java Applet Client
      1. Java Applet + (Android) SDK Tools [+ Python]

2. ##### Test 실행 및 Test Case 별 Test Script 관리 및 결과 저장

   1. Test 에 대한 기본적인 정보를 저장하고, Test Case를 관리
   2. Test Script 를 Pyhton 형태로 작성

3. ##### Device 와 연결하여 Test Script를 직접 수행

   1. Java Applet 기반 Agent 구현
   2. Android SDK Tool (Monkey Runner) 기반 Script Runner 구현s
      1. Device 화면의 좌표 기반으로 Test가 수행
      2. 최종 결과 이미지와 기대 이미지와 동일한지 판단

![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/Test.png)



#### Smart Device Managemant System 개선 및 운영

2016-2017

모바일 기획, 개발, 테스트 등 전반적인 업무지원 지스템 운영

1. 환경구성

   1. IBM WebSphere + LG CNS DevOn Framework + GWT(Google Web Toolkit) - SmartClient + IBM DB2 + Web Basic Tec.(Javascript, JQuery, HTML, JSP)

      * GWT(Google Web Toolkit) - SmartClient
        * Java Script GUI Framework
        * Template 방식으로 DOM 객체를 생성한 후 이후 각 화면 별로 랜더링 후 SPA와 유사하게 작동

      ![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/Apache%20Tomcat%20WEBWAS.png)

2. 요구사항 분석 및 기능 개발

   1. 주요 기능 개발

      1. 외부 시스템 연동을 위한 인터페이스 개발 및 관리

         1. DB Data Message Queue 방식

      2. 배치 프로그램 개발 및 관리

      3. File Upload 기능 개선

      4. Web UI 개선

      5. Excel File 버전 관리 및 Excel Data Parsing 후 처리

         1. Apache POI Lib. 사용 

         ![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/Excel%20Parsing.png)

3. 형상 관리 

   1. SVN

4. 품질 관리 

   1. APM(Application Performance Managemant) 모니터링 및 Transaction 감시 
   2. 단위 테스트 케이스 개발, 수행 및 조치
   3. 정석분석 Sonar

5. 배포 관리 

   1. Jenkins Build 및 Deploy

6. 데이터 관리 

   1. 데이터 정합성 확인 및 조치
   2. 통계 데이터 추출
   3. 요구사항에 맞는 데이터 추출 및 정제



#### Mobile Log Management System 구축 및 운영

2017

단말별 Log File 관리 및 File Download 이력관리, 외부 인터페이스 연계 후 로그 기반 결함 등록 및 관리

1. 환경구성
   1. Client Web system
      1. Ms Azure( Linux ) + Apache/Tomcat + Spring Framework + MySQL + Web Basic Tec.(Javascript, JQuery, HTML, JSP)
   2. Server REST API System
      1. Linux Server +  + Apache/Tomcat + Spring Framework + MySQL

![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/Azure%20Cloud.png)

1. 요구사항 분석 및 기능 개발
   1. Log File이 업로드 되는 Cloud Sync Server App 개발
      1. MS Azure Linux Instance
      2. 3자 테스터가 사외망에서 접근해야 하기에, Cloud Instance로 로그파일 업로드
      3. Log File 및 테스트 정보는 실시간 배치프로그램을 통해 내부망 Linux Server로 Sync 후 삭제 처리
   2. Sync 된 Log File을 관리 및 해당 로그파일 기준으로 외부 결함관리 시스템으로 등록
      1. REST API 구현
      2. Confluence Jira 연동
      3. HP Application LifeCycle Management의 Test 관리 연동
   3. 형상 관리
   4. SVN
2. 품질 관리
   1. 단위 테스트 케이스 개발, 수행 및 조치
   2. 정적분석 Sonar
3. 배포 관리
   1. Jenkins Build 및 Depoly



#### Software Code Quality System 개선 및 운영

2018-2019

프로젝트 별 코드품질 현황에 대한 가시화

1. 환경구성
   1. Visualize Web System
      1. Apache/Tomcat + Spring Framework + MySQL + Web Basic Tec.(Javascript, JQuery, HTML, JSP) + Google Chart
   2. Server Python Sync REST API System
      1. Python
2. 활용 정보
   1. Git / Gerrit
      1. Branch, Commit 정보
      2. Merge 등 Source code 변경 정보
   2. Jenkins
      1. Build 정보
   3. Jira
      1. Release 정보

![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/Jenkins.png)

#### IoT 기기 간 연동, 이벤트 로그 수집, 분석 System 개선

2019-2021

각종 기기 이벤트 로그를 수집하여 분석 후 상황에 맞는 이벤트를 발생시키거나, 데이터를 수집 분석하여 통계 데이터를 제공

![](https://gitlab.com/youngjun0528/moheeto-io/-/raw/master/PersonalWorkHistory/Resource/AWS.png)

1. 환경구성
   1. AWS
      1. Computing : Lambda
         1. Acceptable Test Script (newman)
         2. Elastic Search Index Control
         3. CodeDeploy - AutoScaling  
      2. Storage : S3
         1. Backup File 
         2. Build Config File
      3. Database : RDS(Mysql), ElasticCache(Redis)
      4. Development : Code Deploy
         1. Jenkins 에서 AWS Copde Deploy Call
      5. Container : Elastic Container Service, Elastic Container Registry
         1. ECR : Docker Image Version Control
         2. ECS : Docker Container Service Control
      6. Ananlyze : ElasticSearch Service, Kinesis
         1. Open Distro for Elastic Search & Kibna 
      7. Managemant : Cloud Watch
         1. System Monitoring
   2. Server-Side REST API System
      1. Apache / Tomcat + Spring Framework + MySQL + Redis (+ Kafka/Zookeeper)

#### 개인학습

[Home · Wiki · youngjun0528 / moheeto-io · GitLab](https://gitlab.com/youngjun0528/moheeto-io/-/wikis/home)

##### Front-end WebSite 개발

1. Basic
   1. [youngjun0528 / ModernWebProject · GitLab](https://gitlab.com/youngjun0528/ModernWebProject)
   2. 참고서적 
      1. [Do it! 웹 사이트 따라 만들기 - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791163031192&orderClick=LAG&Kc=)
      2. [모던 자바스크립트 입문 - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160504439&orderClick=LAG&Kc=)
   3. ES6 javascript 및 HTML, CSS 학습
   4. webpack 사용법

2. VueJS
   1. [youngjun0528 / VueProject · GitLab](https://gitlab.com/youngjun0528/VueProject)
   2. 참고서적
      1. [Vue.js 코딩 공작소 - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160509229&orderClick=LAG&Kc=)
      2. [Do it! Vue.js 입문 - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791188612789&orderClick=LEa&Kc=)
3. React
   1. [youngjun0528 / ReactProject · GitLab](https://gitlab.com/youngjun0528/ReactProject)
   2. 참고서적
      1. [Do it! 클론 코딩 영화 평점 웹서비스(클론 코딩 시리즈 1) - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791163031635&orderClick=LAH&Kc=)
      2. [리액트를 다루는 기술(개정판) - 교보문고 (kyobobook.co.kr)](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791160508796&orderClick=LAH&Kc=)

##### Python Algorithm

1. [youngjun0528 / moheeto-io · GitLab](https://gitlab.com/youngjun0528/moheeto-io)
2. 그래프탐색, 이진탐색, 정렬 등 알고리즘에 대한 전반적인 문제풀이

##### 자격증

	1. ISTQB CTFL -  발행처 : KSTQB  - 취득일자 : 2014.10.01
	2. 정보처리기사 - 발행처 : 한국산업인력공단 - 취득일자 : 2014
	3. 한국사자격검정시험 - 발행처 : 국사편찬위원회 - 취득일자 : 2009.06.11
