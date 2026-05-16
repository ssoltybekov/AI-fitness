from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id         = Column(Integer, primary_key=True, index=True)
    name       = Column(String(100), nullable=False)
    email      = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    sessions = relationship("TrainingSession", back_populates="user", lazy="select")


class TrainingSession(Base):
    __tablename__ = "training_sessions"

    id            = Column(Integer, primary_key=True, index=True)
    user_id       = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    timestamp     = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    weight_kg     = Column(Float, nullable=False)
    quality_score = Column(Float, nullable=False)  # 0.0 – 100.0

    errors      = Column(JSON, default=list)

    ai_feedback = Column(JSON, nullable=True)

    user = relationship("User", back_populates="sessions")