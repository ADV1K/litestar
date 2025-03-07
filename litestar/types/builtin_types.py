from __future__ import annotations

from typing import TYPE_CHECKING, Type, Union

from typing_extensions import _TypedDictMeta  # type: ignore

if TYPE_CHECKING:
    from typing_extensions import TypeAlias

__all__ = (
    "NoneType",
    "UnionType",
    "UnionTypes",
    "TypedDictClass",
)

NoneType: type[None] = type(None)

try:
    from types import UnionType  # pyright: ignore
except ImportError:
    UnionType: TypeAlias = Union  # type: ignore[no-redef]

UnionTypes = {UnionType, Union}
TypedDictClass: TypeAlias = Type[_TypedDictMeta]
