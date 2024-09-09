# API 문서

## Accounts 관련

### 회원가입 (Sign Up)

#### 엔드포인트 (Endpoint):
- POST `/api/accounts/`

#### 요청 형식 (Request Format):
- Body (JSON 형식)

  <pre>
  {
    "username": "test",
    "email": "test@google.com",
    "password": "ps_test",
    "name": "류",
    "nickname": "YesYesMe",
    "birthdate": "1990-01-01"
  }
  </pre>

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
  {
    "id": 1,
    "username": "test",
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
    "username": "test",
    "password": "ps_test"
  }
  </pre>

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTk2MzIwMCwiaWF0IjoxNzI1ODc2ODAwLCJqdGkiOiI1MzI0ZjU3MzFmZWI0MDY2YWIyYzJjYWI1YmFlNTMzZiIsInVzZXJfaWQiOjV9.C8HRfKB9-jIH4oZvukumuMnhG4UyPIizfUOBfdMz-Xs",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODc3MTAwLCJpYXQiOjE3MjU4NzY4MDAsImp0aSI6Ijc1ZjdmMmJjMTU2ZDQ1MDQ5NDkyMWZhZjJkNTRjYzIzIiwidXNlcl9pZCI6NX0.vG1jGw0hItPgpUubSdk4yQRZQzfpvCj838olI7dGgPM"
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
  - `<username>`: 조회하려는 사용자의 이름 (예: `test`)

#### 응답 형식 (Response Format):
- Body (JSON 형식)

  <pre>
  {
    "id": 1,
    "username": "test",
    "email": "test@google.com",
    "name": "류",
    "nickname": "YesYesMe",
    "birthdate": "1990-01-01"
  }
  </pre>

#### 상태 코드 (Status Codes):
- 200 OK: 프로필 정보 반환 성공
- 400 Bad Request: 잘못된 요청
- 401 Unauthorized: 인증되지 않은 요청 (토큰이 없거나 잘못된 토큰)
- 404 Not Found: 해당 사용자가 존재하지 않음

---
