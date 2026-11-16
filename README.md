# Photo & Video Sharing API

A backend REST API for sharing photos and videos, built with FastAPI. Users can create an account, log in, upload media with a caption, browse a feed, and delete their own posts.

## Features

- User registration and login with JWT authentication (FastAPI Users)
- Photo and video uploads stored on ImageKit, with only the file URL and metadata saved in the database
- Feed of all posts, newest first
- Users can delete only their own posts

## Tech Stack

Python, FastAPI, SQLAlchemy (async), FastAPI Users, JWT, ImageKit, uv

## Project Structure

```
.
├── main.py
├── pyproject.toml
├── .env.example
└── src/
    ├── app.py          # app setup and router registration
    ├── db.py           # database models and session
    ├── images.py       # ImageKit client
    ├── schema.py       # Pydantic schemas
    ├── user.py         # authentication setup
    └── routers/
        ├── auth.py     # register, login, password reset, verify, users
        └── posts.py    # upload, feed, delete
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- [uv](https://docs.astral.sh/uv/)
- A free [ImageKit](https://imagekit.io/) account

### Setup

```bash
git clone https://github.com/BopGbenga/<repo-name>.git
cd <repo-name>
uv sync
```

Create a `.env` file in the project root (see `.env.example`):

```
JWT_SECRET=your_long_random_secret
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key
IMAGEKIT_URL_ENDPOINT=https://ik.imagekit.io/your_id
```

### Run

```bash
uv run uvicorn src.app:app --reload
```

Then open http://127.0.0.1:8000/docs to try the API.

## API Endpoints

| Method | Endpoint           | Description                            | Auth required |
| ------ | ------------------ | -------------------------------------- | ------------- |
| POST   | `/auth/register`   | Create an account                      | No            |
| POST   | `/auth/jwt/login`  | Log in and get an access token         | No            |
| GET    | `/users/me`        | Get the current user                   | Yes           |
| POST   | `/upload`          | Upload a photo or video with a caption | Yes           |
| GET    | `/feed`            | List all posts, newest first           | Yes           |
| DELETE | `/posts/{post_id}` | Delete one of your own posts           | Yes           |

Password reset and email verification endpoints are also included under `/auth`.

## Notes

- Password reset and verification tokens are currently printed to the server console. Sending them by email is not implemented yet.
- The project pins `imagekitio==3.1.0`, since newer major versions of the ImageKit SDK have a different API.

## Author

**Oluwagbenga Bello**, Backend Engineer
[GitHub](https://github.com/BopGbenga) · [LinkedIn](https://linkedin.com/in/bellogbenga)
