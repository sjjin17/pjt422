# Sub PJT - 쓰레기통 관리 시스템
## 422
422(사이이)는 ‘사소하지만 이렇게 이루어진다’의 줄임말이면서 4/22 지구의 날을 생각하여 이름이 붙여진 대학교 건물 내의 쓰레기통을 관리하는 웹 IoT 기반 시스템입니다.
<br>
<br>
<br>
<!-- 필수 항목 -->

## 카테고리

| Application | Domain | Language | Framework |
| ---- | ---- | ---- | ---- |
| :white_check_mark: Desktop Web | :black_square_button: AI | :white_check_mark: JavaScript | :white_check_mark: Vue.js |
| :black_square_button: Mobile Web | :black_square_button: Big Data | :black_square_button: TypeScript | :black_square_button: React |
| :white_check_mark: Responsive Web | :black_square_button: Blockchain | :black_square_button: C/C++ | :black_square_button: Angular |
| :black_square_button: Android App | :white_check_mark: IoT | :black_square_button: C# | :black_square_button: Node.js |
| :black_square_button: iOS App | :black_square_button: AR/VR/Metaverse | :white_check_mark: ​Python | :white_check_mark: Flask/Django |
| :black_square_button: Desktop App | :black_square_button: Game | :black_square_button: Java | :black_square_button: Spring/Springboot |
| | | :black_square_button: Kotlin | |

<!-- 필수 항목 -->

## 프로젝트 소개

* 프로젝트명: 웹 기반 교내 쓰레기통 관리 시스템
* 서비스 특징: 웹/모바일(웹 IoT) 프로젝트
* 주요 기능
  - a
* 주요 기술
  - Single Page Application
  - Raspberry Pi
  - REST API
* 참조 리소스
  - a
* 배포 환경
  - URL: // 웹 서비스, 랜딩 페이지, 프로젝트 소개 등의 배포 URL 기입
  - 테스트 계정: // 로그인이 필요한 경우, 사용 가능한 테스트 계정(ID/PW) 기입


<!-- 자유 양식 -->

## 팀 소개

* 안다영: 팀장, FE, UCC
* 김지인: FE, UCC
* 박정미: FE, UCC
* 장세진: BE, Infra
* 홍인표: BE, Infra


## 개발 스택

* FE : HTML, CSS, Javascript, Vue3, Vuex, Vue-router
* BE : Python, DJango
* Infra : SQLite, AWS EC2



<!-- 자유 양식 -->

<!-- ## 프로젝트 상세 설명 -->

<!-- // 개발 환경, 기술 스택, 시스템 구성도, ERD, 기능 상세 설명 등 -->


## 배경

- 사람들이 무분별하게 버린 쓰레기로 인해 쓰레기통이 쉽게 오염되고, 방치된 쓰레기통은 악취와 벌레 꼬임을 유발해 관리가 더욱 어려워진다.
- 올바른 분리배출(라벨지 떼기, 내용물 헹구어 버리기, 재활용 마크를 확인 후 분류하기)이 제대로 이루어지지 않아 재활용율이 낮아지고 있다.



## 기능 상세

### HW

- 초음파 센서
	- 관리자가 쓰레기가 얼마나 찼는지 웹으로 확인 가능
	- 쓰레기통이 얼마나 찼는지 쓰레기통 외부의 LED로 사용자가 확인
- NFC, RFID
  - 기존 학생증과 출입증의 ID를 이용하여 추가적인 인증 장비를 필요로 하지 않음
	- 쓰레기를 버릴 때 사용자가 무분별하게 버리지 않도록 태그 시에만 쓰레기통이 열림
	- 관리자가 태그 시 쓰레기를 언제 비웠는지에 대한 데이터가 DB로 전송 --> 일정 시간마다 쓰레기를 비울 수 있도록 구현
- LCD
	- 쓰레기통의 분류를 표시 -> 일반/종이/플라스틱/캔/유리
