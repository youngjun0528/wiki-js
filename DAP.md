---
title: DAP
description: 
published: true
date: 2021-05-24T05:56:08.682Z
tags: 
editor: markdown
dateCreated: 2021-05-24T05:55:08.963Z
---

1.  요구사항 문서

우리 회사는 육류가공식품을 생산하는 업체로 육류가공을 위한 제법 큰 규모의 공장을 운영하고 있다.

우리는 많은 설비들을 24시간 가동하여 제품을 생산하고 있으며, 

설비가 고장나지 않도록 **_관리부서_**를 지정하여 운영하면서 고장 발생 시 **공무부서**로 측각 작업의뢰를 한다. 

작업의뢰는 굳이 해당 설비의 관리부서가 아니라도 의뢰할수 있으며, 이와 관련하여 **언제**, **어느 부서**에서 **어떤 설비**에 대해 **무슨 내용**으로 의뢰한 것인지를 관리해야 한다. 

**작업의뢰**는 사안 에 따라 **_긴급의뢰_**와 **_일반의뢰_**로 구분할수 있는데, 

고장 발생으로 긴급 복구가 필요한 경우는 **고장발생일시**와 함께 긴급의뢰로, 

일반적인 개선에 대한 요청일 때는 일반의뢰로 요청을 하도록 하고있다 

관리 대상인 **설비**는 **설비번호**를 부여하여 설비명, 모델명과 함께 관리하고 있으며,

해당 설비 에 대해 구입처, 제작업체, 설치업체, 수리업체 등을 관리 하여야 한다. 

이들 _설비관련업체__는 종류별로 하나 이상_일 수 있다. 

이와 관련하여 우리는 이들 업체들에 고객번호를 부여하여 관리하고 있다. 

이 업체들 중에는 법인도 있고 개인사업자도 있으며, 이들에 대해 사업자 번호, 대표자 영, 주소, 연락전화번호 등을 관리하고, 

법인인 경우는 업체명도 관리하고 있다. 

의뢰된 작업은 사안에 따라 _몇 개의 의뢰를 묶어서 한 번의 작업으로 처리_하거나 _몇 개의 작업으로 분할하여 처리_할수 있다. 

공무부서들은 의뢰 내용을 판단하여 _자체적으로 작업_하기도 하고, 외주공사로 처리하기도 하여, 

작업실적에 대한 작업주체는 공무부서 중 하나이거나 외부 의 수리업체 일 수도 있다. 

작업실적을 관리하기 위해 작업번호를 부여하고, 작업명과 조치내용, 작업시작일시와 종료일시를 관리하며, 

자체작업인 경우는 어느 부서가 작업했는지를 관리하고, 외주공사인 경우는 수리업체와 함께 외주공사에 대한 투자코드가 있으면 이것도 관리한다. 

외주 공사에 대한 수리업체는 대상 작업에 포함된 설비에 따라 하나 이상일 수 있으나 편의상 대표 로 하나의 업체만 선정하여 관리하고, 

나머지 업체는 선정된 업체가 알아서 관리하여 업을 수 행하도록 하고 있으며, 외주공사를 맡기는 수리업체는 법인에 국한하고 있다

2\. 테이블

|     |
| --- |
| **\[설비\]** |
| 설비번호 |
| 설비명 |
| 모델명 |

|     |
| --- |
| **\[설비관리업체\]** |
| 고객번호 |
| 설비업체코드 |
| 설비번호 |

|     |
| --- |
| **\[설비업체코드\]** |
| 구입처 / 제작업체 / 설치업체 / 수리업체 |

|     |
| --- |
| **\[설비업체\]** |
| 사업자번호 |
| 대표자명 |
| 주소  |
| 전화번호 |
| 업체구분 |

|     |
| --- |
| **\[법인\]** |
| 업체명 |

|     |
| --- |
| **\[개인사업자\]** |
|     |

|     |
| --- |
| **\[작업의뢰\]** |
| 작업의뢰구분 |
| 작업의뢰번호 |
| 작업의뢰일시 |
| 작업의뢰부서 |
| 설비번호 |
| 작업의뢰내용 |

|     |
| --- |
| **\[긴급의뢰\]** |
| 고장발생일시 |

|     |
| --- |
| **\[일반의뢰\]** |
|     |

|     |
| --- |
| **\[작업실적\]** |
| 작업번호 |
| 작업명 |
| 조치내용 |
| 작업시작일시 |
| 종료일시 |
| 작업구분 |

|     |
| --- |
| **\[자제작업\]** |
| 작업부서 |

|     |
| --- |
| **\[외주공사\]** |
| 수리업체 |
| 투자코드 |

3\. ERD
```diagram
PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIHdpZHRoPSIxcHgiIGhlaWdodD0iMXB4IiB2aWV3Qm94PSItMC41IC0wLjUgMSAxIiBjb250ZW50PSImbHQ7bXhmaWxlIGhvc3Q9JnF1b3Q7ZW1iZWQuZGlhZ3JhbXMubmV0JnF1b3Q7IG1vZGlmaWVkPSZxdW90OzIwMjEtMDUtMjRUMDU6NTY6MDEuNDEzWiZxdW90OyBhZ2VudD0mcXVvdDs1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzkwLjAuNDQzMC4yMTIgU2FmYXJpLzUzNy4zNiZxdW90OyB2ZXJzaW9uPSZxdW90OzE0LjcuMCZxdW90OyBldGFnPSZxdW90O1kyZGlrUXNydHlXVDd3eUxHdjVWJnF1b3Q7IHR5cGU9JnF1b3Q7ZW1iZWQmcXVvdDsmZ3Q7Jmx0O2RpYWdyYW0gaWQ9JnF1b3Q7TENkcjlHZUdsbU1VVXRWcFpGTFQmcXVvdDsgbmFtZT0mcXVvdDtQYWdlLTEmcXVvdDsmZ3Q7ZFpIQkRvTWdESWFmaHJ2Q292UHMzTHpzNUdGbklwMlFvRFhJb3R2VFR3UE9FYmVraC9iclgzNG9oT1h0ZERHOGwxY1VvQW1OeEVUWWlWQWFIeWdsUzBUaTZVaWFKUTQwUmdrdjJrQ2xYdUJoNU9sRENSZ0NvVVhVVnZVaHJMSHJvTFlCNDhiZ0dNcnVxRVBYbmpld0ExWE45WjdlbExEUzBTTk5OMTZDYXVUcUhDZVo2N1I4RmZ1WERKSUxITDhRS3dqTERhSjFXVHZsb0pmbHJYdHhjK2MvM2MvRkRIVDJ4OENjYkdmUFJmQkRySGdEJmx0Oy9kaWFncmFtJmd0OyZsdDsvbXhmaWxlJmd0OyI+PGRlZnMvPjxnLz48L3N2Zz4=
```
