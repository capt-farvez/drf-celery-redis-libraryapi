# API Documentation 


## Base URL
```
http://127.0.0.1:8000/v1/api/
```

---

##  Endpoints

### ✅ Authors

#### 1. Create Author:

- **URL:** `POST /v1/api/authors/`
- **Body:**
```json
{
  "name": "John Doe",
  "date_of_birth": "1980-01-01"
}
```
#### 2. Get All Authors:

- **URL:** `GET /v1/api/authors/`
- **Response:**
```
[
  {
    "id": 1,
    "name": "John Doe",
    "date_of_birth": "1980-01-01"
  }
]
```
#### 3. Get Author by ID

- **URL:** `GET /v1/api/authors/1/`

#### 4. Update Author
- **URL:** `PUT /v1/api/authors/1/`
- **Body:**
```
{
  "name": "John D.",
  "date_of_birth": "1980-01-01"
}
```
#### 5. Delete Author

- **URL:** `DELETE /v1/api/authors/1/`


### 📖 Books
#### 1. Create Book with Existing Author
- **URL:** `POST /v1/api/books/`
- **Body:**
```
{
  "title": "Django for APIs",
  "author": 1,
  "published_date": "2013-05-06",
  "genre": "Programming"
}
```
**author is the Author ID**

#### 2. Get All Books
- **URL: GET /v1/api/books/**

#### 3. Filter Books by Author Name
- **URL:** `GET /v1/api/books/?author_name=John`

#### 4. Get Book by ID
- **URL:** `GET /v1/api/books/1/`

#### 5. Update Book
- **URL:** `PUT /v1/api/books/1/`
- **Body:**
```
{
  "title": "Django for APIs - Updated",
  "author": 1,
  "published_date": "2013-05-06",
  "genre": "Programming",
  "is_archived": false
}
```
#### 6. Delete Book
- **URL:** `DELETE /v1/api/books/1/`