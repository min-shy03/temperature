# 🏫 GSC WEB : 스마트 학과 관리 솔루션

> **교실 환경 모니터링부터 공정한 당번 관리까지**
> 영진전문대 글로벌시스템융합과(GSC) 학생들을 위한 **All-in-One 웹 서비스**

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?style=flat-square&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7.0-DC382D?style=flat-square&logo=redis&logoColor=white)

[![Service Link](https://img.shields.io/badge/Service_Live-gsc--web.cloud-6772E5?style=for-the-badge&logo=google-cloud&logoColor=white)](https://gsc-web.cloud)
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

### 2. 순환형 청소 당번 선출 엔진
- **Rolling Deck:** 전원이 한 번씩 수행할 때까지 중복 없이 순환하는 공정 알고리즘
- **Auto-Fill:** 후보 인원이 부족할 경우 즉시 데이터를 리셋하여 당번(4명) 강제 충원
- **데모:**
  <p align="center">
    <img src="https://github.com/user-attachments/assets/98cd551c-a8f8-4e1b-8e2f-7a79a3e50f36" width="600" alt="청소 당번 선출 데모">
  </p>

### 3. 스마트 커리큘럼 관리
- **Dynamic Timetable:** 1~3학년 전체 시간표 웹 조회 및 관리자 수정 기능
- **데모:**
  <p align="center">
    <img src="https://github.com/user-attachments/assets/e7697289-02e4-4557-aa66-7fb964e49d3a" width="600" >
  </p>

---

## 🛠️ 기술적 챌린지 (Highlights)

### 1. HTTP Polling 한계 극복 → SSE 도입
- **문제:** 잦은 Polling 요청으로 인한 트래픽 과부하 및 데이터 지연 발생
- **해결:** **Server-Sent Events(SSE)** 도입으로 서버 부하를 줄이고 단방향 실시간 통신 구현
- **결과:** 네트워크 리소스 절감 및 지연 없는 실시간 그래프 시각화 성공

### 2. 당번 선출 로직 고도화 및 DB 동기화
- **문제:** 후보 부족 시 선출 중단 문제 및 파이썬 객체-DB 간 상태 불일치(Stale Data)로 인한 데이터 누락 발생
- **해결:** 1. **잔여 인원 우선 선출 + 즉시 리셋** 로직으로 인원수 제약 없는 무한 순환 구조 구축
  2. SQL `update` 대신 **객체 직접 수정 및 명시적 commit** 방식을 사용하여 완벽한 데이터 동기화 보장
- **결과:** 예외 상황 없는 안정적이고 공정한 자동 선출 시스템 완성

### 3. 대용량 데이터 처리 최적화 (Batch Task)
- **문제:** 분 단위로 누적되는 방대한 센서 데이터로 인해 월별 통계 조회 속도가 점진적으로 저하됨
- **해결:** **APScheduler**를 이용해 매월 1일 데이터 자동 집계 및 통계 테이블 이관 배치 작업 구축
- **결과:** 통계 조회 시 대량 연산을 방지하여 응답 속도를 **0.1초 미만**으로 상시 유지

---

## 👤 Project Member

| 이름 | 역할 | Github |
|:---:|:---:|:---:|
| **민수현** | Full-Stack Developer | [@min-shy03](https://github.com/min-shy03) |
