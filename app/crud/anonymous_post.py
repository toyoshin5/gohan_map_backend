from sqlalchemy.orm import Session

from app.models.anonymous_post import AnonymousPost


def fetch_anonymous_post_by_uid(db: Session, uid: str) -> list[AnonymousPost]:
    posts = db.query(AnonymousPost).filter(AnonymousPost.userId == uid).all()
    return posts
