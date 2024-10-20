import secrets
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.config import settings

from .base import Base
from .mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .user import User


def generate_secret_token() -> str:
    return secrets.token_urlsafe(settings.access_token.token_length)


class AccessToken(IntIdPkMixin, Base):
    token: Mapped[str] = mapped_column(
        unique=True,
        default=generate_secret_token,
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
    )
    user: Mapped["User"] = relationship(
        back_populates="access_tokens",
    )

    @classmethod
    def generate_token(cls) -> str:
        return generate_secret_token()