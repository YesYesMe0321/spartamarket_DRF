# API 문서

## Accounts 관련

### 회원가입 (Sign Up)

#### 엔드포인트 (Endpoint):
- POST `/api/accounts/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)

  <pre>
  {
    "username": "testuser",
    "email": "test@google.com",
    "password": "password123",
    "name": "홍길동",
    "nickname": "길동이",
    "birthdate": "1990-01-01"
  }
  </pre>

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
  {
    "id": 1,
    "username": "testuser",
    "email": "test@google.com"
  }
  </pre>

#### 상태 코드 (Status Codes):
- 201 Created: 회원가입 성공
- 400 Bad Request: 필수 필드가 누락되었거나 형식이 맞지 않음

---

### 로그인 (Login)

#### 엔드포인트 (Endpoint):
- POST `/api/accounts/login/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)

  <pre>
  {
    "username": "testuser",
    "password": "password123"
  }
  </pre>

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
  {
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
  </pre>

#### 상태 코드 (Status Codes):
- 200 OK: 로그인 성공, 토큰 발급
- 400 Bad Request: 잘못된 로그인 정보

---

### 프로필 확인 (Profile Check)

#### 엔드포인트 (Endpoint):
- GET `/api/accounts/<username>/`

#### 요청 형식 (Request Format):
- **Headers:**
  - `Authorization: Bearer <ACCESS_TOKEN>`
  
- URL Path Parameter:
  - `<username>`: 조회하려는 사용자의 이름 (예: `testuser`)

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
  {
    "id": 1,
    "username": "testuser",
    "email": "test@google.com",
    "name": "홍길동",
    "nickname": "길동이",
    "birthdate": "1990-01-01"
  }
  </pre>

#### 상태 코드 (Status Codes):
- 200 OK: 프로필 정보 반환 성공
- 400 Bad Request: 잘못된 요청
- 401 Unauthorized: 인증되지 않은 요청 (토큰이 없거나 잘못된 토큰)
- 404 Not Found: 해당 사용자가 존재하지 않음

---