- HW 추가 사항
	- 채로 음료 안의 알갱이 같은 것은 걸러지도록 하고, 나머지는 필터를 달아서 자연에 방류
	- 컵 내의 내용물을 씻을 수 있는 곳
	- 거울, 태그를 할 때마다 사진을 찍어서 양심 자극
	- 다 찼을 때는 RFID를 찍어도 더 이상 열리지 않고 가장 가까운 쓰레기통을 알려줄 수 있도록 함

### Frontend(Vue.js)
시스템 관리자, 관리자(미화원), 학생 세 분류의 유저가 존재하고 일부는 특정 기능 접근 권한이 제한됨
- 모든 화면 공통 component
  - navigation bar : main, stats, settings tap과 로그인 버튼이 표시됨
- 로그인 화면
  - 로그인을 통해 관리자 전용 화면으로의 전환이 가능
- 시스템 관리자 전용 화면
  - 관리자의 권한을 모두 가지고 있음
  - hover를 통해 해당 쓰레기통의 자세한 정보를 확인할 수 있고 해당 정보를 수정하는 것이 가능함(예시:A동 1층 3구역은 유리의 배출이 거의 없고 플라스틱의 배출량이 상당하므로 해당 쓰레기통을 유리 대신 플라스틱으로 변경함)
  - 지도나 쓰레기통을 추가/제거할 수 있음
  - (설정 탭) 관리자를 관리하고 추가할 수 있음
- 관리자 전용 화면
	- 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨 
    - 층은 관리자가 한 눈에 현황을 파악할 수 있도록 엘리베이터 버튼처럼 표시됨
    - 층은 색상(쓰레기통 채워짐 정도, 숫자도 함께 표시), 경고 아이콘(비운 지 오래되거나 꽉 찬 쓰레기통 경고), 알림 아이콘(알림 개수)으로 표현됨
	- 지도 내부에 쓰레기통 안의 내용물 양이 색과 숫자로 표시됨
    - 초록색: 0 ~ 39%
    - 노란색: 40% ~ 69%
    - 빨간색: 70% ~ 100%
  - hover를 통해 해당 쓰레기통의 자세한 정보를 확인할 수 있음
  - 쓰레기통의 분류 변경 가능
    - 한 층에 각 분류가 최소 하나 씩은 있도록 구현
  - 비운지 오래되거나 꽉 찬 쓰레기통은 경고 아이콘이 표시됨
  - 메인 화면과 통계 화면 사이 전환 가능
  - (통계 탭) 알림 메시지 리스트가 표시됨
  - (통계 탭) 쓰레기통 ID, 최근 비움 시간, 위치, 종류, 마지막으로 비운 사람 등이 표로 나타나있고 각 column을 기준으로 정렬 가능
  - (통계 탭) 일정한 기간의 배출량 확인 가능
  - 로그아웃 구현
- 사용자 전용 화면
	- 층을 선택하면 해당 층의 단면도가 나오고, 쓰레기통의 위치가 표시됨
	- 쓰레기통 사용 가능 여부 확인
- 내비게이션 바
  - 로고, 화면 분류, 알림 메시지 아이콘(개수 포함), 로그인/로그아웃 버튼 등으로 구성  
- Frontend 추가 사항
	- 관리자) 마지막으로 비워 둔 시간, 시간 별, 장소 별 통계를 내서 어느 곳에서 어느 시간에 쓰레기가 많이 찰지 예측
	- 사용자) 올바른 분리배출 가이드 제공

### Backend(Python DJango, Maria DB)

* 구성요소
  - 각 쓰레기통 위치, 종류, 이벤트, 각 층/분류 등등
* 로그인
  * 관리자 로그인
  * 나머지 유저 비 로그인

* DB
  * Table
    * 건물
    * 위치
    * 쓰레기통
    * 관리자
    * 학생 + 교직원
    * 사용 내역
    
  * 관계
    * 건물 - 위치 (1 : M)
    * 위치 - 쓰레기통 (1 : M)
    * 쓰레기통 - (학생 + 교직원) (M : N)


- 로그 (구현 예정)



##	구현 목록

##	세부 사항


##	추가 기능   


##	유지보수 측면   
