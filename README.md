# 개요

## 목표
- DRF 를 사용해 마켓 백엔드 기능 기초를 구현한다.
- Accounts 와 Products 앱을 추가한다.
- Accounts 앱에서는 회원가입, 로그인, 프로필 확인과 같은 Accounts CRUD 를 구현한다.
- Products 앱에서는 상품 등록, 상품 조회, 상품 수정, 상품 삭제와 같은 Products CRUD 를 구현한다.

### 프론트엔드
- 프론트엔드 구현보다는 DRF-백엔드에만 집중한다.
- templates 폴더는 배제하며 API 테스트는 POSTMAN 을 사용한다.

---

# API 문서

## Accounts 관련

### 회원가입 (Sign Up)

#### 엔드포인트 (Endpoint):
- POST `/api/accounts/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)
  {
    "username": "test",
    "email": "test@google.com",
    "password": "ps_test",
    "name": "류",
    "nickname": "YesYesMe",
    "birthdate": "1990-01-01"
  }

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "id": 1,
    "username": "test",
    "email": "test@google.com"
  }

#### 상태 코드 (Status Codes):
- 201 Created: 회원가입 성공
- 400 Bad Request: 필수 필드 누락 또는 형식 오류

---

### 로그인 (Login)

#### 엔드포인트 (Endpoint):
- POST `/api/accounts/login/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)
  {
    "username": "test",
    "password": "ps_test"
  }

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "refresh": "your_refresh_token",
    "access": "your_access_token"
  }

#### 상태 코드 (Status Codes):
- 200 OK: 로그인 성공, 토큰 반환
- 400 Bad Request: 잘못된 로그인 정보

---

### 프로필 조회 (Profile Retrieval)

#### 엔드포인트 (Endpoint):
- GET `/api/accounts/<str:username>/`

#### 요청 형식 (Request Format):
- Headers
  - Authorization: Bearer <access_token>

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "id": 1,
    "username": "test",
    "email": "test@google.com",
    "name": "류",
    "nickname": "YesYesMe",
    "birthdate": "1990-01-01"
  }

#### 상태 코드 (Status Codes):
- 200 OK: 프로필 조회 성공
- 404 Not Found: 유저를 찾을 수 없음
- 403 Forbidden: 인증 실패

---

## Products 관련

---

### 상품 목록 조회 (Product List)

#### 엔드포인트 (Endpoint):
- GET `/api/products/`

#### 요청 형식 (Request Format):
- 별도의 요청 본문 불필요

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  [
    {
      "id": 1,
      "title": "상품 1",
      "description": "상품 1 설명",
      "created_at": "2024-09-09T10:00:00Z"
    },
    {
      "id": 2,
      "title": "상품 2",
      "description": "상품 2 설명",
      "created_at": "2024-09-09T11:00:00Z"
    }
  ]

#### 상태 코드 (Status Codes):
- 200 OK: 상품 목록 조회 성공
- 500 Internal Server Error: 서버 오류

---

### 상품 등록 (Product Creation)

#### 엔드포인트 (Endpoint):
- POST `/api/products/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)
  {
    "title": "상품 제목",
    "description": "상품 설명",
    "image": "이미지 URL 또는 파일"
  }
- Headers
  - Authorization: Bearer <access_token>

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "id": 1,
    "title": "상품 제목",
    "description": "상품 설명",
    "created_at": "2024-09-09T10:00:00Z"
  }

#### 상태 코드 (Status Codes):
- 201 Created: 상품 등록 성공
- 400 Bad Request: 필수 필드 누락 또는 형식 오류

---

### 상품 수정 (Product Update)

#### 엔드포인트 (Endpoint):
- PUT `/api/products/<int:productId>/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)
  {
    "title": "수정된 상품 제목",
    "description": "수정된 상품 설명"
  }
- Headers
  - Authorization: Bearer <access_token>

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "id": 1,
    "title": "수정된 상품 제목",
    "description": "수정된 상품 설명",
    "created_at": "2024-09-09T10:00:00Z"
  }

#### 상태 코드 (Status Codes):
- 200 OK: 상품 수정 성공
- 403 Forbidden: 수정 권한이 없음
- 404 Not Found: 상품을 찾을 수 없음

---

### 상품 삭제 (Product Deletion)

#### 엔드포인트 (Endpoint):
- DELETE `/api/products/<int:productId>/`

#### 요청 형식 (Request Format):
- Headers
  - Authorization: Bearer <access_token>

#### 응답 형식 (Response Format):
- Body (JSON 형식)
  {
    "detail": "상품이 삭제되었습니다."
  }

#### 상태 코드 (Status Codes):
- 204 No Content: 상품 삭제 성공
- 403 Forbidden: 삭제 권한이 없음
- 404 Not Found: 상품을 찾을 수 없음
