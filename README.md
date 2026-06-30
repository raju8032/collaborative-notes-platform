notes
#Notes Management Module

## Overview

This module implements the Notes Management functionality for the Collaborative Notes Platform. It provides REST APIs for creating, retrieving, updating, deleting, and searching notes. The module is designed to integrate with the Authentication module developed.
---

## Features

- Create new notes
- View all notes
- View a single note
- Update existing notes
- Delete notes
- Search notes by title or content

---

## Folder Structure

backend/
├── config/
│   └── db.js
├── controllers/
│   └── noteController.js
├── models/
│   └── noteModel.js
├── routes/
│   └── noteRoutes.js

database/
└── notes.sql

---

## Technologies Used

- Node.js
- Express.js
- MySQL
- mysql2

---

## Installation

### Install Dependencies

```bash
npm install
```

### Start the Server

```bash
node server.js
```

or

```bash
npm start
```

---

## Database Setup

Create a MySQL database.

```sql
CREATE DATABASE collaborative_notes;
```

Import the database schema.

```sql
SOURCE database/notes.sql;
```

Configure database credentials in

```
config/db.js
```

Example

```javascript
host: "localhost"
user: "root"
password: ""
database: "collaborative_notes"
```

---

## API Endpoints

### Create # Member 2 - Notes Management Module

## Overview

This module implements the Notes Management functionality for the Collaborative Notes Platform. It provides REST APIs for creating, retrieving, updating, deleting, and searching notes. The module is designed to integrate with the Authentication module developed by Member 1.

---

## Features

- Create new notes
- View all notes
- View a single note
- Update existing notes
- Delete notes
- Search notes by title or content

---

## Folder Structure

backend/
├── config/
│   └── db.js
├── controllers/
│   └── noteController.js
├── models/
│   └── noteModel.js
├── routes/
│   └── noteRoutes.js

database/
└── notes.sql

---

## Technologies Used

- Node.js
- Express.js
- MySQL
- mysql2

---

## Installation

### Install Dependencies

```bash
npm install
```

### Start the Server

```bash
node server.js
```

or

```bash
npm start
```

---

## Database Setup

Create a MySQL database.

```sql
CREATE DATABASE collaborative_notes;
```

Import the database schema.

```sql
SOURCE database/notes.sql;
```

Configure database credentials in

```
config/db.js
```

Example

```javascript
host: "localhost"
user: "root"
password: ""
database: "collaborative_notes"
```

---

## API Endpoints

### Create Note

POST /api/notes

Request

```json
{
  "title": "Meeting Notes",
    "content": "Project discussion",
      "created_by": 1,
        "team_id": 1
        }
        ```

        Response

        ```json
        {
          "message": "Note Created"
          }
          ```

          ---

          ### Get All Notes

          GET /api/notes

          ---

          ### Get Note by ID

          GET /api/notes/:id

          Example

          ```
          GET /api/notes/3
          ```

          ---

          ### Update Note

          PUT /api/notes/:id

          Request

          ```json
          {
            "title": "Updated Title",
              "content": "Updated Content"
              }
              ```

              ---

              ### Delete Note

              DELETE /api/notes/:id

              ---

              ### Search Notes

              GET /api/notes/search?keyword=project

              ---

              ## Expected Integration

              This module requires

              - User Authentication Module (Member 1)
              - Database Connection
              - Express Application

              Authentication middleware can be added later to restrict access to authenticated users.

              ---

              ## Testing

              The APIs were tested using

              - Postman

              Tested Operations

              - Create Note
              - Read Note
              - Update Note
              - Delete Note
              - Search Note

              ---

              ## Developed By

              Member 2

              Module:
              Notes Management

              Responsibilities:

              - CRUD Operations
              - Search Functionality
              - Database Integration
              - REST API Development
```

Response

```json
{
  "message": "Note Created"
}
```

---

### Get All Notes

GET /api/notes

---

### Get Note by ID

GET /api/notes/:id

Example

```
GET /api/notes/3
```

---

### Update Note

PUT /api/notes/:id

Request

```json
{
  "title": "Updated Title",
  "content": "Updated Content"
}
```

---

### Delete Note

DELETE /api/notes/:id

---

### Search Notes

GET /api/notes/search?keyword=project

---

## Expected Integration

This module requires

- User Authentication Module (Member 1)
- Database Connection
- Express Application

Authentication middleware can be added later to restrict access to authenticated users.

---

## Testing

The APIs were tested using

- Postman

Tested Operations

- Create Note
- Read Note
- Update Note
- Delete Note
- Search Note

---

## Developed By
Name : R N Joshika
Module:
Notes Management

Responsibilities:

- CRUD Operations
- Search Functionality
- Database Integration
- REST API Development
