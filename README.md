# 🏫 GSC WEB : 스마트 학과 관리 솔루션

> **교실 환경 모니터링부터 공정한 당번 관리까지**  영진전문대 글로벌시스템융합과(GSC) 학생들을 위한 **All-in-One 웹 서비스**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7.0-DC382D?style=flat-square&logo=redis&logoColor=white)

<br>

**언어 선택 (Language):**
**🇰🇷 한국어** | [🇯🇵 日本語](./README_JP.md)

---

## 💡 프로젝트 소개

매일 반복되는 학과 생활의 불편함을 해결하기 위해 개발된 **IoT 기반 스마트 통합 관리 시스템**입니다.

---

## 🚀 핵심 기능

### 1. 실시간 교실 환경 대시보드
- **Zero-Refresh:** IoT 센서 데이터를 **새로고침 없이 실시간**으로 그래프에 반영
- **Data Archive:** 지난 1년간의 월별 평균 온·습도 데이터 시각화

### 2. 공정성 100% 청소 당번 매칭
- **Fair Algorithm:** '최근 수행자 제외', '성별 균형(여학생 포함)' 등 공정 로직 적용
- **History Tracking:** 당번 수행 이력 DB 관리로 중복 당첨 차단

### 3. 스마트 커리큘럼 관리
- **Dynamic Timetable:** 1~3학년 전체 시간표 웹 조회 및 관리자 수정 기능

---

## 🛠️ 기술 스택

| 영역 | 기술 스택 | 비고 |
|:---:|---|---|
| **Backend** | **Python, Flask** | RESTful API 서버 구축 |
| **Database** | **MySQL (SQLAlchemy)** | 데이터 무결성 보장 |
| **Real-time** | **Redis + SSE** | 초고속 실시간 스트리밍 구현 |
| **Frontend** | **HTML/CSS/JS (Jinja2)** | 직관적인 UI/UX |
| **Batch** | **APScheduler** | 대용량 데이터 통계 자동화 |

---

## 👨‍💻 기술적 챌린지 (Highlights)

### 1. HTTP Polling 한계 극복 → SSE 도입
- **문제:** 잦은 Polling 요청으로 인한 트래픽 과부하 및 딜레이 발생
- **해결:** **Server-Sent Events(SSE)** 도입으로 단방향 실시간 통신 구현
- **결과:** 네트워크 리소스 절감 및 **지연 없는 실시간 그래프** 구현

### 2. 당번 선출 알고리즘 고도화
- **문제:** 단순 랜덤 추첨 시 성비 불균형 및 연속 당첨 문제 발생
- **해결:** **미수행자 우선 + 성별 쿼터제 + 직전 수행자 배제** 로직 구현
- **결과:** 시스템 도입 후 당번 선정 편리화

### 3. 대용량 데이터 처리 최적화
- **문제:** 분 단위 센서 데이터 누적으로 인한 통계 조회 속도 저하
- **해결:** **APScheduler**를 이용한 월별 데이터 자동 집계/이관 배치 작업 구축
- **결과:** 통계 조회 속도 **0.1초 미만** 유지

---

## 👤 Project Member

| 이름 | 역할 | Github |
|:---:|:---:|:---:|
| **민수현** | Full-Stack Developer | [@min-shy03](https://github.com/min-shy03) |
